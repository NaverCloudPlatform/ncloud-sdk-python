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
- configure 파일은 [NCLOUD CLI](https://cli.ncloud-docs.com/docs/guide-userguide) 를 이용하여 생성할 수도 있습니다.
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


## Server Role

- Server Role은 서브계정과 유사한 수준의 권한을 Server에 부여하는 서비스로 VPC Server에 적용할 수 있는 서비스입니다. Role이 설정된 Server 내에서 Ncloud SDK 를 실행하면 metadata api를 통해 임시 자격 증명을 받아와서 API인증키로 사용됩니다. 
- Server Role을 사용하기 위해 ncloud-sdk-js `ncloud.init` 를 호출해서 인증키를 받아야 합니다. Server Role 인증키 적용 방법은 Example 을 참고하시기 바랍니다.
- [Console](https://console.ncloud.com)의 [Sub Account](https://console.ncloud.com/iam/dashboard) > Roles 메뉴에서 Server Role을 설정할 수 있습니다.
 
### Server Example

```python
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
```

`CredentialsResolver().load_credentials()`를 사용하면 아래 순서로 인증키를 찾습니다: 

1. Environment: NCLOUD_ACCESS_KEY_ID (또는 NCLOUD_ACCESS_KEY), NCLOUD_SECRET_KEY (또는 NCLOUD_SECRET_ACCESS_KEY) 환경변수 정보를 찾습니다. 
2. Config File: configure 파일에서 인증키를 찾습니다. Mac/Linux 의 경우 ~/.ncloud/configure 에, Windows 의 경우 C:\Users\USERNAME\\.ncloud\configure 에 인증키 정보를 저장합니다.
3. Server Role: Server Role이 설정된 VPC Server에서 metadata api 를 통해 임시 인증키를 찾습니다. 임시 인증키는 Role에 부여된 권한과 같습니다.



## Documentation for individual modules

Services | Documentation | Install Command
------------ | ------------- | -------------
*Server* | [**Server**](https://github.com/NaverCloudPlatform/ncloud-sdk-python/blob/master/lib/services/server/README.md) | pip install ncloud-server
*Loadbalancer* | [**Loadbalancer**](https://github.com/NaverCloudPlatform/ncloud-sdk-python/blob/master/lib/services/loadbalancer/README.md) | pip install ncloud-loadbalancer
*Autoscaling* | [**Autoscaling**](https://github.com/NaverCloudPlatform/ncloud-sdk-python/blob/master/lib/services/autoscaling/README.md) | pip install ncloud-autoscaling
*Monitoring* | [**Monitoring**](https://github.com/NaverCloudPlatform/ncloud-sdk-python/blob/master/lib/services/monitoring/README.md) | pip install ncloud-monitoring
*CDN* | [**CDN**](https://github.com/NaverCloudPlatform/ncloud-sdk-python/blob/master/lib/services/cdn/README.md) | pip install ncloud-cdn
*CloudDB* | [**CloudDB**](https://github.com/NaverCloudPlatform/ncloud-sdk-python/blob/master/lib/services/clouddb/README.md) | pip install ncloud-clouddb
*Server(VPC)* | [**Server(VPC)**](https://github.com/NaverCloudPlatform/ncloud-sdk-python/blob/master/lib/services/vserver/README.md) | pip install ncloud-vserver
*VPC* | [**VPC**](https://github.com/NaverCloudPlatform/ncloud-sdk-python/blob/master/lib/services/vpc/README.md) | pip install ncloud-vpc
*Nas(VPC)* | [**Nas(VPC)**](https://github.com/NaverCloudPlatform/ncloud-sdk-python/blob/master/lib/services/vnas/README.md) | pip install ncloud-vnas


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
