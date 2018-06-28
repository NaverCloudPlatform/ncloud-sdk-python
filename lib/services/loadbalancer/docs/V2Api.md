# ncloud_loadbalancer.V2Api

All URIs are relative to *https://ncloud.apigw.ntruss.com/loadbalancer/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_load_balancer_ssl_certificate**](V2Api.md#add_load_balancer_ssl_certificate) | **POST** /addLoadBalancerSslCertificate | 
[**change_load_balanced_server_instances**](V2Api.md#change_load_balanced_server_instances) | **POST** /changeLoadBalancedServerInstances | 
[**change_load_balancer_instance_configuration**](V2Api.md#change_load_balancer_instance_configuration) | **POST** /changeLoadBalancerInstanceConfiguration | 
[**create_load_balancer_instance**](V2Api.md#create_load_balancer_instance) | **POST** /createLoadBalancerInstance | 
[**delete_load_balancer_instances**](V2Api.md#delete_load_balancer_instances) | **POST** /deleteLoadBalancerInstances | 
[**delete_load_balancer_ssl_certificate**](V2Api.md#delete_load_balancer_ssl_certificate) | **POST** /deleteLoadBalancerSslCertificate | 
[**get_load_balanced_server_instance_list**](V2Api.md#get_load_balanced_server_instance_list) | **POST** /getLoadBalancedServerInstanceList | 
[**get_load_balancer_instance_list**](V2Api.md#get_load_balancer_instance_list) | **POST** /getLoadBalancerInstanceList | 
[**get_load_balancer_ssl_certificate_list**](V2Api.md#get_load_balancer_ssl_certificate_list) | **POST** /getLoadBalancerSslCertificateList | 
[**get_load_balancer_target_server_instance_list**](V2Api.md#get_load_balancer_target_server_instance_list) | **POST** /getLoadBalancerTargetServerInstanceList | 


# **add_load_balancer_ssl_certificate**
> AddLoadBalancerSslCertificateResponse add_load_balancer_ssl_certificate(add_load_balancer_ssl_certificate_request)



로드밸런서SSL인증서추가

### Example
```python
from __future__ import print_function
import ncloud_loadbalancer
from ncloud_loadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_loadbalancer.V2Api(ncloud_loadbalancer.ApiClient(configuration))
add_load_balancer_ssl_certificate_request = ncloud_loadbalancer.AddLoadBalancerSslCertificateRequest() # AddLoadBalancerSslCertificateRequest | addLoadBalancerSslCertificateRequest

try:
    api_response = api_instance.add_load_balancer_ssl_certificate(add_load_balancer_ssl_certificate_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->add_load_balancer_ssl_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_load_balancer_ssl_certificate_request** | [**AddLoadBalancerSslCertificateRequest**](AddLoadBalancerSslCertificateRequest.md)| addLoadBalancerSslCertificateRequest | 

### Return type

[**AddLoadBalancerSslCertificateResponse**](AddLoadBalancerSslCertificateResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_load_balanced_server_instances**
> ChangeLoadBalancedServerInstancesResponse change_load_balanced_server_instances(change_load_balanced_server_instances_request)



로드밸런서에Bind된서버인스턴스변경

### Example
```python
from __future__ import print_function
import ncloud_loadbalancer
from ncloud_loadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_loadbalancer.V2Api(ncloud_loadbalancer.ApiClient(configuration))
change_load_balanced_server_instances_request = ncloud_loadbalancer.ChangeLoadBalancedServerInstancesRequest() # ChangeLoadBalancedServerInstancesRequest | changeLoadBalancedServerInstancesRequest

try:
    api_response = api_instance.change_load_balanced_server_instances(change_load_balanced_server_instances_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->change_load_balanced_server_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_load_balanced_server_instances_request** | [**ChangeLoadBalancedServerInstancesRequest**](ChangeLoadBalancedServerInstancesRequest.md)| changeLoadBalancedServerInstancesRequest | 

### Return type

[**ChangeLoadBalancedServerInstancesResponse**](ChangeLoadBalancedServerInstancesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_load_balancer_instance_configuration**
> ChangeLoadBalancerInstanceConfigurationResponse change_load_balancer_instance_configuration(change_load_balancer_instance_configuration_request)



로드밸런서인스턴스설정변경

### Example
```python
from __future__ import print_function
import ncloud_loadbalancer
from ncloud_loadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_loadbalancer.V2Api(ncloud_loadbalancer.ApiClient(configuration))
change_load_balancer_instance_configuration_request = ncloud_loadbalancer.ChangeLoadBalancerInstanceConfigurationRequest() # ChangeLoadBalancerInstanceConfigurationRequest | changeLoadBalancerInstanceConfigurationRequest

try:
    api_response = api_instance.change_load_balancer_instance_configuration(change_load_balancer_instance_configuration_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->change_load_balancer_instance_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_load_balancer_instance_configuration_request** | [**ChangeLoadBalancerInstanceConfigurationRequest**](ChangeLoadBalancerInstanceConfigurationRequest.md)| changeLoadBalancerInstanceConfigurationRequest | 

### Return type

[**ChangeLoadBalancerInstanceConfigurationResponse**](ChangeLoadBalancerInstanceConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_load_balancer_instance**
> CreateLoadBalancerInstanceResponse create_load_balancer_instance(create_load_balancer_instance_request)



로드밸런서인스턴스생성

### Example
```python
from __future__ import print_function
import ncloud_loadbalancer
from ncloud_loadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_loadbalancer.V2Api(ncloud_loadbalancer.ApiClient(configuration))
create_load_balancer_instance_request = ncloud_loadbalancer.CreateLoadBalancerInstanceRequest() # CreateLoadBalancerInstanceRequest | createLoadBalancerInstanceRequest

try:
    api_response = api_instance.create_load_balancer_instance(create_load_balancer_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_load_balancer_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_load_balancer_instance_request** | [**CreateLoadBalancerInstanceRequest**](CreateLoadBalancerInstanceRequest.md)| createLoadBalancerInstanceRequest | 

### Return type

[**CreateLoadBalancerInstanceResponse**](CreateLoadBalancerInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer_instances**
> DeleteLoadBalancerInstancesResponse delete_load_balancer_instances(delete_load_balancer_instances_request)



로드밸런서인스턴스삭제

### Example
```python
from __future__ import print_function
import ncloud_loadbalancer
from ncloud_loadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_loadbalancer.V2Api(ncloud_loadbalancer.ApiClient(configuration))
delete_load_balancer_instances_request = ncloud_loadbalancer.DeleteLoadBalancerInstancesRequest() # DeleteLoadBalancerInstancesRequest | deleteLoadBalancerInstancesRequest

try:
    api_response = api_instance.delete_load_balancer_instances(delete_load_balancer_instances_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_load_balancer_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_load_balancer_instances_request** | [**DeleteLoadBalancerInstancesRequest**](DeleteLoadBalancerInstancesRequest.md)| deleteLoadBalancerInstancesRequest | 

### Return type

[**DeleteLoadBalancerInstancesResponse**](DeleteLoadBalancerInstancesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer_ssl_certificate**
> DeleteLoadBalancerSslCertificateResponse delete_load_balancer_ssl_certificate(delete_load_balancer_ssl_certificate_request)



로드밸런서SSL인증서삭제

### Example
```python
from __future__ import print_function
import ncloud_loadbalancer
from ncloud_loadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_loadbalancer.V2Api(ncloud_loadbalancer.ApiClient(configuration))
delete_load_balancer_ssl_certificate_request = ncloud_loadbalancer.DeleteLoadBalancerSslCertificateRequest() # DeleteLoadBalancerSslCertificateRequest | deleteLoadBalancerSslCertificateRequest

try:
    api_response = api_instance.delete_load_balancer_ssl_certificate(delete_load_balancer_ssl_certificate_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_load_balancer_ssl_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_load_balancer_ssl_certificate_request** | [**DeleteLoadBalancerSslCertificateRequest**](DeleteLoadBalancerSslCertificateRequest.md)| deleteLoadBalancerSslCertificateRequest | 

### Return type

[**DeleteLoadBalancerSslCertificateResponse**](DeleteLoadBalancerSslCertificateResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balanced_server_instance_list**
> GetLoadBalancedServerInstanceListResponse get_load_balanced_server_instance_list(get_load_balanced_server_instance_list_request)



로드밸런서Bind된서버인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_loadbalancer
from ncloud_loadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_loadbalancer.V2Api(ncloud_loadbalancer.ApiClient(configuration))
get_load_balanced_server_instance_list_request = ncloud_loadbalancer.GetLoadBalancedServerInstanceListRequest() # GetLoadBalancedServerInstanceListRequest | getLoadBalancedServerInstanceListRequest

try:
    api_response = api_instance.get_load_balanced_server_instance_list(get_load_balanced_server_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_load_balanced_server_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_load_balanced_server_instance_list_request** | [**GetLoadBalancedServerInstanceListRequest**](GetLoadBalancedServerInstanceListRequest.md)| getLoadBalancedServerInstanceListRequest | 

### Return type

[**GetLoadBalancedServerInstanceListResponse**](GetLoadBalancedServerInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer_instance_list**
> GetLoadBalancerInstanceListResponse get_load_balancer_instance_list(get_load_balancer_instance_list_request)



로드밸런서인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_loadbalancer
from ncloud_loadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_loadbalancer.V2Api(ncloud_loadbalancer.ApiClient(configuration))
get_load_balancer_instance_list_request = ncloud_loadbalancer.GetLoadBalancerInstanceListRequest() # GetLoadBalancerInstanceListRequest | getLoadBalancerInstanceListRequest

try:
    api_response = api_instance.get_load_balancer_instance_list(get_load_balancer_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_load_balancer_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_load_balancer_instance_list_request** | [**GetLoadBalancerInstanceListRequest**](GetLoadBalancerInstanceListRequest.md)| getLoadBalancerInstanceListRequest | 

### Return type

[**GetLoadBalancerInstanceListResponse**](GetLoadBalancerInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer_ssl_certificate_list**
> GetLoadBalancerSslCertificateListResponse get_load_balancer_ssl_certificate_list(get_load_balancer_ssl_certificate_list_request)



로드밸런서SSL인증서조회

### Example
```python
from __future__ import print_function
import ncloud_loadbalancer
from ncloud_loadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_loadbalancer.V2Api(ncloud_loadbalancer.ApiClient(configuration))
get_load_balancer_ssl_certificate_list_request = ncloud_loadbalancer.GetLoadBalancerSslCertificateListRequest() # GetLoadBalancerSslCertificateListRequest | getLoadBalancerSslCertificateListRequest

try:
    api_response = api_instance.get_load_balancer_ssl_certificate_list(get_load_balancer_ssl_certificate_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_load_balancer_ssl_certificate_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_load_balancer_ssl_certificate_list_request** | [**GetLoadBalancerSslCertificateListRequest**](GetLoadBalancerSslCertificateListRequest.md)| getLoadBalancerSslCertificateListRequest | 

### Return type

[**GetLoadBalancerSslCertificateListResponse**](GetLoadBalancerSslCertificateListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer_target_server_instance_list**
> GetLoadBalancerTargetServerInstanceListResponse get_load_balancer_target_server_instance_list(get_load_balancer_target_server_instance_list_request)



로드밸런서Target서버인스턴스리스트

### Example
```python
from __future__ import print_function
import ncloud_loadbalancer
from ncloud_loadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_loadbalancer.V2Api(ncloud_loadbalancer.ApiClient(configuration))
get_load_balancer_target_server_instance_list_request = ncloud_loadbalancer.GetLoadBalancerTargetServerInstanceListRequest() # GetLoadBalancerTargetServerInstanceListRequest | getLoadBalancerTargetServerInstanceListRequest

try:
    api_response = api_instance.get_load_balancer_target_server_instance_list(get_load_balancer_target_server_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_load_balancer_target_server_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_load_balancer_target_server_instance_list_request** | [**GetLoadBalancerTargetServerInstanceListRequest**](GetLoadBalancerTargetServerInstanceListRequest.md)| getLoadBalancerTargetServerInstanceListRequest | 

### Return type

[**GetLoadBalancerTargetServerInstanceListResponse**](GetLoadBalancerTargetServerInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

