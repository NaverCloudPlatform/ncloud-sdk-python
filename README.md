# ncloud-sdk

## 설치

### For [Python](https://www.python.org/)

#### pip
설치는 pip를 이용해서 아래의 명령어로 설치할 수 있습니다.

```
pip install ncloud-sdk --user
```

#### Requirements.
Python 2.7 and 3.4+

## 시작하기

### ncloud-sdk 를 사용하기 위해서는 먼저 인증키를 생성해야 합니다.
- 인증키는 [포털](https://www.ncloud.com)의 마이페이지 > 계정관리 > [인증키 관리](https://www.ncloud.com/mypage/manage/authkey) 메뉴에서 "신규 API 인증키 생성"을 통해서 Access Key ID, Secret Key를 생성합니다.
- 이미 생성된 인증키가 있을 경우 [포털](https://www.ncloud.com)의 마이페이지 > 계정관리 > [인증키 관리](https://www.ncloud.com/mypage/manage/authkey) 메뉴에서 확인할 수 있습니다.
- sub account의 경우, [Console](https://console.ncloud.com)의 [Sub Account](https://console.ncloud.com/iam/dashboard) > Sub Accounts > 서브 계정 상세 메뉴에서 "API Key"탭에서 생성한 Access Key ID, Secret Key를 사용할 수도 있습니다.

### 생성된 인증키 정보를 저장합니다.
- Mac/Linux의 경우 ~/.ncloud/configure에, Windows의 경우 C:\Users\USERNAME\\.ncloud\configure에 인증키 정보를 저장합니다.
- configure 파일은 [NCLOUD CLI](http://docs.ncloud.com/ko/tool/tool-3-1.html) 를 이용하여 생성할 수도 있습니다.
- configure example
```
ncloud_access_key_id = C9zxQyBQVqcRNQmcAXKn
ncloud_secret_access_key = NDgSdssXg4RiMMN1f5dqIe775GJXzSe8hWpd2X3g
```

## Example

#### server

```python
import ncloud_server
from ncloud_server.api.v2_api import V2Api
from ncloud_server.rest import ApiException
import ncloud_apikey

configuration = ncloud_server.Configuration()

apikeys = ncloud_apikey.ncloud_key.NcloudKey().keys()
configuration.access_key = apikeys['access_key']
configuration.secret_key = apikeys['secret_key']

api = V2Api(ncloud_server.ApiClient(configuration))

get_login_key_list_request = ncloud_server.GetLoginKeyListRequest()
try:
    api_response = api.get_login_key_list(get_login_key_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_login_key_list: %s\n" % e)
```

#### cdn

```python
import ncloud_cdn
from ncloud_cdn.api.v2_api import V2Api
from ncloud_cdn.rest import ApiException
import ncloud_apikey

configuration = ncloud_cdn.Configuration()

apikeys = ncloud_apikey.ncloud_key.NcloudKey().keys()
configuration.access_key = apikeys['access_key']
configuration.secret_key = apikeys['secret_key']

api = V2Api(ncloud_cdn.ApiClient(configuration))

get_cdn_plus_instance_list_request = ncloud_cdn.GetCdnPlusInstanceListRequest()
try:
    api_response = api.get_cdn_plus_instance_list(get_cdn_plus_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_cdn_plus_instance_list: %s\n" % e)
```

## Documentation for individual modules

Services | Documentation | Install Command
------------ | ------------- | -------------
*Server* | [**Server**](lib/services/server/README.md) | pip install ncloud-server
*Loadbalancer* | [**Loadbalancer**](lib/services/loadbalancer/README.md) | pip install ncloud-loadbalancer
*Autoscaling* | [**Autoscaling**](lib/services/autoscaling/README.md) | pip install ncloud-autoscaling
*Monitoring* | [**Monitoring**](lib/services/monitoring/README.md) | pip install ncloud-monitoring
*CDN* | [**CDN**](lib/services/cdn/README.md) | pip install ncloud-cdn
*CloudDB* | [**CloudDB**](lib/services/clouddb/README.md) | pip install ncloud-clouddb


### License

```
Copyright (c) 2018 NAVER BUSINESS PLATFORM Corp.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
