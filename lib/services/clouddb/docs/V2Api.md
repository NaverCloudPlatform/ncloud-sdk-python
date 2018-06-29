# ncloud_clouddb.V2Api

All URIs are relative to *https://ncloud.apigw.ntruss.com/clouddb/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_db_instance**](V2Api.md#create_cloud_db_instance) | **POST** /createCloudDBInstance | 
[**delete_cloud_db_server_instance**](V2Api.md#delete_cloud_db_server_instance) | **POST** /deleteCloudDBServerInstance | 
[**get_cloud_db_config_group_list**](V2Api.md#get_cloud_db_config_group_list) | **POST** /getCloudDBConfigGroupList | 
[**get_cloud_db_image_product_list**](V2Api.md#get_cloud_db_image_product_list) | **POST** /getCloudDBImageProductList | 
[**get_cloud_db_instance_list**](V2Api.md#get_cloud_db_instance_list) | **POST** /getCloudDBInstanceList | 
[**get_cloud_db_product_list**](V2Api.md#get_cloud_db_product_list) | **POST** /getCloudDBProductList | 
[**reboot_cloud_db_server_instance**](V2Api.md#reboot_cloud_db_server_instance) | **POST** /rebootCloudDBServerInstance | 


# **create_cloud_db_instance**
> CreateCloudDBInstanceResponse create_cloud_db_instance(create_cloud_db_instance_request)



CloudDB인스턴스생성

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
create_cloud_db_instance_request = ncloud_clouddb.CreateCloudDBInstanceRequest() # CreateCloudDBInstanceRequest | createCloudDBInstanceRequest

try:
    api_response = api_instance.create_cloud_db_instance(create_cloud_db_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_cloud_db_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_cloud_db_instance_request** | [**CreateCloudDBInstanceRequest**](CreateCloudDBInstanceRequest.md)| createCloudDBInstanceRequest | 

### Return type

[**CreateCloudDBInstanceResponse**](CreateCloudDBInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_db_server_instance**
> DeleteCloudDBServerInstanceResponse delete_cloud_db_server_instance(delete_cloud_db_server_instance_request)



CloudDB서버인스턴스삭제

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
delete_cloud_db_server_instance_request = ncloud_clouddb.DeleteCloudDBServerInstanceRequest() # DeleteCloudDBServerInstanceRequest | deleteCloudDBServerInstanceRequest

try:
    api_response = api_instance.delete_cloud_db_server_instance(delete_cloud_db_server_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_cloud_db_server_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_cloud_db_server_instance_request** | [**DeleteCloudDBServerInstanceRequest**](DeleteCloudDBServerInstanceRequest.md)| deleteCloudDBServerInstanceRequest | 

### Return type

[**DeleteCloudDBServerInstanceResponse**](DeleteCloudDBServerInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_db_config_group_list**
> GetCloudDBConfigGroupListResponse get_cloud_db_config_group_list(get_cloud_db_config_group_list_request)



CloudDB설정그룹리스트조회

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
get_cloud_db_config_group_list_request = ncloud_clouddb.GetCloudDBConfigGroupListRequest() # GetCloudDBConfigGroupListRequest | getCloudDBConfigGroupListRequest

try:
    api_response = api_instance.get_cloud_db_config_group_list(get_cloud_db_config_group_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_cloud_db_config_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cloud_db_config_group_list_request** | [**GetCloudDBConfigGroupListRequest**](GetCloudDBConfigGroupListRequest.md)| getCloudDBConfigGroupListRequest | 

### Return type

[**GetCloudDBConfigGroupListResponse**](GetCloudDBConfigGroupListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_db_image_product_list**
> GetCloudDBImageProductListResponse get_cloud_db_image_product_list(get_cloud_db_image_product_list_request)



CloudDB이미지상품리스트

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
get_cloud_db_image_product_list_request = ncloud_clouddb.GetCloudDBImageProductListRequest() # GetCloudDBImageProductListRequest | getCloudDBImageProductListRequest

try:
    api_response = api_instance.get_cloud_db_image_product_list(get_cloud_db_image_product_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_cloud_db_image_product_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cloud_db_image_product_list_request** | [**GetCloudDBImageProductListRequest**](GetCloudDBImageProductListRequest.md)| getCloudDBImageProductListRequest | 

### Return type

[**GetCloudDBImageProductListResponse**](GetCloudDBImageProductListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_db_instance_list**
> GetCloudDBInstanceListResponse get_cloud_db_instance_list(get_cloud_db_instance_list_request)



CloudDB인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
get_cloud_db_instance_list_request = ncloud_clouddb.GetCloudDBInstanceListRequest() # GetCloudDBInstanceListRequest | getCloudDBInstanceListRequest

try:
    api_response = api_instance.get_cloud_db_instance_list(get_cloud_db_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_cloud_db_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cloud_db_instance_list_request** | [**GetCloudDBInstanceListRequest**](GetCloudDBInstanceListRequest.md)| getCloudDBInstanceListRequest | 

### Return type

[**GetCloudDBInstanceListResponse**](GetCloudDBInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_db_product_list**
> GetCloudDBProductListResponse get_cloud_db_product_list(get_cloud_db_product_list_request)



CloudDB상품리스트조회

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
get_cloud_db_product_list_request = ncloud_clouddb.GetCloudDBProductListRequest() # GetCloudDBProductListRequest | getCloudDBProductListRequest

try:
    api_response = api_instance.get_cloud_db_product_list(get_cloud_db_product_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_cloud_db_product_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cloud_db_product_list_request** | [**GetCloudDBProductListRequest**](GetCloudDBProductListRequest.md)| getCloudDBProductListRequest | 

### Return type

[**GetCloudDBProductListResponse**](GetCloudDBProductListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reboot_cloud_db_server_instance**
> RebootCloudDBServerInstanceResponse reboot_cloud_db_server_instance(reboot_cloud_db_server_instance_request)



CloudDB서버인스턴스재부팅

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
reboot_cloud_db_server_instance_request = ncloud_clouddb.RebootCloudDBServerInstanceRequest() # RebootCloudDBServerInstanceRequest | rebootCloudDBServerInstanceRequest

try:
    api_response = api_instance.reboot_cloud_db_server_instance(reboot_cloud_db_server_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->reboot_cloud_db_server_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reboot_cloud_db_server_instance_request** | [**RebootCloudDBServerInstanceRequest**](RebootCloudDBServerInstanceRequest.md)| rebootCloudDBServerInstanceRequest | 

### Return type

[**RebootCloudDBServerInstanceResponse**](RebootCloudDBServerInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

