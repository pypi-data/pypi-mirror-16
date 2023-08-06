import os
import subprocess
import time
import logging

import requests
from requests import exceptions, Session

from python_kemptech_api import utils
from python_kemptech_api.api_xml import (
    get_error_msg, is_successful,
    get_data_field, parse_to_dict,
    get_data)
from python_kemptech_api.exceptions import (
    KempTechApiException,
    CommandNotAvailableException,
    ConnectionTimeoutException,
    VirtualServiceMissingLoadmasterInfo,
    RealServerMissingLoadmasterInfo,
    RealServerMissingVirtualServiceInfo,
    LoadMasterParameterError,
    ValidationError,
    SubVsCannotCreateSubVs,
    BackupFailed,
    DownloadUserCertFailed,
    UnauthorizedAccessError,
    UserAlreadyExistsException,
    NotVirtualServiceInstanceError)
from python_kemptech_api.capabilities import CAPABILITIES, DEFAULT
from .utils import (
    validate_port,
    validate_ip,
    validate_protocol,
    UseTlsAdapter,
    get_sub_vs_list_from_data,
    get_api_bool_string,
    get_dict_entry_as_list,
    cast_to_list,
    falsey_to_none)


requests.packages.urllib3.disable_warnings()
log = logging.getLogger(__name__)


class HttpClient(object):
    """Client that performs HTTP requests."""

    ip_address = None
    endpoint = None

    def __init__(self, tls_version=utils.DEFAULT_TLS_VERSION, cert=None):
        self._tls_version = tls_version
        self.cert = cert
        self._tls_session = Session()
        self._tls_session.mount("http://", UseTlsAdapter(self._tls_version))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._tls_session.close()
        return False

    def _do_request(self, http_method, rest_command,
                    parameters=None,
                    file=None, headers=None):
        """Perform a HTTP request.

        :param http_method: GET or POST.
        :param rest_command: The command to run.
        :param parameters: dict containing parameters.
        :param file: Location of file to send.
        :param headers: Optional headers to send.
        :return: The Status code of request and the response text body.
        """

        cmd_url = "{endpoint}{cmd}?".format(endpoint=self.endpoint,
                                            cmd=rest_command)
        log.debug("Request is: %s", cmd_url)

        try:
            if file is not None:
                with open(file, 'rb') as payload:
                    response = self._tls_session.request(http_method, cmd_url,
                                                         params=parameters,
                                                         verify=False,
                                                         data=payload,
                                                         headers=headers,
                                                         cert=self.cert)
            else:
                response = self._tls_session.request(http_method, cmd_url,
                                                     params=parameters,
                                                     timeout=utils.TIMEOUT,
                                                     verify=False,
                                                     headers=headers,
                                                     cert=self.cert)
            self._tls_session.close()
            if response.status_code == 401:
                log.warning("Cannot authenticate to %s check that the "
                            "credentials are correct.", self.ip_address)
                raise UnauthorizedAccessError(self.ip_address,
                                              response.status_code)
            elif 400 < response.status_code < 500:
                raise KempTechApiException(msg=response.text,
                                           code=response.status_code)
            else:
                response.raise_for_status()
        except exceptions.ConnectTimeout:
            log.error("The connection timed out to %s.", self.ip_address)
            raise ConnectionTimeoutException(self.ip_address)
        except exceptions.ConnectionError:
            log.error("A connection error occurred to %s.", self.ip_address)
            raise
        except exceptions.URLRequired:
            log.error("%s is an invalid URL", cmd_url)
            raise
        except exceptions.TooManyRedirects:
            log.error("Too many redirects with request to %s.", cmd_url)
            raise
        except exceptions.Timeout:
            log.error("A connection %s has timed out.", self.ip_address)
            raise
        except exceptions.HTTPError:
            log.error("A HTTP error occurred with request to %s.", cmd_url)
            raise KempTechApiException(msg=response.text,
                                       code=response.status_code)
        except exceptions.RequestException:
            log.error("An error occurred with request to %s.", cmd_url)
            raise
        return response.text

    def _get(self, rest_command, parameters=None, headers=None):
        return self._do_request('GET', rest_command, parameters,
                                headers=headers)

    def _post(self, rest_command, file=None, parameters=None, headers=None):
        return self._do_request('POST', rest_command, parameters=parameters,
                                file=file, headers=headers)


