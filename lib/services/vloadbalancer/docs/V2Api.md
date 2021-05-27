# ncloud_vloadbalancer.V2Api

All URIs are relative to *https://ncloud.apigw.ntruss.com/vloadbalancer/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_target**](V2Api.md#add_target) | **POST** /addTarget | 
[**change_load_balancer_instance_configuration**](V2Api.md#change_load_balancer_instance_configuration) | **POST** /changeLoadBalancerInstanceConfiguration | 
[**change_load_balancer_listener_configuration**](V2Api.md#change_load_balancer_listener_configuration) | **POST** /changeLoadBalancerListenerConfiguration | 
[**change_target_group_configuration**](V2Api.md#change_target_group_configuration) | **POST** /changeTargetGroupConfiguration | 
[**change_target_group_health_check_configuration**](V2Api.md#change_target_group_health_check_configuration) | **POST** /changeTargetGroupHealthCheckConfiguration | 
[**create_load_balancer_instance**](V2Api.md#create_load_balancer_instance) | **POST** /createLoadBalancerInstance | 
[**create_load_balancer_listener**](V2Api.md#create_load_balancer_listener) | **POST** /createLoadBalancerListener | 
[**create_target_group**](V2Api.md#create_target_group) | **POST** /createTargetGroup | 
[**delete_load_balancer_instances**](V2Api.md#delete_load_balancer_instances) | **POST** /deleteLoadBalancerInstances | 
[**delete_load_balancer_listeners**](V2Api.md#delete_load_balancer_listeners) | **POST** /deleteLoadBalancerListeners | 
[**delete_target_groups**](V2Api.md#delete_target_groups) | **POST** /deleteTargetGroups | 
[**get_load_balancer_instance_detail**](V2Api.md#get_load_balancer_instance_detail) | **POST** /getLoadBalancerInstanceDetail | 
[**get_load_balancer_instance_list**](V2Api.md#get_load_balancer_instance_list) | **POST** /getLoadBalancerInstanceList | 
[**get_load_balancer_listener_list**](V2Api.md#get_load_balancer_listener_list) | **POST** /getLoadBalancerListenerList | 
[**get_load_balancer_rule_list**](V2Api.md#get_load_balancer_rule_list) | **POST** /getLoadBalancerRuleList | 
[**get_target_group_detail**](V2Api.md#get_target_group_detail) | **POST** /getTargetGroupDetail | 
[**get_target_group_list**](V2Api.md#get_target_group_list) | **POST** /getTargetGroupList | 
[**get_target_list**](V2Api.md#get_target_list) | **POST** /getTargetList | 
[**remove_target**](V2Api.md#remove_target) | **POST** /removeTarget | 
[**set_load_balancer_description**](V2Api.md#set_load_balancer_description) | **POST** /setLoadBalancerDescription | 
[**set_load_balancer_instance_subnet**](V2Api.md#set_load_balancer_instance_subnet) | **POST** /setLoadBalancerInstanceSubnet | 
[**set_target**](V2Api.md#set_target) | **POST** /setTarget | 
[**set_target_group_description**](V2Api.md#set_target_group_description) | **POST** /setTargetGroupDescription | 


# **add_target**
> AddTargetResponse add_target(add_target_request)



타겟추가

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
add_target_request = ncloud_vloadbalancer.AddTargetRequest() # AddTargetRequest | addTargetRequest

try:
    api_response = api_instance.add_target(add_target_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->add_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_target_request** | [**AddTargetRequest**](AddTargetRequest.md)| addTargetRequest | 

### Return type

[**AddTargetResponse**](AddTargetResponse.md)

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
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
change_load_balancer_instance_configuration_request = ncloud_vloadbalancer.ChangeLoadBalancerInstanceConfigurationRequest() # ChangeLoadBalancerInstanceConfigurationRequest | changeLoadBalancerInstanceConfigurationRequest

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

# **change_load_balancer_listener_configuration**
> ChangeLoadBalancerListenerConfigurationResponse change_load_balancer_listener_configuration(change_load_balancer_listener_configuration_request)



로드밸런서리스너설정변경

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
change_load_balancer_listener_configuration_request = ncloud_vloadbalancer.ChangeLoadBalancerListenerConfigurationRequest() # ChangeLoadBalancerListenerConfigurationRequest | changeLoadBalancerListenerConfigurationRequest

try:
    api_response = api_instance.change_load_balancer_listener_configuration(change_load_balancer_listener_configuration_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->change_load_balancer_listener_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_load_balancer_listener_configuration_request** | [**ChangeLoadBalancerListenerConfigurationRequest**](ChangeLoadBalancerListenerConfigurationRequest.md)| changeLoadBalancerListenerConfigurationRequest | 

### Return type

[**ChangeLoadBalancerListenerConfigurationResponse**](ChangeLoadBalancerListenerConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_target_group_configuration**
> ChangeTargetGroupConfigurationResponse change_target_group_configuration(change_target_group_configuration_request)



타겟그룹설정변경

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
change_target_group_configuration_request = ncloud_vloadbalancer.ChangeTargetGroupConfigurationRequest() # ChangeTargetGroupConfigurationRequest | changeTargetGroupConfigurationRequest

try:
    api_response = api_instance.change_target_group_configuration(change_target_group_configuration_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->change_target_group_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_target_group_configuration_request** | [**ChangeTargetGroupConfigurationRequest**](ChangeTargetGroupConfigurationRequest.md)| changeTargetGroupConfigurationRequest | 

### Return type

[**ChangeTargetGroupConfigurationResponse**](ChangeTargetGroupConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_target_group_health_check_configuration**
> ChangeTargetGroupHealthCheckConfigurationResponse change_target_group_health_check_configuration(change_target_group_health_check_configuration_request)



타겟그룹헬스체크설정변경

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
change_target_group_health_check_configuration_request = ncloud_vloadbalancer.ChangeTargetGroupHealthCheckConfigurationRequest() # ChangeTargetGroupHealthCheckConfigurationRequest | changeTargetGroupHealthCheckConfigurationRequest

try:
    api_response = api_instance.change_target_group_health_check_configuration(change_target_group_health_check_configuration_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->change_target_group_health_check_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_target_group_health_check_configuration_request** | [**ChangeTargetGroupHealthCheckConfigurationRequest**](ChangeTargetGroupHealthCheckConfigurationRequest.md)| changeTargetGroupHealthCheckConfigurationRequest | 

### Return type

[**ChangeTargetGroupHealthCheckConfigurationResponse**](ChangeTargetGroupHealthCheckConfigurationResponse.md)

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
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
create_load_balancer_instance_request = ncloud_vloadbalancer.CreateLoadBalancerInstanceRequest() # CreateLoadBalancerInstanceRequest | createLoadBalancerInstanceRequest

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

# **create_load_balancer_listener**
> CreateLoadBalancerListenerResponse create_load_balancer_listener(create_load_balancer_listener_request)



로드밸런서리스너생성

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
create_load_balancer_listener_request = ncloud_vloadbalancer.CreateLoadBalancerListenerRequest() # CreateLoadBalancerListenerRequest | createLoadBalancerListenerRequest

try:
    api_response = api_instance.create_load_balancer_listener(create_load_balancer_listener_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_load_balancer_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_load_balancer_listener_request** | [**CreateLoadBalancerListenerRequest**](CreateLoadBalancerListenerRequest.md)| createLoadBalancerListenerRequest | 

### Return type

[**CreateLoadBalancerListenerResponse**](CreateLoadBalancerListenerResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_target_group**
> CreateTargetGroupResponse create_target_group(create_target_group_request)



타겟그룹생성

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
create_target_group_request = ncloud_vloadbalancer.CreateTargetGroupRequest() # CreateTargetGroupRequest | createTargetGroupRequest

try:
    api_response = api_instance.create_target_group(create_target_group_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_target_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_target_group_request** | [**CreateTargetGroupRequest**](CreateTargetGroupRequest.md)| createTargetGroupRequest | 

### Return type

[**CreateTargetGroupResponse**](CreateTargetGroupResponse.md)

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
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
delete_load_balancer_instances_request = ncloud_vloadbalancer.DeleteLoadBalancerInstancesRequest() # DeleteLoadBalancerInstancesRequest | deleteLoadBalancerInstancesRequest

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

# **delete_load_balancer_listeners**
> DeleteLoadBalancerListenersResponse delete_load_balancer_listeners(delete_load_balancer_listeners_request)



로드밸런서리스너삭제

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
delete_load_balancer_listeners_request = ncloud_vloadbalancer.DeleteLoadBalancerListenersRequest() # DeleteLoadBalancerListenersRequest | deleteLoadBalancerListenersRequest

try:
    api_response = api_instance.delete_load_balancer_listeners(delete_load_balancer_listeners_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_load_balancer_listeners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_load_balancer_listeners_request** | [**DeleteLoadBalancerListenersRequest**](DeleteLoadBalancerListenersRequest.md)| deleteLoadBalancerListenersRequest | 

### Return type

[**DeleteLoadBalancerListenersResponse**](DeleteLoadBalancerListenersResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_target_groups**
> DeleteTargetGroupsResponse delete_target_groups(delete_target_groups_request)



타겟그룹삭제

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
delete_target_groups_request = ncloud_vloadbalancer.DeleteTargetGroupsRequest() # DeleteTargetGroupsRequest | deleteTargetGroupsRequest

try:
    api_response = api_instance.delete_target_groups(delete_target_groups_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_target_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_target_groups_request** | [**DeleteTargetGroupsRequest**](DeleteTargetGroupsRequest.md)| deleteTargetGroupsRequest | 

### Return type

[**DeleteTargetGroupsResponse**](DeleteTargetGroupsResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer_instance_detail**
> GetLoadBalancerInstanceDetailResponse get_load_balancer_instance_detail(get_load_balancer_instance_detail_request)



로드밸런서인스턴스상세조회

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
get_load_balancer_instance_detail_request = ncloud_vloadbalancer.GetLoadBalancerInstanceDetailRequest() # GetLoadBalancerInstanceDetailRequest | getLoadBalancerInstanceDetailRequest

try:
    api_response = api_instance.get_load_balancer_instance_detail(get_load_balancer_instance_detail_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_load_balancer_instance_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_load_balancer_instance_detail_request** | [**GetLoadBalancerInstanceDetailRequest**](GetLoadBalancerInstanceDetailRequest.md)| getLoadBalancerInstanceDetailRequest | 

### Return type

[**GetLoadBalancerInstanceDetailResponse**](GetLoadBalancerInstanceDetailResponse.md)

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
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
get_load_balancer_instance_list_request = ncloud_vloadbalancer.GetLoadBalancerInstanceListRequest() # GetLoadBalancerInstanceListRequest | getLoadBalancerInstanceListRequest

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

# **get_load_balancer_listener_list**
> GetLoadBalancerListenerListResponse get_load_balancer_listener_list(get_load_balancer_listener_list_request)



로드밸런서리스너리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
get_load_balancer_listener_list_request = ncloud_vloadbalancer.GetLoadBalancerListenerListRequest() # GetLoadBalancerListenerListRequest | getLoadBalancerListenerListRequest

try:
    api_response = api_instance.get_load_balancer_listener_list(get_load_balancer_listener_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_load_balancer_listener_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_load_balancer_listener_list_request** | [**GetLoadBalancerListenerListRequest**](GetLoadBalancerListenerListRequest.md)| getLoadBalancerListenerListRequest | 

### Return type

[**GetLoadBalancerListenerListResponse**](GetLoadBalancerListenerListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer_rule_list**
> GetLoadBalancerRuleListResponse get_load_balancer_rule_list(get_load_balancer_rule_list_request)



로드밸런서룰리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
get_load_balancer_rule_list_request = ncloud_vloadbalancer.GetLoadBalancerRuleListRequest() # GetLoadBalancerRuleListRequest | getLoadBalancerRuleListRequest

try:
    api_response = api_instance.get_load_balancer_rule_list(get_load_balancer_rule_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_load_balancer_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_load_balancer_rule_list_request** | [**GetLoadBalancerRuleListRequest**](GetLoadBalancerRuleListRequest.md)| getLoadBalancerRuleListRequest | 

### Return type

[**GetLoadBalancerRuleListResponse**](GetLoadBalancerRuleListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_group_detail**
> GetTargetGroupDetailResponse get_target_group_detail(get_target_group_detail_request)



타겟그룹상세조회

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
get_target_group_detail_request = ncloud_vloadbalancer.GetTargetGroupDetailRequest() # GetTargetGroupDetailRequest | getTargetGroupDetailRequest

try:
    api_response = api_instance.get_target_group_detail(get_target_group_detail_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_target_group_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_target_group_detail_request** | [**GetTargetGroupDetailRequest**](GetTargetGroupDetailRequest.md)| getTargetGroupDetailRequest | 

### Return type

[**GetTargetGroupDetailResponse**](GetTargetGroupDetailResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_group_list**
> GetTargetGroupListResponse get_target_group_list(get_target_group_list_request)



타겟그룹리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
get_target_group_list_request = ncloud_vloadbalancer.GetTargetGroupListRequest() # GetTargetGroupListRequest | getTargetGroupListRequest

try:
    api_response = api_instance.get_target_group_list(get_target_group_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_target_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_target_group_list_request** | [**GetTargetGroupListRequest**](GetTargetGroupListRequest.md)| getTargetGroupListRequest | 

### Return type

[**GetTargetGroupListResponse**](GetTargetGroupListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_list**
> GetTargetListResponse get_target_list(get_target_list_request)



타겟리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
get_target_list_request = ncloud_vloadbalancer.GetTargetListRequest() # GetTargetListRequest | getTargetListRequest

try:
    api_response = api_instance.get_target_list(get_target_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_target_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_target_list_request** | [**GetTargetListRequest**](GetTargetListRequest.md)| getTargetListRequest | 

### Return type

[**GetTargetListResponse**](GetTargetListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_target**
> RemoveTargetResponse remove_target(remove_target_request)



타겟제거

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
remove_target_request = ncloud_vloadbalancer.RemoveTargetRequest() # RemoveTargetRequest | removeTargetRequest

try:
    api_response = api_instance.remove_target(remove_target_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->remove_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_target_request** | [**RemoveTargetRequest**](RemoveTargetRequest.md)| removeTargetRequest | 

### Return type

[**RemoveTargetResponse**](RemoveTargetResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_load_balancer_description**
> SetLoadBalancerDescriptionResponse set_load_balancer_description(set_load_balancer_description_request)



로드밸런서설명설정

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
set_load_balancer_description_request = ncloud_vloadbalancer.SetLoadBalancerDescriptionRequest() # SetLoadBalancerDescriptionRequest | setLoadBalancerDescriptionRequest

try:
    api_response = api_instance.set_load_balancer_description(set_load_balancer_description_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->set_load_balancer_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_load_balancer_description_request** | [**SetLoadBalancerDescriptionRequest**](SetLoadBalancerDescriptionRequest.md)| setLoadBalancerDescriptionRequest | 

### Return type

[**SetLoadBalancerDescriptionResponse**](SetLoadBalancerDescriptionResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_load_balancer_instance_subnet**
> SetLoadBalancerInstanceSubnetResponse set_load_balancer_instance_subnet(set_load_balancer_instance_subnet_request)



로드밸런서인스턴스서브넷설정

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
set_load_balancer_instance_subnet_request = ncloud_vloadbalancer.SetLoadBalancerInstanceSubnetRequest() # SetLoadBalancerInstanceSubnetRequest | setLoadBalancerInstanceSubnetRequest

try:
    api_response = api_instance.set_load_balancer_instance_subnet(set_load_balancer_instance_subnet_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->set_load_balancer_instance_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_load_balancer_instance_subnet_request** | [**SetLoadBalancerInstanceSubnetRequest**](SetLoadBalancerInstanceSubnetRequest.md)| setLoadBalancerInstanceSubnetRequest | 

### Return type

[**SetLoadBalancerInstanceSubnetResponse**](SetLoadBalancerInstanceSubnetResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_target**
> SetTargetResponse set_target(set_target_request)



타겟설정

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
set_target_request = ncloud_vloadbalancer.SetTargetRequest() # SetTargetRequest | setTargetRequest

try:
    api_response = api_instance.set_target(set_target_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->set_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_target_request** | [**SetTargetRequest**](SetTargetRequest.md)| setTargetRequest | 

### Return type

[**SetTargetResponse**](SetTargetResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_target_group_description**
> SetTargetGroupDescriptionResponse set_target_group_description(set_target_group_description_request)



타겟그룹설명설정

### Example
```python
from __future__ import print_function
import ncloud_vloadbalancer
from ncloud_vloadbalancer.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vloadbalancer.V2Api(ncloud_vloadbalancer.ApiClient(configuration))
set_target_group_description_request = ncloud_vloadbalancer.SetTargetGroupDescriptionRequest() # SetTargetGroupDescriptionRequest | setTargetGroupDescriptionRequest

try:
    api_response = api_instance.set_target_group_description(set_target_group_description_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->set_target_group_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_target_group_description_request** | [**SetTargetGroupDescriptionRequest**](SetTargetGroupDescriptionRequest.md)| setTargetGroupDescriptionRequest | 

### Return type

[**SetTargetGroupDescriptionResponse**](SetTargetGroupDescriptionResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

