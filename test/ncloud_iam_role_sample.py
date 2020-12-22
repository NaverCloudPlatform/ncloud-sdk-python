# coding: utf-8

import time
import thread
import datetime
import ncloud_server
from ncloud_server.api.v2_api import V2Api
from ncloud_server.rest import ApiException
from ncloud_apikey.credentials import CredentialsResolver


def test_server_api(tid, time_to_sleep, api):
    print('thread %d, now %s, sleep %ss' % (tid, datetime.datetime.now().time(), time_to_sleep))
    try:
        get_login_key_list_request = ncloud_server.GetLoginKeyListRequest()
        api_response = api.get_login_key_list(get_login_key_list_request)
        print('thread %d, now: %s, response: %s' % (tid, datetime.datetime.now().time(), api_response))
    except ApiException as e:
        print("Exception when calling V2Api->get_login_key_list: %s\n" % e)
    print('thread %d, now: %s, end' % (tid, datetime.datetime.now().time()))


configuration = ncloud_server.Configuration()

credentials = CredentialsResolver().load_credentials()
configuration.access_key = credentials.access_key
configuration.secret_key = credentials.secret_key

api = V2Api(ncloud_server.ApiClient(configuration))

print('start: %s' % datetime.datetime.now().time())

# mandatory refresh (10)
thread.start_new_thread(test_server_api, (0, 5, api))
time.sleep(1)

# advisory refresh (30)
thread.start_new_thread(test_server_api, (1, 20, api))

time.sleep(20)

print('end: %s' % datetime.datetime.now().time())
