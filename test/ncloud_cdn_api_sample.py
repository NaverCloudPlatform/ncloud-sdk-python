# coding: utf-8

import ncloud_cdn
from ncloud_cdn.api.v2_api import V2Api
from ncloud_cdn.rest import ApiException
import ncloud_apikey

configuration = ncloud_cdn.Configuration()

apikeys = ncloud_apikey.ncloud_key.NcloudKey().keys()
configuration.access_key = apikeys['access_key'] # "C9zx~~~~~~~~~~~~AXKn"
configuration.secret_key = apikeys['secret_key'] # "NDgSd~~~~~~~~~~~~~~~~~~~~~~~~~~~~~pd2X3g"

api = V2Api(ncloud_cdn.ApiClient(configuration))

get_cdn_plus_instance_list_request = ncloud_cdn.GetCdnPlusInstanceListRequest()
try:
    api_response = api.get_cdn_plus_instance_list(get_cdn_plus_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_cdn_plus_instance_list: %s\n" % e)
