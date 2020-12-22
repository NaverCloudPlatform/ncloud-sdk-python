# coding: utf-8
import ncloud_server
from ncloud_server.api.v2_api import V2Api
from ncloud_server.rest import ApiException
from ncloud_apikey.credentials import CredentialsResolver

configuration = ncloud_server.Configuration()

credentials = CredentialsResolver().load_credentials()
configuration.access_key = credentials.access_key
configuration.secret_key = credentials.secret_key

api = V2Api(ncloud_server.ApiClient(configuration))

get_login_key_list_request = ncloud_server.GetLoginKeyListRequest()
try:
    api_response = api.get_login_key_list(get_login_key_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_login_key_list: %s\n" % e)