def send_response(response):

    if is_successful(response):
        return parse_to_dict(response)
    else:
        raise KempTechApiException(get_error_msg(response))


class LoadMaster(HttpClient):
    """LoadMaster API object."""

    def __init__(self, ip, username=None, password=None, port=443,
                 cert=None):
        self.ip_address = ip
        self.username = username
        self.password = password
        self.port = port
        self.cert = cert
        self.version = None
        super(LoadMaster, self).__init__(utils.DEFAULT_TLS_VERSION, self.cert)

    def __repr__(self):
        return '{}:{}'.format(self.ip_address, self.port)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.version == other.version
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.version > other.version
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.version < other.version
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.version >= other.version
        else:
            return False

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.version <= other.version
        else:
            return False

    @property
    def endpoint(self):
        if self.cert:
            return "https://{ip}:{port}/access".format(
                ip=self.ip_address,
                port=self.port
            )
        else:
            return "https://{user}:{pw}@{ip}:{port}/access".format(
                user=self.username,
                pw=self.password,
                ip=self.ip_address,
                port=self.port
            )

    @property
    def access_info(self):
        return {
            "endpoint": self.endpoint,
            "ip_address": self.ip_address,
            "cert": self.cert,
        }

    @property
    def capabilities(self):
        if self.version is None:
            self.version = "7.1.34"
        return CAPABILITIES.get(self.version, CAPABILITIES[DEFAULT])

    def _get_curl_command_list(self, command):
        curl = ['curl', '-s', '-k', '--connect-timeout', str(utils.TIMEOUT)]
        command = '{}/{}'.format(self.endpoint, command)
        if self.cert:
            curl.extend(['-E', self.cert])
        curl.append(command)
        return curl

    def clone_virtual_service(self, service, ip, port, protocol, enable=True,
                              dry_run=False):
        """Given a VirtualService instance, add it to this LoadMaster

        :param service: The VirtualService instance to clone
        :param ip: The new IP address of the virtual service
        :param port: The new port of the virtual service
        :param protocol: The new protocol of the virtual service
        :param enable: Enable the VirtualService
        :param dry_run: Don't save the VirtualSerivce immediately
        :return: The altered VirtualService tied to the this LoadMaster
        """
        if not isinstance(service, VirtualService):
            raise NotVirtualServiceInstanceError()
        service.endpoint = self.endpoint
        service.ip_address = self.ip_address
        service.cert = self.cert
        service.vs = ip
        service.port = port
        service.prot = protocol
        service.enable = get_api_bool_string(enable)
        service.index = None
        if not dry_run:
            service.save()
        return service

    def create_virtual_service(self, ip, port=80, protocol="tcp"):
        """VirtualService factory with pre-configured LoadMaster connection."""
        vs = VirtualService(self.access_info, ip, port, protocol)
        return vs

    def get_virtual_services(self):
        response = self._get("/listvs")
        data = get_data(response)
        virtual_services = []
        # if there is no VS key, build_virtual_services will fail with a
        # ValidationError, which is the best we can do for now
        # (without changing the upstream code and raising an exception earlier,
        # possibly retrying)
        services = data.get('VS', [])
        services = cast_to_list(services)
        for service in services:
            master_vs_id = int(service.get('MasterVSID', 0))
            if master_vs_id != 0:
                for vs in services:
                    if int(vs.get("Index", 0)) == master_vs_id:
                        virt_serv = self.build_virtual_service(service, vs)
            else:
                virt_serv = self.build_virtual_service(service, response)
            virtual_services.append(virt_serv)
        return virtual_services

    def get_virtual_service(self, index=None, address=None, port=None,
                            protocol=None):
        if index is None:
            validate_ip(address)
            validate_port(port)
            validate_protocol(protocol)
            service_id = {"vs": address, "port": port, "prot": protocol}
        else:
            service_id = {"vs": index}
        response = self._get("/showvs", service_id)
        service = get_data(response)
        # again line below will fail with ValidationError if empty response
        virt_serv = self.build_virtual_service(service)
        return virt_serv

    def get_all_objects(self):
        # x variables are the object while x_data is the OrderedDict
        virtual_services = []
        response = self._get("/listvs")
        data = get_data(response)
        virtual_services_data = data.get('VS', [])
        virtual_services_data = cast_to_list(virtual_services_data)

        # create vs and rs objects at this point
        # loop through all vss and attach matching real server objects
        for service_data in virtual_services_data:
            master_vs_id = int(service_data.get('MasterVSID', 0))
            if master_vs_id != 0:
                for vs in virtual_services_data:
                    if int(vs.get("Index", 0)) == master_vs_id:
                        virt_serv = self.build_virtual_service(service_data,
                                                               vs)
            else:
                virt_serv = self.build_virtual_service(service_data, response)
            real_servers = cast_to_list(service_data.get("Rs", []))
            for server_data in real_servers:
                rs = virt_serv.build_real_server(server_data)
                virt_serv.real_servers.append(rs)
            virtual_services.append(virt_serv)
        # replace subvs's with vs's that have RSs in them.
        for vs in virtual_services:
            for subvs in vs.subvs_entries:
                for top_level_vs in virtual_services:
                    if subvs.index == top_level_vs.index:
                        subvs.real_servers = top_level_vs.real_servers

        return virtual_services

    def build_virtual_service(self, service, response=None):
        """Create a VirtualService instance with populated with API parameters

        This does not include potentially attached real servers
        :param service: OrderedDict populated with virtual service data
        :param response: Optional response of a listvs call. This acts as a
        cache, if you want to create a lot of VirtualService
        objects in a row, such as with looping, you can call
        listvs and pass the response in each time and this
        will nullify the extra listvs calls.
        :return: VirtualService object with populated attributes
        """
        is_sub_vs = True if int(service.get('MasterVSID', 0)) != 0 else False
        if is_sub_vs:
            # `response` needs to be a dict in here
            # Add lb properties to the sub vs
            if response is None:
                response = self._get("/showvs",
                                     {"vs": service.get('MasterVSID')})
                parent_vs_data = get_data(response)
            else:
                parent_vs_data = response
            subvs_lb_props = get_sub_vs_list_from_data(parent_vs_data)[1]
            virt_serv = VirtualService(self.access_info, service.get('Index'),
                                       is_sub_vs=True)
            virt_serv.subvs_data = subvs_lb_props[service.get('Index')]
            virt_serv.subvs_data['parentvs'] = service.get('MasterVSID')
        else:
            # `response` needs to be a raw xml output here
            # Add any sub VSs to the top level VS
            if response is None:
                response = self._get("/listvs")
            data = get_data(response)
            virt_serv = VirtualService(self.access_info,
                                       service.get('VSAddress'),
                                       service.get('VSPort'),
                                       service.get('Protocol'),
                                       is_sub_vs=False)
            virt_serv.subvs_entries = []
            services = get_dict_entry_as_list("VS", data)
            this_vs_index = service.get('Index')
            for vs in services:
                # add subvs to parent vs
                if vs['MasterVSID'] == this_vs_index:
                    subvs = VirtualService(self.access_info, vs['Index'], is_sub_vs=True)
                    subvs.populate_default_attributes(vs)
                    subvs_api_entries = service.get("SubVS", [])
                    subvs_api_entries = cast_to_list(subvs_api_entries)
                    for subvs_api in subvs_api_entries:
                        # add the "Rs" part of the subvs to the subvs instance
                        if subvs_api["VSIndex"] == subvs.index:
                            subvs.subvs_data = subvs_api
                            # Have to add a parentvs hook to make life easy
                            subvs.subvs_data['parentvs'] = this_vs_index
                    virt_serv.subvs_entries.append(subvs)
        virt_serv.populate_default_attributes(service)
        return virt_serv

    def set_parameter(self, parameter, value):
        """assign the value to the given loadmaster parameter

        :param parameter: a valid LoadMaster parameter.
        :type parameter: str.
        :param value: the value to be assigned
        :type value: str.
        :raises: LoadMasterParameterError
        """
        parameters = {
            'param': parameter,
            'value': value,
        }
        response = self._get('/set', parameters)
        if not is_successful(response):
            raise LoadMasterParameterError(self, parameters)

    def get_parameter(self, parameter):
        """get the value of the given LoadMaster parameter

        :param parameter: a valid LoadMaster parameter.
        :type parameter: str.
        :return: str -- the parameter value
        """
        parameters = {
            'param': parameter,
        }
        response = self._get('/get', parameters)
        value = get_data_field(response, parameter)
        if isinstance(value, dict):
            # This hack converts possible HTML to an awful one string
            # disaster instead of returning parsed html as an OrderedDict.
            value = "".join("{!s}={!r}".format(key, val) for (key, val) in
                            sorted(value.items()))
        if parameter == "version":
            self.version = ".".join(value.split("."[:3]))
        return value

    def get_all_parameters(self):
        """ Return all parameters as a dict with lowercase keys

        :return: A dict of all the parameters, with the keys lowercased
        """
        response = self._get('/getall')
        data = get_data(response)
        return dict((k.lower(), v) for k, v in data.items())

    def enable_api(self):
        """enable LoadMaster API"""
        # Can't use the HttpClient methods for this as the
        # endpoint is different when attempting to enable the API.
        try:
            if self.cert:
                url = ("https://{ip}:{port}/progs/doconfig/enableapi/set/yes".
                       format(ip=self.ip_address, port=self.port))
                resp = self._tls_session.get(url, verify=False, timeout=1,
                                             cert=self.cert)
            else:
                url = ("https://{user}:{pw}@{ip}:{port}/progs/doconfig/"
                       "enableapi/set/yes").format(user=self.username,
                                                   pw=self.password,
                                                   ip=self.ip_address,
                                                   port=self.port)
                resp = self._tls_session.get(url, verify=False, timeout=1)
            self._tls_session.close()
            resp.raise_for_status()
            return True
        except exceptions.RequestException:
            return False

    def stats(self):
        response = self._get('/stats')
        return send_response(response)

    def update_firmware(self, file):
        response = self._post('/installpatch', file)
        self.version = None
        return is_successful(response)

    def restore_firmware(self):
        response = self._get("/restorepatch")
        self.version = None
        return is_successful(response)

    def shutdown(self):
        response = self._get('/shutdown')
        return is_successful(response)

    def reboot(self):
        response = self._get('/reboot')
        return is_successful(response)

    def get_sdn_controller(self):
        response = self._get('/getsdncontroller')
        return send_response(response)

    def get_license_info(self):
        try:
            response = self._get('360/licenseinfo')
            return send_response(response)

        except KempTechApiException:
            raise CommandNotAvailableException(
                self, '/access360/licenseinfo')

    def list_addons(self):
        response = self._get('/listaddon')
        return send_response(response)

    def upload_template(self, file):
        response = self._post('/uploadtemplate', file)
        return send_response(response)

    def list_templates(self):
        response = self._get('/listtemplates')
        return send_response(response)

    def delete_template(self, template_name):
        params = {'name': template_name}
        response = self._get('/deltemplate', parameters=params)
        return send_response(response)

    def apply_template(self, virtual_ip, port, protocol, template_name):
        params = {
            'vs': virtual_ip,
            'port': port,
            'prot': protocol,
            'name': template_name,
        }
        response = self._get('/addvs', parameters=params)
        return send_response(response)

    def get_sdn_info(self):
        response = self._get('/sdninfo')
        return send_response(response)

    def restore_backup(self, backup_type, file):
        # 1 LoadMaster Base Configuration
        # 2 Virtual Service Configuration
        # 3 GEO Configuration
        if backup_type not in [1, 2, 3]:
            backup_type = 2
        params = {"type": backup_type}
        response = self._post('/restore', file=file,
                              parameters=params)
        return send_response(response)

    def backup(self, location='backups'):
        if not os.path.exists(location):
            os.makedirs(location)
        file_name = os.path.join(location, "{}_{}.backup".format(
            self.ip_address, time.strftime("%Y-%m-%d_%H:%M:%S")))

        with open(file_name, 'wb') as file:
            cmd = self._get_curl_command_list('backup')
            subprocess.call(cmd, stdout=file)
            file.seek(0, 2)
            if file.tell() == 0:
                raise BackupFailed(self.ip_address)
        return file_name

    def alsi_license(self, kemp_id, password):
        params = {
            "kemp_id": kemp_id,
            "password": password,
        }
        response = self._get('/alsilicense', parameters=params)
        return send_response(response)

    def set_initial_password(self, password):
        params = {"passwd": password}
        response = self._get('/set_initial_password', parameters=params)
        return send_response(response)

    def kill_asl_instance(self):
        response = self._get('/killaslinstance')
        return send_response(response)

    def show_interface(self, interface_id=0):
        if not isinstance(interface_id, int):
            raise ValidationError('"interface_id" must be an integer')
        response = self._get('/showiface', {"interface": interface_id})
        data = get_data(response)
        interface = data["Interface"]
        if interface["IPAddress"] is not None:
            # Address/cidr is set in this case and can safely be split
            address_cidr_split = interface["IPAddress"].split("/")
            interface["IPAddress"] = address_cidr_split[0]
            interface["cidr"] = address_cidr_split[1]
        return interface

    def add_local_user(self, user, password=None, radius=False):
        params = {
            'user': user,
            'radius': get_api_bool_string(radius),
        }
        if password is None:
            params['nopass'] = 'y'
        else:
            params['password'] = password

        try:
            response = self._get('/useraddlocal', params)
        except KempTechApiException as e:
            if str(e) == "User already exists.":
                raise UserAlreadyExistsException(user, self.ip_address)
            else:
                raise
        return send_response(response)

    def delete_local_user(self, user):
        params = {'user': user}
        response = self._get('/userdellocal', params)
        return send_response(response)

    def set_user_perms(self, user, perms=None):
        perms = [] if perms is None else perms
        perms = cast_to_list(perms)
        params = {
            'user': user,
            'perms': ",".join([perm for perm in perms]),
        }
        response = self._get('/usersetperms', params)
        return send_response(response)

    def new_user_cert(self, user):
        params = {'user': user}
        response = self._get('/usernewcert', params)
        return send_response(response)

    def download_user_cert(self, user, location=os.curdir):
        file_name = os.path.join(location, "{}.cert".format(user))

        with open(file_name, 'wb') as file:
            cmd = self._get_curl_command_list('userdownloadcert?user={}'
                                              .format(user))
            subprocess.call(cmd, stdout=file)
            file.seek(0, 2)
            if file.tell() == 0:
                raise DownloadUserCertFailed(self.ip_address)
        return file_name


