#  (c) Copyright 2015 Hewlett Packard Enterprise Development LP
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""
This checks the cinder.conf file to find errors in the configuration of 3PAR
arrays.

Requires python-3parclient: sudo pip install python-3parclient
Assumes the volume_driver is correctly set
"""

import logging
from six.moves import configparser
from cinderdiags import constant
from cinderdiags import hpe3par_testclient as testclient

logger = logging.getLogger(__name__)

try:
    from hpe3parclient import client as hpeclient
    from hpe3parclient import exceptions as hpe_exceptions
except ImportError:
    logger.error('python-3parclient package not found (pip install python-3parclient)')


class WSChecker(object):

    def __init__(self, client, conf, node, test=False,
                 include_system_info=False):
        """Tests web service api configurations in the cinder.conf file

        :param conf: location of cinder.conf
        :param node: cinder node the cinder.conf was copied from
        :param test: use testing client
        """
        self.conf = conf
        self.ssh_client = client
        self.node = node
        self.is_test = test
        self.include_system_info = include_system_info
        self.parser = configparser.ConfigParser()
        self.parser.read(self.conf)
        self.hpe3pars = []
        for section in self.parser.sections():
            if self.parser.has_option(section, 'volume_driver') \
                    and 'hpe_3par' in self.parser.get(section, 'volume_driver'):
                self.hpe3pars.append(section)

    def check_all(self):
        """Tests configuration settings for all 3par arrays

        :return: a list of dictionaries
        """
        all_tests = []
        for section_name in self.hpe3pars:
            all_tests.append(self.check_section(section_name))
        return all_tests

    def check_section(self, section_name):
        logger.info("hpe3par_wsapi_checks - check_section()")
        """Runs all WS configuration tests for a section

        :param section_name: from cinder.conf as [SECTION_NAME]
        :return: a dictionary - each property is pass/fail/unknown
        """
        tests = {
            "name": section_name,
            "url": "unknown",
            "credentials": "unknown",
            "cpg": "unknown",
            "iscsi": "unknown",
            "node": self.node,
            "driver": "unknown",
        }
        if self.include_system_info:
            tests["system_info"] = "unknown"
            tests['conf_items'] = "unknown"

        if section_name in self.hpe3pars:
            logger.info("Checking 3PAR options for node '%s' backend section "
                         "%s" % (self.node, section_name))

            if self.include_system_info:
                tests['conf_items'] = self.get_conf_items(section_name)

            tests["driver"] = self.has_driver(section_name)
            client = self.get_client(section_name, self.is_test)
            if client:
                logger.info("client: '%s'" % (client))
                tests["url"] = "pass"
                if self.cred_is_valid(section_name, client):
                    if self.include_system_info:
                        tests["system_info"] = self.get_system_info(section_name,
                                                                    client)
                    tests["credentials"] = "pass"
                    tests["cpg"] = self.cpg_is_valid(section_name, client)
                    if 'iscsi' in self.parser.get(section_name,
                                                  'volume_driver'):
                        tests["iscsi"] = self.iscsi_is_valid(section_name,
                                                             client)
                    client.logout()
                else:
                    tests["credentials"] = "fail"
            else:
                tests["url"] = "fail"
            if 'hpe_3par_fc' in self.parser.get(section_name, 'volume_driver'):
                tests["iscsi"] = "N/A"
            return tests
        else:
            return None

# Config testing methods check if option values are valid
    def get_client(self, section_name, test):
        logger.info("hpe3par_wsapi_checks - get_client()")
        """Tries to create a client and verifies the api url

        :return: The client if url is valid, None if invalid/missing
        """
        try:
            url = self.parser.get(section_name, 'hpe3par_api_url')
            logger.info("Attempting to connect to %s..." % url)
            if test:
                cl = testclient.HPE3ParClient(url)
            else:
                cl = hpeclient.HPE3ParClient(url)
            return cl
        except (hpe_exceptions.UnsupportedVersion, hpe_exceptions.HTTPBadRequest,
                TypeError) as e:
            logger.info("Failed to connect to hpe3par_api_url for node '%s' "
                        "backend section '%s' --- %s" % (self.node,
                                                         section_name, e))
            return None
        except configparser.NoOptionError:
            logger.info("No hpe3par_api_url provided for node '%s' backend "
                        "section '%s'" % (self.node, section_name))
            return None

    def cred_is_valid(self, section_name, client):
        logger.info("hpe3par_wsapi_checks - cred_is_valid()")
        """Tries to login to the client to verify credentials

        :return: True if credentials are valid, False if invalid/missing
        """
        logger.info("Use credentials %s -- %s: " %
                    (self.parser.get(section_name, 'hpe3par_username'),
                     self.parser.get(section_name, 'hpe3par_password')))
        try:
            client.login(self.parser.get(section_name, 'hpe3par_username'),
                         self.parser.get(section_name, 'hpe3par_password'))
            return True
        except (hpe_exceptions.HTTPForbidden,
                hpe_exceptions.HTTPUnauthorized):
            logger.info("Incorrect hpe3par_username or hpe3par_password "
                        "provided for node '%s' backend section '%s'" %
                        (self.node, section_name))
            return False
        except configparser.NoOptionError:
            logger.info("No hpe3par_username or hpe3par_password provided for "
                        "node '%s' backend section '%s'" % (self.node,
                                                            section_name))
            return False

    def cpg_is_valid(self, section_name, client):
        logger.info("hpe3par_wsapi_checks - cpg_is_valid()")
        """Tests to see if a cpg exists on the 3PAR array to verify cpg name

        :return: string
        """
        result = "pass"
        try:
            cpg_list = [x.strip() for x in
                        self.parser.get(section_name, 'hpe3par_cpg').split(',')]
            logger.info("Checking hpe3par_cpg option for node '%s' backend "
                         "section '%s'" % (self.node, section_name))
            for cpg in cpg_list:
                try:
                    logger.info("request client.getCPG(): '%s' " %
                                (cpg))
                    client.getCPG(cpg)
                except hpe_exceptions.HTTPNotFound:
                    logger.info("Node '%s' backend section '%s' hpe3par_cpg "
                                "contains an invalid CPG name: '%s'" %
                                (self.node, section_name, cpg))
                    result = "fail"
        except configparser.NoOptionError:
            logger.info("No hpe3par_cpg provided for node '%s' backend section "
                        "'%s'" %
                        (self.node, section_name))
            result = "fail"
        return result

    def iscsi_is_valid(self, section_name, client):
        logger.info("hpe3par_wsapi_checks - iscsi_is_valid()")
        """Gets the iSCSI target ports from the client, checks the iSCSI IPs.

        :return: string
        """
        valid_ips = []
        result = "pass"

        ip_list = self.get_iscsi_ips(section_name)
        if ip_list:
            logger.info("Checking iSCSI IP addresses for node '%s' backend "
                         "section '%s'" % (self.node, section_name))
            for port in client.getPorts()['members']:
                if (port['mode'] == client.PORT_MODE_TARGET and
                        port['linkState'] == client.PORT_STATE_READY and
                        port['protocol'] == client.PORT_PROTO_ISCSI):
                    valid_ips.append(port['IPAddr'])
                    logger.info("Checking iscsi IP port: '%s'" % (port['IPAddr']))
            for ip_addr in ip_list:
                ip = ip_addr.split(':')
                logger.info("ip: '%s'" % (ip))
                if ip[0] not in valid_ips:
                    logger.info("Node '%s' backend section '%s' "
                                "hpe3par_iscsi_ips or iscsi_ip_address "
                                "contains an invalid iSCSI "
                                "IP '%s'" % (self.node, section_name, ip))
                    result = "fail"

        else:
            logger.info("No hpe3par_iscsi_ips or iscsi_ip_address "
                        "provided for node '%s' backend "
                        "section '%s" % (self.node, section_name))
            result = 'fail'

        return result

    def get_iscsi_ips(self, section_name):
        ip_list = []
        try:
            # first check special HPE tag for multiple IPs
            ip_list = [x.strip() for x in
                       self.parser.get(section_name,
                                       'hpe3par_iscsi_ips').split(',')]
        except configparser.NoOptionError:
            try:
                # next check standard cinder.conf entry for single IP
                ip_addr = self.parser.get(section_name,
                                          'iscsi_ip_address')
                if ip_addr:
                    ip_list = []
                    ip_list.append(ip_addr)
                    return ip_list
            except configparser.NoOptionError:
                return None

        try:
            # next check standard cinder.conf entry for single IP
            ip_addr = self.parser.get(section_name,
                                      'iscsi_ip_address')
            if ip_addr:
                if not ip_list:
                    ip_list = []
                ip_list.append(ip_addr)
                return ip_list
        except configparser.NoOptionError:
            return ip_list

        return ip_list

    def has_driver(self, section_name):
        logger.info("hpe3par_wsapi_checks - has_driver()")
        """Checks that the volume_driver is installed

        :return: string
        """
        try:
            volume_driver = self.parser.get(section_name, 'volume_driver')
            path = volume_driver.split('.')
            logger.info("volume_driver: '%s'  path: '%s'" % (volume_driver, path))
            if ("%s.%s" % (path[-2], path.pop())) in constant.HPE3PAR_DRIVERS:
                path = '/'.join(path)
                logger.info("Checking for driver at '%s' for node '%s' "
                             "backend section '%s'" % (self.node, path,
                                                       section_name))
                response = self.ssh_client.execute('locate ' + path)

                if path in response:
                    result = "pass"
                elif ('command not found' or 'command-not-found') in response:
                    logger.warning("Could not check '%s' driver on node'%s'. "
                                   "Make sure that 'mlocate' is installed on "
                                   "the node." % (section_name, self.node))
                    result = "unknown"
                else:
                    logger.info("Node '%s' backend section '%s' volume_driver "
                                "contains an "
                                "invalid driver location: '%s'" % (
                        self.node, section_name,  path))
                    result = "fail"
            else:
                logger.info("Node '%s' backend section '%s' volume_driver is "
                            "invalid " % (self.node, section_name))
                result = "fail"

        except configparser.NoOptionError:
            logger.info("No volume_diver provided for node '%s' backend "
                        "section '%s'" % (self.node, section_name))
        return result

    def get_conf_items(self, section_name):
        logger.info("get cinder.conf items")
        """Get all items listed in config.conf for this section

        :return: string
        """
        options = ['hpe3par_api_url',
                   'hpe3par_username',
                   'hpe3par_password',
                   'hpe3par_cpg',
                   'hpe3par_iscsi_ips',
                   'iscsi_ip_address',
                   'volume_backend_name',
                   'volume_driver']

        result = ""
        for option in options:
            try:
                value = self.parser.get(section_name, option)
                logger.info("value = '%s'" % (value))
                result += option + "==" + value + ";;"
            except:
                result += option + "==<blank>" + ";;"

        logger.info("Items: '%s'" % (result))
        return result

    def get_system_info(self, section_name, client):
        logger.info("hpe3par_wsapi_checks - get_system_info()")
        """Get all system info, including licenses

        :return: string
        """
        result = "unknown"

        try:
            info = client.getStorageSystemInfo()
            result = "name:" + info['name'] + ";;"
            result += "os_version:" + info['systemVersion'] + ";;"
            result += "model:" + info['model'] + ";;"
            result += "serial_number:" + info['serialNumber'] + ";;"
            result += "ip_address:" + info['IPv4Addr'] + ";;"
            result += "licenses:"
            if 'licenseInfo' in info:
                if 'licenses' in info['licenseInfo']:
                    valid_licenses = info['licenseInfo']['licenses']
                    one_added = False
                    for license in valid_licenses:
                        if one_added:
                            result += ";"
                        one_added = True
                        entry = license.get('name')
                        if 'expiryTimeSec' in license:
                            entry += "//" + str(license.get('expiryTimeSec'))
                        logger.info("License: '%s' - " % (entry))
                        result += entry
            info = client.getWsApiVersion()
            result += ";;wsapi_version:" + str(info['major']) + "." + \
                str(info['minor']) + "." + str(info['revision']) + \
                "." + str(info['build']) + ";;"

            # the following is needed to get pool information
            # get list of cpgs
            result += "host_name:" + self.ssh_client.get_host_name() + ";;"
            result += "backend:" + section_name + ";;"
            result += "cpgs:" + self.parser.get(section_name, 'hpe3par_cpg')

            logger.info("Result: '%s' - " % (result))
        except configparser.NoOptionError:
            logger.info("No license info for backend section "
                        "'%s'" %
                        (section_name))
        return result
