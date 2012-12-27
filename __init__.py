import ConfigParser
import os
import requests
import unittest2 as unittest
import shutil


class CDMICapabilitiesTestCase(unittest.TestCase):
    """Class that inherits Python's unittest.TestCase Attributes
       into self.cdmi.

    Attributes:
        cdmi: instance of a CDMIObject
    """

    def setUp(self):
        self.cdmi = CDMI()


class CDMI(object):
    """Class to represent a connection to a CDMI Server.

        Attributes(type):

            adminpassword(string):
                Administrator password for the CDMI server

            adminuser(string):
                User name for an administrator user of the CDMI server

            capabilities_object_capabilties(dictionary):
                Cababilities object capabiltites of the CDMI server

            capabilities_uri(string):
                Capabilities URI of the cdmi server

            config(ConfigParser):
                ConfigParser object that cdmi.conf is parsed into

            configFile(string):
                Path to the configuration file (cdmi.conf)

            container_object_capabilities(dictionary):
                Container object capabilities of CDMI server

            data_object_capabilities(dictionary):
                Data object capabilities of the CDMI server

            data_system_capabilities(dictionary):
                Data system capabilities of the CDMI server

            domain_object_capabilities(dictionary):
                Domain object capabilities of the CDMI server

            endpoint(string):
                Relative Path to the CDMI server's endpoint

            host(string):
                Host for the CDMI server

            queue_object_capabilities(dictionary):
                Queue object capabilites of the CDMI Server

            secure(boolean):
                Connection scheme (HTTP or HTTPS)

            storage_system_capabilities(dictionary):
                Storage system capabilties of the CDMI server

            system_wide_capabilities(dictionary):
                Dictionary of the system wide capabilities

            verisons(string):
                Comma seperated list of the CDMI Versions Supported by the 
                server
    """

    def __init__(self):
        """Initialize the CDMI Class

            Args: self

            Returns: None

            Raises: 

        """

        #Import the configuration from the config file
        config = ConfigParser.ConfigParser()
        configFile = 'cdmi.conf'
        config.read(configFile)

        self.adminpassword = config.get('CDMI', 'adminpassword')
        self.capabilities_uri = config.get('CDMI', 'capabilities_uri')
        self.endpoint = config.get('CDMI', 'endpoint')
        self.host = config.get('CDMI', 'host')
        self.secure = config.get('CDMI', 'secure')
        self.version = config.get('CDMI', 'versions')

        #System Wide Capabilities
        self.system_wide_capabilities = {
            "cdmi_domains": "False",
            "cdmi_export_cifs": "False",
            "cdmi_dataobjects": "False",
            "cdmi_export_iscsi": "False",
            "cdmi_export_nfs": "False",
            "cdmi_export_occi_iscsi": "False",
            "cdmi_export_webdav": "False",
            "cdmi_metadata_maxitems": "False",
            "cdmi_metadata_maxsize": "False",
            "cdmi_metadata_maxtotalsize": "False",
            "cdmi_notification": "False",
            "cdmi_logging": "False",
            "cdmi_query": "False",
            "cdmi_query_regex": "False",
            "cdmi_query_tags": "False",
            "cdmi_query_value": "False",
            "cdmi_queues": "False",
            "cdmi_security_access_control": "False",
            "cdmi_security_audit": "False",
            "cdmi_security_data_integrity": "False",
            "cdmi_security_encryption": "False",
            "cdmi_security_immutability": "False",
            "cdmi_security_sanitization": "False",
            "cdmi_serialization_json": "False",
            "cdmi_snapshots": "False",
            "cdmi_references": "False",
            "cdmi_object_move_from_local": "False",
            "cdmi_object_move_from_remote": "False",
            "cdmi_object_move_from_ID": "False",
            "cdmi_object_move_to_ID": "False",
            "cdmi_object_copy_from_local": "False",
            "cdmi_object_copy_from_remote": "False",
            "cdmi_object_access_by_ID": "False",
            "cdmi_post_dataobject_by_ID": "False",
            "cdmi_post_queue_by_ID": "False",
            "cdmi_deserialize_dataobject_by_ID": "False",
            "cdmi_deserialize_queue_by_ID": "False",
            "cdmi_serialize_dataobject_to_ID": "False",
            "cdmi_serialize_domain_to_ID": "False",
            "cdmi_serialize_container_to_ID": "False",
            "cdmi_serialize_queue_to_ID": "False",
            "cdmi_copy_dataobject_by_ID": "False",
            "cdmi_copy_queue_by_ID": "False",
            "cdmi_create_reference_by_ID": "False"
        }

        #Storage System Capabilities
        storage_system_capabilities = {
            "cdmi_acl": "False",
            "cdmi_size": "False",
            "cdmi_ctime": "False",
            "cdmi_atime": "False",
            "cdmi_mtime": "False",
            "cdmi_acount": "False",
            "cdmi_mcount": "False"
        }

        #Data System Capabilities
        data_system_capabilities = {
            "cdmi_assignedsize": "False",
            "cdmi_data_redundancy": "False",
            "cdmi_data_dispersion": "False",
            "cdmi_data_retention": "False",
            "cdmi_data_autodelete": "False",
            "cdmi_data_holds": "False",
            "cdmi_encryption": "False",
            "cdmi_geographic_placement": "False",
            "cdmi_immediate_redundancy": "False",
            "cdmi_infrastructure_redundancy": "False",
            "cdmi_latency": "False",
            "cdmi_RPO": "False",
            "cdmi_RTO": "False",
            "cdmi_sanitization_method": "False",
            "cdmi_throughput": "False",
            "cdmi_value_hash": "False"
        }

        #Data Object Metadata Capabilities
        self.data_object_capabilities = {
            "cdmi_list_children": "False",
            "cdmi_list_children_range": "False",
            "cdmi_read_metadata": "False",
            "cdmi_modify_metadata": "False",
            "cdmi_modify_deserialize_container": "False",
            "cdmi_snapshot": "False",
            "cdmi_serialize_dataobject": "False",
            "cdmi_serialize_container": "False",
            "cdmi_serialize_queue": "False",
            "cdmi_serialize_domain": "False",
            "cdmi_deserialize_container": "False",
            "cdmi_deserialize_queue": "False",
            "cdmi_deserialize_dataobject": "False",
            "cdmi_create_dataobject": "False",
            "cdmi_post_dataobject": "False",
            "cdmi_post_queue": "False",
            "cdmi_create_container": "False",
            "cdmi_create_queue": "False",
            "cdmi_create_reference": "False",
            "cdmi_export_container_cifs": "False",
            "cdmi_export_container_nfs": "False",
            "cdmi_export_container_iscsi": "False",
            "cdmi_export_container_occi": "False",
            "cdmi_export_container_webdav": "False",
            "cdmi_delete_container": "False",
            "cdmi_move_container": "False",
            "cdmi_copy_container": "False",
            "cdmi_move_dataobject": "False",
            "cdmi_copy_dataobject": "False",
        }

        self.data_object_capabilities.update(data_system_capabilities)
        self.data_object_capabilities.update(storage_system_capabilities)

        self.container_object_capabilities = {
            "cdmi_list_children": "False",
            "cdmi_list_children_range": "False",
            "cdmi_read_metadata": "False",
            "cdmi_modify_metadata": "False",
            "cdmi_modify_deserialize_container": "False",
            "cdmi_snapshot": "False",
            "cdmi_serialize_dataobject": "False",
            "cdmi_serialize_container": "False",
            "cdmi_serialize_queue": "False",
            "cdmi_serialize_domain": "False",
            "cdmi_deserialize_container": "False",
            "cdmi_deserialize_queue": "False",
            "cdmi_deserialize_dataobject": "False",
            "cdmi_create_dataobject": "False",
            "cdmi_post_dataobject": "False",
            "cdmi_post_queue": "False",
            "cdmi_create_container": "False",
            "cdmi_create_queue": "False",
            "cdmi_create_reference": "False",
            "cdmi_export_container_cifs": "False",
            "cdmi_export_container_nfs": "False",
            "cdmi_export_container_iscsi": "False",
            "cdmi_export_container_occi": "False",
            "cdmi_export_container_webdav": "False",
            "cdmi_delete_container": "False",
            "cdmi_move_container": "False",
            "cdmi_copy_container": "False",
            "cdmi_move_dataobject": "False",
            "cdmi_copy_dataobject": "False",
        }

        self.container_object_capabilities.update(data_system_capabilities)
        self.container_object_capabilities.update(storage_system_capabilities)

        self.domain_object_capabilities = {
            "cdmi_list_children": "False",
            "cdmi_list_children_range": "False",
            "cdmi_read_metadata": "False",
            "cdmi_modify_metadata": "False",
            "cdmi_modify_deserialize_container": "False",
            "cdmi_snapshot": "False",
            "cdmi_serialize_dataobject": "False",
            "cdmi_serialize_container": "False",
            "cdmi_serialize_queue": "False",
            "cdmi_serialize_domain": "False",
            "cdmi_deserialize_container": "False",
            "cdmi_deserialize_queue": "False",
            "cdmi_deserialize_dataobject": "False",
            "cdmi_create_dataobject": "False",
            "cdmi_post_dataobject": "False",
            "cdmi_post_queue": "False",
            "cdmi_create_container": "False",
            "cdmi_create_queue": "False",
            "cdmi_create_reference": "False",
            "cdmi_export_container_cifs": "False",
            "cdmi_export_container_nfs": "False",
            "cdmi_export_container_iscsi": "False",
            "cdmi_export_container_occi": "False",
            "cdmi_export_container_webdav": "False",
            "cdmi_delete_container": "False",
            "cdmi_move_container": "False",
            "cdmi_copy_container": "False",
            "cdmi_move_dataobject": "False",
            "cdmi_copy_dataobject": "False",
        }

        self.domain_object_capabilities.update(data_system_capabilities)
        self.domain_object_capabilities.update(storage_system_capabilities)

        self.capability_object_capabilities = {
            "cdmi_read_value": "False",
            "cdmi_read_metadata": "False",
            "cdmi_modify_value": "False",
            "cdmi_modify_metadata": "False",
            "cdmi_modify_deserialize_queue": "False",
            "cdmi_delete_queue": "False",
            "cdmi_move_queue": "False",
            "cdmi_copy_queue": "False",
            "cdmi_reference_queue": "False"
        }

        self.queue_object_capabilities = {
            "cdmi_read_value": "False",
            "cdmi_read_metadata": "False",
            "cdmi_modify_value": "False",
            "cdmi_modify_metadata": "False",
            "cdmi_modify_deserialize_queue": "False",
            "cdmi_delete_queue": "False",
            "cdmi_move_queue": "False",
            "cdmi_copy_queue": "False",
            "cdmi_reference_queue": "False"
        }

        self.queue_object_capabilities.update(data_system_capabilities)
        self.queue_object_capabilities.update(storage_system_capabilities)

    def build_url(self,
                  uri):

        if self.secure is True:
            scheme = 'http://'
        else:
            scheme = 'https://'

        url = scheme + self.host + uri

        return url

    def build_headers(self,
                      accept='*/*',
                      headers={},
                      content=None,
                      cdmi=True):

        if headers is None:
            headers = {}

        if accept != '*/*':
            headers['Accept'] = accept

        if content is not None:
            headers['Content-Type'] = content

        if cdmi is True:
            headers['X-CDMI-Specification-Version'] = self.version

        return headers

    def get(self,
            uri,
            accept=None,
            headers=None,
            user=None,
            password=None,
            cdmi=True):

        """Makes an HTTP GET Request to the CDMI Server.

            Args(type):

                self

                uri(string):
                    URI to perform the request to on the CDMI server

                accept(string):
                    Content Type to be accepted by the CDMI server

                headers(dictionary):
                    Additional headers to add to the request

                user(string):
                    User who makes the request (used by requests to build
                    the auth string)

                password(string):
                    Password for the user who makes the request (used by
                    requests to build the authorization string)

                cdmi(bool):
                    Specifies whether the request is a CDMI (True) or Non-CDMI(False)
                    request (Adds the CDMI header to the request)

            Returns:

                response(requests.Response()):
                    Response object from the CDMI server

            Raises:
                requests.HTTPError,
                requests.URLError,
                requests.ConnectionError

        """

        #Build the URL from the URI
        url = self.build_url(uri)

        #Build the headers for the request
        hdr = self.build_headers(headers=headers)

        #Determine the Auth Method to Make the request
        if user is None and \
                password is None:
            response = requests.get(url=url,
                                    headers=hdr,
                                    verify=False)

        elif user == self.adminuser and \
                password == self.adminpassword:

                    response = requests.get(url=url,
                                            headers=hdr,
                                            auth=(self.adminuser,
                                                  self.adminpassword),
                                            verify=False)

        else:
            response = requests.get(url=url,
                                    headers=hdr,
                                    auth=(self.user,
                                          self.password),
                                    verify=False)

            response.raise_for_status

        return response

    def discover_all_capabilities(self):

        #System Wide Capabilities
        capabilities = self.get(self.capabilities_uri)

        for key in self.system_wide_capabilities.keys():

            try:
                if capabilities.json.get('capabilities').get(key) == 'true':
                    self.system_wide_capabilities[key] = True
            except KeyError:
                pass

        #Container Capabilities
        capabilities = self.get(self.capabilities_uri + '/container')

        for key in self.container_object_capabilities.keys():

            try:
                if capabilities.json.get('capabilities').get(key) == 'true':
                    self.container_object_capabilities[key] = True
            except KeyError:
                pass

        #Data Capabilities
        capabilities = self.get(self.capabilities_uri + '/dataobject')

        for key in self.data_object_capabilities.keys():

            try:
                if capabilities.json.get('capabilities').get(key) == 'true':
                    self.data_object_capabilities[key] = True
            except KeyError:
                pass

        #Domain Object Capabilities
        capabilities = self.get(self.capabilities_uri + '/domain')

        for key in self.domain_object_capabilities.keys():

            try:
                if capabilities.json.get('capabilities').get(key) == 'true':
                    self.domain_object_capabilities[key] = True
            except KeyError:
                pass

        #Domain Object Capabilities
        capabilities = self.get(self.capabilities_uri + '/queue')

        for key in self.domain_object_capabilities.keys():

            try:
                if capabilities.json.get('capabilities').get(key) == 'true':
                    self.domain_object_capabilities[key] = True
            except KeyError:
                pass

    def generate_test_cases(self):

        for key in self.system_wide_capabilities.keys():

            #Copy the template to ./tests/system_wide_capabilities/<key>
            if not os.path.exists('./tests/system_wide_capabilities'):
                os.mkdir('./tests/system_wide_capabilities')

            shutil.copy('./templates/template.py',
                        './tests/system_wide_capabilities/%s.py' % key)

        for key in self.container_object_capabilities.keys():

            #Copy the template to ./tests/system_wide_capabilities/<key>
            if not os.path.exists('./tests/container_object_capabilities'):
                os.mkdir('./tests/container_object_capabilities')

            shutil.copy('./templates/template.py',
                        './tests/container_object_capabilities/%s.py' % key)

        for key in self.data_object_capabilities.keys():

            #Copy the template to ./tests/system_wide_capabilities/<key>
            if not os.path.exists('./tests/data_object_capabilities'):
                os.mkdir('./tests/data_object_capabilities')

            shutil.copy('./templates/template.py',
                        './tests/data_object_capabilities/%s.py' % key)

        for key in self.domain_object_capabilities.keys():

            #Copy the template to ./tests/system_wide_capabilities/<key>
            if not os.path.exists('./tests/domain_object_capabilities'):
                os.mkdir('./tests/domain_object_capabilities')

            shutil.copy('./templates/template.py',
                        './tests/domain_object_capabilities/%s.py' % key)

        for key in self.queue_object_capabilities.keys():

            #Copy the template to ./tests/system_wide_capabilities/<key>
            if not os.path.exists('./tests/queue_object_capabilities'):
                os.mkdir('./tests/queue_object_capabilities')

            shutil.copy('./templates/template.py',
                        './tests/queue_object_capabilities/%s.py' % key)

cdmi = CDMI()
cdmi.discover_all_capabilities()
cdmi.generate_test_cases()
