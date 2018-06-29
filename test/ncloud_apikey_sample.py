# coding: utf-8

import ncloud_apikey

try:
    apikeys = ncloud_apikey.ncloud_key.NcloudKey().keys()
    print(apikeys)
except ApiException as e:
    print("Exception when ncloud_key: %s\n" % e)
