# ncloud_cdn.V2Api

All URIs are relative to *https://ncloud.apigw.ntruss.com/cdn/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cdn_plus_instance_list**](V2Api.md#get_cdn_plus_instance_list) | **POST** /getCdnPlusInstanceList | 
[**get_cdn_plus_purge_history_list**](V2Api.md#get_cdn_plus_purge_history_list) | **POST** /getCdnPlusPurgeHistoryList | 
[**get_global_cdn_instance_list**](V2Api.md#get_global_cdn_instance_list) | **POST** /getGlobalCdnInstanceList | 
[**get_global_cdn_purge_history_list**](V2Api.md#get_global_cdn_purge_history_list) | **POST** /getGlobalCdnPurgeHistoryList | 
[**request_cdn_plus_purge**](V2Api.md#request_cdn_plus_purge) | **POST** /requestCdnPlusPurge | 
[**request_global_cdn_purge**](V2Api.md#request_global_cdn_purge) | **POST** /requestGlobalCdnPurge | 


# **get_cdn_plus_instance_list**
> GetCdnPlusInstanceListResponse get_cdn_plus_instance_list(get_cdn_plus_instance_list_request)



CDN+인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_cdn
from ncloud_cdn.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_cdn.V2Api(ncloud_cdn.ApiClient(configuration))
get_cdn_plus_instance_list_request = ncloud_cdn.GetCdnPlusInstanceListRequest() # GetCdnPlusInstanceListRequest | getCdnPlusInstanceListRequest

try:
    api_response = api_instance.get_cdn_plus_instance_list(get_cdn_plus_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_cdn_plus_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cdn_plus_instance_list_request** | [**GetCdnPlusInstanceListRequest**](GetCdnPlusInstanceListRequest.md)| getCdnPlusInstanceListRequest | 

### Return type

[**GetCdnPlusInstanceListResponse**](GetCdnPlusInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cdn_plus_purge_history_list**
> GetCdnPlusPurgeHistoryListResponse get_cdn_plus_purge_history_list(get_cdn_plus_purge_history_list_request)



CDN+퍼지기록조회

### Example
```python
from __future__ import print_function
import ncloud_cdn
from ncloud_cdn.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_cdn.V2Api(ncloud_cdn.ApiClient(configuration))
get_cdn_plus_purge_history_list_request = ncloud_cdn.GetCdnPlusPurgeHistoryListRequest() # GetCdnPlusPurgeHistoryListRequest | getCdnPlusPurgeHistoryListRequest

try:
    api_response = api_instance.get_cdn_plus_purge_history_list(get_cdn_plus_purge_history_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_cdn_plus_purge_history_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cdn_plus_purge_history_list_request** | [**GetCdnPlusPurgeHistoryListRequest**](GetCdnPlusPurgeHistoryListRequest.md)| getCdnPlusPurgeHistoryListRequest | 

### Return type

[**GetCdnPlusPurgeHistoryListResponse**](GetCdnPlusPurgeHistoryListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_cdn_instance_list**
> GetGlobalCdnInstanceListResponse get_global_cdn_instance_list(get_global_cdn_instance_list_request)



Global CDN 인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_cdn
from ncloud_cdn.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_cdn.V2Api(ncloud_cdn.ApiClient(configuration))
get_global_cdn_instance_list_request = ncloud_cdn.GetGlobalCdnInstanceListRequest() # GetGlobalCdnInstanceListRequest | getGlobalCdnInstanceListRequest

try:
    api_response = api_instance.get_global_cdn_instance_list(get_global_cdn_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_global_cdn_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_global_cdn_instance_list_request** | [**GetGlobalCdnInstanceListRequest**](GetGlobalCdnInstanceListRequest.md)| getGlobalCdnInstanceListRequest | 

### Return type

[**GetGlobalCdnInstanceListResponse**](GetGlobalCdnInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_cdn_purge_history_list**
> GetGlobalCdnPurgeHistoryListResponse get_global_cdn_purge_history_list(get_global_cdn_purge_history_list_request)



Global CDN퍼지기록조회

### Example
```python
from __future__ import print_function
import ncloud_cdn
from ncloud_cdn.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_cdn.V2Api(ncloud_cdn.ApiClient(configuration))
get_global_cdn_purge_history_list_request = ncloud_cdn.GetCdnPlusPurgeHistoryListRequest() # GetCdnPlusPurgeHistoryListRequest | getGlobalCdnPurgeHistoryListRequest

try:
    api_response = api_instance.get_global_cdn_purge_history_list(get_global_cdn_purge_history_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_global_cdn_purge_history_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_global_cdn_purge_history_list_request** | [**GetCdnPlusPurgeHistoryListRequest**](GetCdnPlusPurgeHistoryListRequest.md)| getGlobalCdnPurgeHistoryListRequest | 

### Return type

[**GetGlobalCdnPurgeHistoryListResponse**](GetGlobalCdnPurgeHistoryListResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_cdn_plus_purge**
> RequestCdnPlusPurgeResponse request_cdn_plus_purge(request_cdn_plus_purge_request)



CDN+퍼지요청

### Example
```python
from __future__ import print_function
import ncloud_cdn
from ncloud_cdn.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_cdn.V2Api(ncloud_cdn.ApiClient(configuration))
request_cdn_plus_purge_request = ncloud_cdn.RequestCdnPlusPurgeRequest() # RequestCdnPlusPurgeRequest | requestCdnPlusPurgeRequest

try:
    api_response = api_instance.request_cdn_plus_purge(request_cdn_plus_purge_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->request_cdn_plus_purge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_cdn_plus_purge_request** | [**RequestCdnPlusPurgeRequest**](RequestCdnPlusPurgeRequest.md)| requestCdnPlusPurgeRequest | 

### Return type

[**RequestCdnPlusPurgeResponse**](RequestCdnPlusPurgeResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_global_cdn_purge**
> RequestGlobalCdnPurgeResponse request_global_cdn_purge(request_global_cdn_purge_request)



Global CDN퍼지요청

### Example
```python
from __future__ import print_function
import ncloud_cdn
from ncloud_cdn.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_cdn.V2Api(ncloud_cdn.ApiClient(configuration))
request_global_cdn_purge_request = ncloud_cdn.RequestGlobalCdnPurgeRequest() # RequestGlobalCdnPurgeRequest | requestGlobalCdnPurgeRequest

try:
    api_response = api_instance.request_global_cdn_purge(request_global_cdn_purge_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->request_global_cdn_purge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_global_cdn_purge_request** | [**RequestGlobalCdnPurgeRequest**](RequestGlobalCdnPurgeRequest.md)| requestGlobalCdnPurgeRequest | 

### Return type

[**RequestGlobalCdnPurgeResponse**](RequestGlobalCdnPurgeResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