class KempBaseObjectModel(object):
    # blacklist attributes that shouldn't be pushed to the loadmaster.
    _API_IGNORE = (
        "ip_address", "endpoint", "rsindex", "vsindex", "index", "status",
        "subvs_data", "subvs_entries", "real_servers", "cert",
        "checkuse1_1", "mastervsid"
    )

    def __repr__(self):
        return '{} {}'.format(self.__class__.__name__, self.to_dict())

    def to_api_dict(self):
        """returns API related attributes as a dict

        Ignores attributes listed in _api_ignore and also attributes
        beginning with an underscore (_). Also ignore values of None"""
        api_dict = {}
        for key, value in self.__dict__.items():
            if (key in self._API_IGNORE or key.startswith("_") or
                    value is None):
                continue
            api_dict[key] = value
        return api_dict

    def to_dict(self):
        """returns attributes whose values are not None or whose name starts
        with _ as a dict"""
        api_dict = {}
        for key, value in self.__dict__.items():
            if key.startswith("_") or value is None:
                continue
            api_dict[key] = value
        return api_dict


class VirtualService(HttpClient, KempBaseObjectModel):

    def __init__(self, loadmaster_info, ip_or_index, port=80, prot="tcp",
                 is_sub_vs=False):
        """Construct VirtualService object.

        :param loadmaster_info: The loadmaster dict with the endpoint params.
        :param ip_or_index: IP or index of the VS. When creating a subvs you
               must pass the index and set the is_sub_vs flag to true in order
               for createsubvs to behave correctly. The index will be
               overwritten with the index of the newly created subvs on save().
        :param port: Port of the virtual service.
        :param prot: Protocol of the virtual service.
        :param is_sub_vs: Whether or not it is a subvs, mark this as true and
               pass the parent VS index as the ip_or_index parameter.
        """
        self.index = None  # to avoid AttributeErrors later
        self._is_sub_vs = is_sub_vs
        self.subvs_data = None
        self.subvs_entries = []
        self.real_servers = []
        if not is_sub_vs:
            # Skip validation when it is a subvs as they do not have ip/port
            self.vs = ip_or_index
            self.port = port
            self.prot = prot
            validate_ip(ip_or_index)
            validate_port(port)
            validate_protocol(prot)
        else:
            self.index = ip_or_index
            self.vs = ip_or_index

        self.cert = loadmaster_info.get("cert")
        try:
            self.endpoint = loadmaster_info["endpoint"]
        except KeyError:
            raise VirtualServiceMissingLoadmasterInfo("endpoint")
        try:
            self.ip_address = loadmaster_info["ip_address"]
        except KeyError:
            raise VirtualServiceMissingLoadmasterInfo("ip_address")
        super(VirtualService, self).__init__(cert=self.cert)

    def __str__(self):
        try:
            if int(self.vs):
                return 'Sub Virtual Service {} on LoadMaster {}'.format(
                    self.vs, self.ip_address)
        except ValueError:
            return 'Virtual Service {} {}:{} on LoadMaster {}'.format(
                self.prot.upper(), self.vs, self.port, self.ip_address)

    def _get_base_parameters(self):
        """Returns the bare minimum VS parameters. IP, port and protocol"""
        if self.index is None:
            return {"vs": self.vs, "port": self.port, "prot": self.prot}
        else:
            return {"vs": self.index}

    def _subvs_to_dict(self):
        return {
            "vs": self.subvs_data['parentvs'],
            "rs": "!{}".format(self.subvs_data['RsIndex']),
            "name": self.subvs_data['Name'],
            "forward": self.subvs_data['Forward'],
            "weight": self.subvs_data['Weight'],
            "limit": self.subvs_data['Limit'],
            "critical": self.subvs_data['Critical'],
            "enable": self.subvs_data['Enable'],
        }

    @property
    def access_info(self):
        if self.index is None:
            return {
                "endpoint": self.endpoint,
                "cert": self.cert,
                "ip_address": self.ip_address,
                "vs": self.vs,
                "port": self.port,
                "prot": self.prot,
            }
        else:
            return {
                "endpoint": self.endpoint,
                "cert": self.cert,
                "ip_address": self.ip_address,
                "vs": self.index,
            }

    @property
    def checkuse1_1(self):
        """This property exists because . can not be in a variable name"""
        return self.__dict__.get('checkuse1.1', None)

    @checkuse1_1.setter
    def checkuse1_1(self, value):
        self.__dict__['checkuse1.1'] = value

    def save(self, update=False):
        """ Send API request to add or update the VirtualService

        For saving virtual, or sub virtual services to the LoadMaster.
        When the service is a sub virtual service, it will also update the sub
        virtual services 'real server' (weight, conns, etc.) parameters as well
        :param update: If True, it will perform an update instead of create
        """
        try:
            if not update:
                if self._is_sub_vs:
                    # Hell, thy name be subvs
                    response = self._get("/showvs",
                                         self._get_base_parameters())
                    data = get_data(response)
                    existing_subvs_entries = get_sub_vs_list_from_data(data)[0]
                    params = self._get_base_parameters()
                    params["createsubvs"] = ""
                    response = self._get("/modvs", params)
                    data = get_data(response)
                    new_subvs_entries, subvs_data = \
                        get_sub_vs_list_from_data(data)
                    s = set(existing_subvs_entries)
                    created_subvs_id = [x
                                        for x in new_subvs_entries
                                        if x not in s]
                    newly_created_vs_params = {"vs": created_subvs_id}
                    self.subvs_data = subvs_data[created_subvs_id[0]]
                    self.subvs_data['parentvs'] = self.vs
                    response = self._get("/showvs", newly_created_vs_params)
                else:
                    response = self._get("/addvs", self.to_api_dict())
            else:
                if self._is_sub_vs:
                    # Update the underlying "Rs" part of the subvs as well
                    self._get("/modrs", self._subvs_to_dict())
                    # Remove enable from the modvs request
                    self.enable = None
                response = self._get("/modvs", self.to_api_dict())
        except KempTechApiException:
            raise

        if is_successful(response):
            vs_data = get_data(response)
            self.populate_default_attributes(vs_data)
        else:
            raise KempTechApiException(get_error_msg(response))

    def update(self):
        self.save(update=True)

    def delete(self):
        response = self._get("/delvs", self._get_base_parameters())
        return send_response(response)

    def populate_default_attributes(self, service):
        """Populate VirtualService instance with standard defaults"""
        self.status = service.get('Status', None)
        self.index = service.get('Index', None)
        self.enable = service.get('Enable', None)
        self.forcel7 = service.get('ForceL7', None)
        self.vstype = service.get('VStype', None)
        self.schedule = service.get('Schedule', None)
        self.nickname = service.get('NickName', None)
        self.altaddress = service.get('AltAddress', None)
        self.transparent = service.get('Transparent', None)
        self.useforsnat = service.get('UseforSnat', None)
        self.persist = service.get('Persist', None)
        self.persisttimeout = service.get('PersistTimeout', None)
        self.cookie = service.get('Cookie', None)
        self.extraports = service.get('ExtraPorts', None)
        self.qos = service.get('QoS', None)
        self.idletime = service.get('Idletime', None)
        self.mastervsid = service.get('MasterVSID', None)

        self.alertthreshold = service.get('AlertThreshold', None)
        self.querytag = service.get('QueryTag', None)
        self.serverinit = service.get('ServerInit', None)
        self.addvia = service.get('AddVia', None)
        self.subnetoriginating = service.get('SubnetOriginating', None)
        self.localbindaddrs = service.get('LocalBindAddrs', None)
        self.defaultgw = service.get('DefaultGW', None)
        #self.followvsid = falsey_to_none(int(service.get('FollowVSID', 0)))
        self.standbyaddr = service.get('StandbyAddr', None)
        self.standbyport = service.get('StandbyPort', None)
        self.errorcode = service.get('ErrorCode', None)
        self.errorurl = service.get('ErrorUrl', None)
        self.errorpage = service.get('ErrorPage', None)

        self.intercept = service.get('Intercept', None)
        self.multiconnect = service.get('MultiConnect', None)
        self.verify = service.get('Verify', None)
        self.espenabled = service.get('EspEnabled', None)
        self.compress = service.get('Compress', None)
        self.cache = service.get('Cache', None)
        self.cachepercent = service.get('CachePercent', None)

        # SSL Acceleration
        sslrewrite = {
            "0": None,
            "1": "http",
            "2": "https",
        }
        self.sslacceleration = service.get('SSLAcceleration', None)
        if self.sslacceleration:
            self.tlstype = service.get('TlsType', None)
            self.cipherset = service.get('CipherSet', None)
            self.ciphers = service.get('Ciphers', None)
        self.sslreencrypt = service.get('SSLReencrypt', None)
        self.sslreverse = service.get('SSLReverse', None)
        try:
            self.sslrewrite = sslrewrite[service.get('SSLRewrite', "0")]
        except KeyError:
            self.sslrewrite = None
        self.starttlsmode = service.get('StartTLSMode', None)
        self.clientcert = service.get('ClientCert', None)
        self.ocspverify = service.get('OCSPVerify', None)
        # self.certfile = service.get('CertFile', None)
        self.reversesnihostname = service.get('ReverseSNIHostname', None)

        # Real servers section
        self.checktype = service.get('CheckType', None)
        self.checkhost = service.get('CheckHost', None)
        self.checkpattern = service.get('CheckPattern', None)
        self.checkurl = service.get('CheckUrl', None)
        self.checkcodes = service.get('CheckCodes', None)
        self.checkheaders = service.get('CheckHeaders', None)
        self.matchlen = service.get('MatchLen', None)
        self.checkuse1_1 = service.get('CheckUse1.1', None)
        self.checkport = falsey_to_none(int(service.get('CheckPort', 0)))
        self.checkuseget = service.get('CheckUseGet', None)
        self.extrahdrkey = service.get('ExtraHdrKey', None)
        self.extrahdrvalue = service.get('ExtraHdrValue', None)
        self.checkpostdata = service.get('CheckPostData', None)
        self.rsruleprecedence = service.get('RSRulePrecedence', None)
        self.rsruleprecedencepos = service.get('RSRulePrecedencePos', None)
        self.enhancedhealthchecks = service.get('EnhancedHealthChecks', None)
        self.rsminimum = service.get('RsMinimum', None)

    def create_sub_virtual_service(self):
        """VirtualService factory with pre-configured LoadMaster connection

        When creating a virtual service that is a sub virtual service you must
        pass the parent index to the constructor and mark the is_sub_vs flag
        as true. This will allow the save() method on the newly created subvs
        instance to be able to create a subvs against the parent vs. The index
        attribute will then be overwritten on save with the subvs's index.
        """
        if self._is_sub_vs:
            raise SubVsCannotCreateSubVs()
        return VirtualService(self.access_info, self.index, is_sub_vs=True)

    def create_real_server(self, ip, port=80):
        """RealServer factory with pre-configured LoadMaster connection."""
        return RealServer(self.access_info, ip, port)

    def get_real_server(self, real_server_address=None, real_server_port=None):

        validate_ip(real_server_address)
        validate_port(real_server_port)

        if self.index is None:
            server_id = {
                "vs": self.vs,
                "port": self.port,
                "prot": self.prot,
                "rs": real_server_address,
                "rsport": real_server_port,
            }
        else:
            server_id = {
                "vs": self.index,
                "rs": real_server_address,
                "rsport": real_server_port,
            }
        response = self._get("/showrs", server_id)
        response_data = get_data(response)
        server = response_data.get("Rs", {})
        # if there is no Rs key, the following will fail with a ValidationError
        # which is the best we can do for now
        real_server = self.build_real_server(server)
        return real_server

    def get_real_servers(self):
        response = self._get("/showvs", self._get_base_parameters())
        data = get_data(response)
        real_servers = []
        servers = data.get('Rs', [])
        servers = cast_to_list(servers)
        for server in servers:
            real_server = self.build_real_server(server)
            real_servers.append(real_server)
        return real_servers

    def build_real_server(self, server):
        if "Addr" not in server:
            raise ValidationError('"Addr" key not present {}'.format(server))
        if "Port" not in server:
            raise ValidationError('"Port" key not present {}'.format(server))
        real_server = RealServer(self.access_info, server['Addr'],
                                 server['Port'])
        real_server.populate_default_attributes(server)
        return real_server


