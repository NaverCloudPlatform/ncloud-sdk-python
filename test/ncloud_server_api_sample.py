# coding: utf-8

import ncloud_server
from ncloud_server.api.v2_api import V2Api
from ncloud_server.rest import ApiException
import ncloud_apikey

configuration = ncloud_server.Configuration()

apikeys = ncloud_apikey.ncloud_key.NcloudKey().keys()
configuration.access_key = apikeys['access_key'] # "C9zx~~~~~~~~~~~~AXKn"
configuration.secret_key = apikeys['secret_key'] # "NDgSd~~~~~~~~~~~~~~~~~~~~~~~~~~~~~pd2X3g"

api = V2Api(ncloud_server.ApiClient(configuration))

get_login_key_list_request = ncloud_server.GetLoginKeyListRequest()
try:
    api_response = api.get_login_key_list(get_login_key_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_login_key_list: %s\n" % e)
