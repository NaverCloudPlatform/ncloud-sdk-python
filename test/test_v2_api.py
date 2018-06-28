# coding: utf-8

from __future__ import absolute_import

import unittest

import ncloud_server
from ncloud_server.api.v2_api import V2Api  # noqa: E501
from ncloud_server.rest import ApiException

import ncloud_apikey
from ncloud_apikey.ncloud_key import NcloudKey

class TestV2Api(unittest.TestCase):
    """V2Api unit test stubs"""

    def setUp(self):
        configuration = ncloud_server.Configuration()
        apikeys = NcloudKey().keys()
        configuration.access_key = apikeys['access_key'] # "C9z~~~~~~~~~~~~~~XKn"
        configuration.secret_key = apikeys['secret_key'] # "NDgS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~d2X3g"
        print("configuration.access_key={}, configuration.secret_key={}".format(configuration.access_key, configuration.secret_key))
        self.api = ncloud_server.api.v2_api.V2Api(ncloud_server.ApiClient(configuration))  # noqa: E501

    def tearDown(self):
        pass

    def test_get_login_key_list(self):
        """Test case for get_login_key_list """
        get_login_key_list_request = ncloud_server.GetLoginKeyListRequest()
        try:
            api_response = self.api.get_login_key_list(get_login_key_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_login_key_list: %s\n" % e)

        pass

if __name__ == '__main__':
    unittest.main()