class RealServer(HttpClient, KempBaseObjectModel):

    def __init__(self, loadmaster_virt_service_info, ip, port=80):
        self.rsindex = None
        self.rs = ip
        validate_ip(ip)
        self.rsport = port
        validate_port(port)
        self.cert = loadmaster_virt_service_info.get("cert")
        try:
            self.vs = loadmaster_virt_service_info["vs"]
        except KeyError:
            raise RealServerMissingVirtualServiceInfo("vs")

        self.port = loadmaster_virt_service_info.get("port", None)
        self.prot = loadmaster_virt_service_info.get("prot", None)
        try:
            self.endpoint = loadmaster_virt_service_info["endpoint"]
        except KeyError:
            raise RealServerMissingLoadmasterInfo("endpoint")

        try:
            self.ip_address = loadmaster_virt_service_info["ip_address"]
        except KeyError:
            raise RealServerMissingLoadmasterInfo("ip_address")

        super(RealServer, self).__init__(cert=self.cert)

    def __str__(self):
        return 'Real Server {} on {}'.format(self.rs, self.vs)

    def _get_base_parameters(self):
        """Returns the bare minimum VS parameters. IP, port and protocol"""
        # Can't use the rsindex until vsindex is correct on a showrs call
        return {
            "vs": self.vs,
            "port": self.port,
            "prot": self.prot,
            "rs": self.rs,
            "rsport": self.rsport,
        }

    def save(self, update=False):
        if not update:
            response = self._get("/addrs", self.to_api_dict())
        else:
            response = self._get("/modrs", self.to_api_dict())
        if is_successful(response):
            response = self._get("/showrs", self._get_base_parameters())
            data = get_data(response)
            rs_data = data.get("Rs", {})
            self.populate_default_attributes(rs_data)
        else:
            raise KempTechApiException(get_error_msg(response))

    def delete(self):
        response = self._get("/delrs", self._get_base_parameters())
        return send_response(response)

    def populate_default_attributes(self, rs_data):
        self.rsindex = rs_data.get('RsIndex', None)
        self.vsindex = rs_data.get('VSIndex', None)
        self.status = rs_data.get('Status', None)
        self.forward = rs_data.get('Forward', None)
        self.enable = rs_data.get('Enable', None)
        self.weight = rs_data.get('Weight', None)
        self.limit = rs_data.get('Limit', None)
        self.critical = rs_data.get('Critical', None)
