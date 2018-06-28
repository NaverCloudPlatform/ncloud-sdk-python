# coding: utf-8

from __future__ import absolute_import

import unittest

import ncloud_apikey
from ncloud_apikey.ncloud_key import NcloudKey

class TestApikey(unittest.TestCase):
    """Apikey unit test stubs"""

    def tearDown(self):
        pass

    def test_get_apikey(self):
        """Test case for get apikey file """
        print("@@ test_get_apikey")
        print(NcloudKey().keys())

        pass

    def test_init_apikey(self):
        """Test case for set apikey """
        print("@@ test_init_apikey")
        print(NcloudKey({'access_key':'abc', 'secret_key':'def'}).keys())
        print(NcloudKey().keys())

        pass

    def test_get_apikey_multi(self):
        """Test case for get apikey multi """
        print("@@ test_get_apikey_multi")
        print(NcloudKey().keys())
        print(NcloudKey().keys())
        print(NcloudKey({'access_key':'abc', 'secret_key':'def'}).keys())
        print(NcloudKey().keys())

        nkey = NcloudKey()
        print(nkey.keys())
        print(nkey.keys())

        pass

if __name__ == '__main__':
    unittest.main()
