# ncloud_vnas.V2Api

All URIs are relative to *https://ncloud.apigw.ntruss.com/vnas/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_nas_volume_access_control**](V2Api.md#add_nas_volume_access_control) | **POST** /addNasVolumeAccessControl | 
[**change_nas_volume_size**](V2Api.md#change_nas_volume_size) | **POST** /changeNasVolumeSize | 
[**create_nas_volume_instance**](V2Api.md#create_nas_volume_instance) | **POST** /createNasVolumeInstance | 
[**delete_nas_volume_instances**](V2Api.md#delete_nas_volume_instances) | **POST** /deleteNasVolumeInstances | 
[**get_nas_volume_instance_detail**](V2Api.md#get_nas_volume_instance_detail) | **POST** /getNasVolumeInstanceDetail | 
[**get_nas_volume_instance_list**](V2Api.md#get_nas_volume_instance_list) | **POST** /getNasVolumeInstanceList | 
[**remove_nas_volume_access_control**](V2Api.md#remove_nas_volume_access_control) | **POST** /removeNasVolumeAccessControl | 
[**set_nas_volume_access_control**](V2Api.md#set_nas_volume_access_control) | **POST** /setNasVolumeAccessControl | 


# **add_nas_volume_access_control**
> AddNasVolumeAccessControlResponse add_nas_volume_access_control(add_nas_volume_access_control_request)



NAS볼륨접근제어추가

### Example
```python
from __future__ import print_function
import ncloud_vnas
from ncloud_vnas.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vnas.V2Api(ncloud_vnas.ApiClient(configuration))
add_nas_volume_access_control_request = ncloud_vnas.AddNasVolumeAccessControlRequest() # AddNasVolumeAccessControlRequest | addNasVolumeAccessControlRequest

try:
    api_response = api_instance.add_nas_volume_access_control(add_nas_volume_access_control_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->add_nas_volume_access_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_nas_volume_access_control_request** | [**AddNasVolumeAccessControlRequest**](AddNasVolumeAccessControlRequest.md)| addNasVolumeAccessControlRequest | 

### Return type

[**AddNasVolumeAccessControlResponse**](AddNasVolumeAccessControlResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_nas_volume_size**
> ChangeNasVolumeSizeResponse change_nas_volume_size(change_nas_volume_size_request)



NAS볼륨사이즈변경

### Example
```python
from __future__ import print_function
import ncloud_vnas
from ncloud_vnas.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vnas.V2Api(ncloud_vnas.ApiClient(configuration))
change_nas_volume_size_request = ncloud_vnas.ChangeNasVolumeSizeRequest() # ChangeNasVolumeSizeRequest | changeNasVolumeSizeRequest

try:
    api_response = api_instance.change_nas_volume_size(change_nas_volume_size_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->change_nas_volume_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_nas_volume_size_request** | [**ChangeNasVolumeSizeRequest**](ChangeNasVolumeSizeRequest.md)| changeNasVolumeSizeRequest | 

### Return type

[**ChangeNasVolumeSizeResponse**](ChangeNasVolumeSizeResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nas_volume_instance**
> CreateNasVolumeInstanceResponse create_nas_volume_instance(create_nas_volume_instance_request)



NAS볼륨인스턴스생성

### Example
```python
from __future__ import print_function
import ncloud_vnas
from ncloud_vnas.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vnas.V2Api(ncloud_vnas.ApiClient(configuration))
create_nas_volume_instance_request = ncloud_vnas.CreateNasVolumeInstanceRequest() # CreateNasVolumeInstanceRequest | createNasVolumeInstanceRequest

try:
    api_response = api_instance.create_nas_volume_instance(create_nas_volume_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_nas_volume_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_nas_volume_instance_request** | [**CreateNasVolumeInstanceRequest**](CreateNasVolumeInstanceRequest.md)| createNasVolumeInstanceRequest | 

### Return type

[**CreateNasVolumeInstanceResponse**](CreateNasVolumeInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nas_volume_instances**
> DeleteNasVolumeInstancesResponse delete_nas_volume_instances(delete_nas_volume_instances_request)



NAS볼륨인스턴스제거

### Example
```python
from __future__ import print_function
import ncloud_vnas
from ncloud_vnas.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vnas.V2Api(ncloud_vnas.ApiClient(configuration))
delete_nas_volume_instances_request = ncloud_vnas.DeleteNasVolumeInstancesRequest() # DeleteNasVolumeInstancesRequest | deleteNasVolumeInstancesRequest

try:
    api_response = api_instance.delete_nas_volume_instances(delete_nas_volume_instances_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_nas_volume_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_nas_volume_instances_request** | [**DeleteNasVolumeInstancesRequest**](DeleteNasVolumeInstancesRequest.md)| deleteNasVolumeInstancesRequest | 

### Return type

[**DeleteNasVolumeInstancesResponse**](DeleteNasVolumeInstancesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nas_volume_instance_detail**
> GetNasVolumeInstanceDetailResponse get_nas_volume_instance_detail(get_nas_volume_instance_detail_request)



NAS볼륨인스턴스상세조회

### Example
```python
from __future__ import print_function
import ncloud_vnas
from ncloud_vnas.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vnas.V2Api(ncloud_vnas.ApiClient(configuration))
get_nas_volume_instance_detail_request = ncloud_vnas.GetNasVolumeInstanceDetailRequest() # GetNasVolumeInstanceDetailRequest | getNasVolumeInstanceDetailRequest

try:
    api_response = api_instance.get_nas_volume_instance_detail(get_nas_volume_instance_detail_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_nas_volume_instance_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_nas_volume_instance_detail_request** | [**GetNasVolumeInstanceDetailRequest**](GetNasVolumeInstanceDetailRequest.md)| getNasVolumeInstanceDetailRequest | 

### Return type

[**GetNasVolumeInstanceDetailResponse**](GetNasVolumeInstanceDetailResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nas_volume_instance_list**
> GetNasVolumeInstanceListResponse get_nas_volume_instance_list(get_nas_volume_instance_list_request)



NAS볼륨인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vnas
from ncloud_vnas.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vnas.V2Api(ncloud_vnas.ApiClient(configuration))
get_nas_volume_instance_list_request = ncloud_vnas.GetNasVolumeInstanceListRequest() # GetNasVolumeInstanceListRequest | getNasVolumeInstanceListRequest

try:
    api_response = api_instance.get_nas_volume_instance_list(get_nas_volume_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_nas_volume_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_nas_volume_instance_list_request** | [**GetNasVolumeInstanceListRequest**](GetNasVolumeInstanceListRequest.md)| getNasVolumeInstanceListRequest | 

### Return type

[**GetNasVolumeInstanceListResponse**](GetNasVolumeInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_nas_volume_access_control**
> RemoveNasVolumeAccessControlResponse remove_nas_volume_access_control(remove_nas_volume_access_control_request)



NAS볼륨접근제어삭제

### Example
```python
from __future__ import print_function
import ncloud_vnas
from ncloud_vnas.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vnas.V2Api(ncloud_vnas.ApiClient(configuration))
remove_nas_volume_access_control_request = ncloud_vnas.RemoveNasVolumeAccessControlRequest() # RemoveNasVolumeAccessControlRequest | removeNasVolumeAccessControlRequest

try:
    api_response = api_instance.remove_nas_volume_access_control(remove_nas_volume_access_control_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->remove_nas_volume_access_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_nas_volume_access_control_request** | [**RemoveNasVolumeAccessControlRequest**](RemoveNasVolumeAccessControlRequest.md)| removeNasVolumeAccessControlRequest | 

### Return type

[**RemoveNasVolumeAccessControlResponse**](RemoveNasVolumeAccessControlResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_nas_volume_access_control**
> SetNasVolumeAccessControlResponse set_nas_volume_access_control(set_nas_volume_access_control_request)



NAS볼륨접근제어설정

### Example
```python
from __future__ import print_function
import ncloud_vnas
from ncloud_vnas.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vnas.V2Api(ncloud_vnas.ApiClient(configuration))
set_nas_volume_access_control_request = ncloud_vnas.SetNasVolumeAccessControlRequest() # SetNasVolumeAccessControlRequest | setNasVolumeAccessControlRequest

try:
    api_response = api_instance.set_nas_volume_access_control(set_nas_volume_access_control_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->set_nas_volume_access_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_nas_volume_access_control_request** | [**SetNasVolumeAccessControlRequest**](SetNasVolumeAccessControlRequest.md)| setNasVolumeAccessControlRequest | 

### Return type

[**SetNasVolumeAccessControlResponse**](SetNasVolumeAccessControlResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

