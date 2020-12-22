# coding: utf-8

from __future__ import absolute_import

import time
import thread
import datetime
from ncloud_apikey.credentials import CredentialsResolver


def test_load_credentials(tid, time_to_sleep, credentials):
    print('thread %d, now %s, sleep %ss' % (tid, datetime.datetime.now().time(), time_to_sleep))
    try:
        print('thread %d, now: %s, credentials: %s,access_key: %s, expiration: %s' % (
            tid, datetime.datetime.now().time(), credentials, credentials.access_key, credentials.expiration))
    except Exception as e:
        print(e)
    print('thread %d, now: %s, end' % (tid, datetime.datetime.now().time()))


creds = CredentialsResolver().load_credentials()
print('start: %s' % (datetime.datetime.now().time()))

# mandatory refresh (10)
thread.start_new_thread(test_load_credentials, (0, 5, creds))
time.sleep(1)

# advisory refresh (30)
thread.start_new_thread(test_load_credentials, (1, 20, creds))

time.sleep(20)
