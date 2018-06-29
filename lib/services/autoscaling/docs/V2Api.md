# ncloud_autoscaling.V2Api

All URIs are relative to *https://ncloud.apigw.ntruss.com/autoscaling/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auto_scaling_group**](V2Api.md#create_auto_scaling_group) | **POST** /createAutoScalingGroup | 
[**create_launch_configuration**](V2Api.md#create_launch_configuration) | **POST** /createLaunchConfiguration | 
[**delete_auto_scaling_group**](V2Api.md#delete_auto_scaling_group) | **POST** /deleteAutoScalingGroup | 
[**delete_auto_scaling_launch_configuration**](V2Api.md#delete_auto_scaling_launch_configuration) | **POST** /deleteAutoScalingLaunchConfiguration | 
[**delete_policy**](V2Api.md#delete_policy) | **POST** /deletePolicy | 
[**delete_scheduled_action**](V2Api.md#delete_scheduled_action) | **POST** /deleteScheduledAction | 
[**execute_policy**](V2Api.md#execute_policy) | **POST** /executePolicy | 
[**get_adjustment_type_list**](V2Api.md#get_adjustment_type_list) | **POST** /getAdjustmentTypeList | 
[**get_auto_scaling_activity_log_list**](V2Api.md#get_auto_scaling_activity_log_list) | **POST** /getAutoScalingActivityLogList | 
[**get_auto_scaling_configuration_log_list**](V2Api.md#get_auto_scaling_configuration_log_list) | **POST** /getAutoScalingConfigurationLogList | 
[**get_auto_scaling_group_list**](V2Api.md#get_auto_scaling_group_list) | **POST** /getAutoScalingGroupList | 
[**get_auto_scaling_policy_list**](V2Api.md#get_auto_scaling_policy_list) | **POST** /getAutoScalingPolicyList | 
[**get_launch_configuration_list**](V2Api.md#get_launch_configuration_list) | **POST** /getLaunchConfigurationList | 
[**get_scaling_process_type_list**](V2Api.md#get_scaling_process_type_list) | **POST** /getScalingProcessTypeList | 
[**get_scheduled_action_list**](V2Api.md#get_scheduled_action_list) | **POST** /getScheduledActionList | 
[**put_scaling_policy**](V2Api.md#put_scaling_policy) | **POST** /putScalingPolicy | 
[**put_scheduled_update_group_action**](V2Api.md#put_scheduled_update_group_action) | **POST** /putScheduledUpdateGroupAction | 
[**resume_processes**](V2Api.md#resume_processes) | **POST** /resumeProcesses | 
[**set_desired_capacity**](V2Api.md#set_desired_capacity) | **POST** /setDesiredCapacity | 
[**set_server_instance_health**](V2Api.md#set_server_instance_health) | **POST** /setServerInstanceHealth | 
[**suspend_processes**](V2Api.md#suspend_processes) | **POST** /suspendProcesses | 
[**terminate_server_instance_in_auto_scaling_group**](V2Api.md#terminate_server_instance_in_auto_scaling_group) | **POST** /terminateServerInstanceInAutoScalingGroup | 
[**update_auto_scaling_group**](V2Api.md#update_auto_scaling_group) | **POST** /updateAutoScalingGroup | 


# **create_auto_scaling_group**
> CreateAutoScalingGroupResponse create_auto_scaling_group(create_auto_scaling_group_request)



B.오토스케일링그룹생성

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
create_auto_scaling_group_request = ncloud_autoscaling.CreateAutoScalingGroupRequest() # CreateAutoScalingGroupRequest | createAutoScalingGroupRequest

try:
    api_response = api_instance.create_auto_scaling_group(create_auto_scaling_group_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_auto_scaling_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_auto_scaling_group_request** | [**CreateAutoScalingGroupRequest**](CreateAutoScalingGroupRequest.md)| createAutoScalingGroupRequest | 

### Return type

[**CreateAutoScalingGroupResponse**](CreateAutoScalingGroupResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_launch_configuration**
> CreateLaunchConfigurationResponse create_launch_configuration(create_launch_configuration_request)



A.론치설정생성

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
create_launch_configuration_request = ncloud_autoscaling.CreateLaunchConfigurationRequest() # CreateLaunchConfigurationRequest | createLaunchConfigurationRequest

try:
    api_response = api_instance.create_launch_configuration(create_launch_configuration_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_launch_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_launch_configuration_request** | [**CreateLaunchConfigurationRequest**](CreateLaunchConfigurationRequest.md)| createLaunchConfigurationRequest | 

### Return type

[**CreateLaunchConfigurationResponse**](CreateLaunchConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auto_scaling_group**
> DeleteAutoScalingGroupResponse delete_auto_scaling_group(delete_auto_scaling_group_request)



B.오토스케일링그룹삭제

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
delete_auto_scaling_group_request = ncloud_autoscaling.DeleteAutoScalingGroupRequest() # DeleteAutoScalingGroupRequest | deleteAutoScalingGroupRequest

try:
    api_response = api_instance.delete_auto_scaling_group(delete_auto_scaling_group_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_auto_scaling_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_auto_scaling_group_request** | [**DeleteAutoScalingGroupRequest**](DeleteAutoScalingGroupRequest.md)| deleteAutoScalingGroupRequest | 

### Return type

[**DeleteAutoScalingGroupResponse**](DeleteAutoScalingGroupResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auto_scaling_launch_configuration**
> DeleteAutoScalingLaunchConfigurationRequest delete_auto_scaling_launch_configuration(delete_auto_scaling_launch_configuration_request)



A.오토스케일링론치설정삭제

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
delete_auto_scaling_launch_configuration_request = ncloud_autoscaling.DeleteAutoScalingLaunchConfigurationRequest() # DeleteAutoScalingLaunchConfigurationRequest | deleteAutoScalingLaunchConfigurationRequest

try:
    api_response = api_instance.delete_auto_scaling_launch_configuration(delete_auto_scaling_launch_configuration_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_auto_scaling_launch_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_auto_scaling_launch_configuration_request** | [**DeleteAutoScalingLaunchConfigurationRequest**](DeleteAutoScalingLaunchConfigurationRequest.md)| deleteAutoScalingLaunchConfigurationRequest | 

### Return type

[**DeleteAutoScalingLaunchConfigurationRequest**](DeleteAutoScalingLaunchConfigurationRequest.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> DeletePolicyResponse delete_policy(delete_policy_request)



F.스케일링정책삭제

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
delete_policy_request = ncloud_autoscaling.DeletePolicyRequest() # DeletePolicyRequest | deletePolicyRequest

try:
    api_response = api_instance.delete_policy(delete_policy_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_policy_request** | [**DeletePolicyRequest**](DeletePolicyRequest.md)| deletePolicyRequest | 

### Return type

[**DeletePolicyResponse**](DeletePolicyResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_action**
> DeleteScheduledActionResponse delete_scheduled_action(delete_scheduled_action_request)



C.스케쥴액션삭제

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
delete_scheduled_action_request = ncloud_autoscaling.DeleteScheduledActionRequest() # DeleteScheduledActionRequest | deleteScheduledActionRequest

try:
    api_response = api_instance.delete_scheduled_action(delete_scheduled_action_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_scheduled_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_scheduled_action_request** | [**DeleteScheduledActionRequest**](DeleteScheduledActionRequest.md)| deleteScheduledActionRequest | 

### Return type

[**DeleteScheduledActionResponse**](DeleteScheduledActionResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_policy**
> ExecutePolicyResponse execute_policy(execute_policy_request)



F.스케일링정책수행

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
execute_policy_request = ncloud_autoscaling.ExecutePolicyRequest() # ExecutePolicyRequest | executePolicyRequest

try:
    api_response = api_instance.execute_policy(execute_policy_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->execute_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execute_policy_request** | [**ExecutePolicyRequest**](ExecutePolicyRequest.md)| executePolicyRequest | 

### Return type

[**ExecutePolicyResponse**](ExecutePolicyResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_adjustment_type_list**
> GetAdjustmentTypeListResponse get_adjustment_type_list(get_adjustment_type_list_request)



F.조정유형리스트조회

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
get_adjustment_type_list_request = ncloud_autoscaling.GetAdjustmentTypeListRequest() # GetAdjustmentTypeListRequest | getAdjustmentTypeListRequest

try:
    api_response = api_instance.get_adjustment_type_list(get_adjustment_type_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_adjustment_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_adjustment_type_list_request** | [**GetAdjustmentTypeListRequest**](GetAdjustmentTypeListRequest.md)| getAdjustmentTypeListRequest | 

### Return type

[**GetAdjustmentTypeListResponse**](GetAdjustmentTypeListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_scaling_activity_log_list**
> GetAutoScalingActivityLogListResponse get_auto_scaling_activity_log_list(get_auto_scaling_activity_log_list_request)



E.액티비티로그리스트조회

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
get_auto_scaling_activity_log_list_request = ncloud_autoscaling.GetAutoScalingActivityLogListRequest() # GetAutoScalingActivityLogListRequest | getAutoScalingActivityLogListRequest

try:
    api_response = api_instance.get_auto_scaling_activity_log_list(get_auto_scaling_activity_log_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_auto_scaling_activity_log_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_auto_scaling_activity_log_list_request** | [**GetAutoScalingActivityLogListRequest**](GetAutoScalingActivityLogListRequest.md)| getAutoScalingActivityLogListRequest | 

### Return type

[**GetAutoScalingActivityLogListResponse**](GetAutoScalingActivityLogListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_scaling_configuration_log_list**
> GetAutoScalingConfigurationLogListResponse get_auto_scaling_configuration_log_list(get_auto_scaling_configuration_log_list_request)



E.오토스케일링설정로그리스트조회

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
get_auto_scaling_configuration_log_list_request = ncloud_autoscaling.GetAutoScalingConfigurationLogListRequest() # GetAutoScalingConfigurationLogListRequest | getAutoScalingConfigurationLogListRequest

try:
    api_response = api_instance.get_auto_scaling_configuration_log_list(get_auto_scaling_configuration_log_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_auto_scaling_configuration_log_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_auto_scaling_configuration_log_list_request** | [**GetAutoScalingConfigurationLogListRequest**](GetAutoScalingConfigurationLogListRequest.md)| getAutoScalingConfigurationLogListRequest | 

### Return type

[**GetAutoScalingConfigurationLogListResponse**](GetAutoScalingConfigurationLogListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_scaling_group_list**
> GetAutoScalingGroupListResponse get_auto_scaling_group_list(get_auto_scaling_group_list_request)



B.오토스케일링그룹리스트조회

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
get_auto_scaling_group_list_request = ncloud_autoscaling.GetAutoScalingGroupListRequest() # GetAutoScalingGroupListRequest | getAutoScalingGroupListRequest

try:
    api_response = api_instance.get_auto_scaling_group_list(get_auto_scaling_group_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_auto_scaling_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_auto_scaling_group_list_request** | [**GetAutoScalingGroupListRequest**](GetAutoScalingGroupListRequest.md)| getAutoScalingGroupListRequest | 

### Return type

[**GetAutoScalingGroupListResponse**](GetAutoScalingGroupListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_scaling_policy_list**
> GetAutoScalingPolicyListResponse get_auto_scaling_policy_list(get_auto_scaling_policy_list_request)



F.오토스케일링정책리스트조회

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
get_auto_scaling_policy_list_request = ncloud_autoscaling.GetAutoScalingPolicyListRequest() # GetAutoScalingPolicyListRequest | getAutoScalingPolicyListRequest

try:
    api_response = api_instance.get_auto_scaling_policy_list(get_auto_scaling_policy_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_auto_scaling_policy_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_auto_scaling_policy_list_request** | [**GetAutoScalingPolicyListRequest**](GetAutoScalingPolicyListRequest.md)| getAutoScalingPolicyListRequest | 

### Return type

[**GetAutoScalingPolicyListResponse**](GetAutoScalingPolicyListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_launch_configuration_list**
> GetLaunchConfigurationListResponse get_launch_configuration_list(get_launch_configuration_list_request)



A.론치설정리스트조회

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
get_launch_configuration_list_request = ncloud_autoscaling.GetLaunchConfigurationListRequest() # GetLaunchConfigurationListRequest | getLaunchConfigurationListRequest

try:
    api_response = api_instance.get_launch_configuration_list(get_launch_configuration_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_launch_configuration_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_launch_configuration_list_request** | [**GetLaunchConfigurationListRequest**](GetLaunchConfigurationListRequest.md)| getLaunchConfigurationListRequest | 

### Return type

[**GetLaunchConfigurationListResponse**](GetLaunchConfigurationListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scaling_process_type_list**
> GetScalingProcessTypeListResponse get_scaling_process_type_list(get_scaling_process_type_list_request)



D.프로세스구분리스트조회

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
get_scaling_process_type_list_request = ncloud_autoscaling.GetScalingProcessTypeListRequest() # GetScalingProcessTypeListRequest | getScalingProcessTypeListRequest

try:
    api_response = api_instance.get_scaling_process_type_list(get_scaling_process_type_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_scaling_process_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_scaling_process_type_list_request** | [**GetScalingProcessTypeListRequest**](GetScalingProcessTypeListRequest.md)| getScalingProcessTypeListRequest | 

### Return type

[**GetScalingProcessTypeListResponse**](GetScalingProcessTypeListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_action_list**
> GetScheduledActionListResponse get_scheduled_action_list(get_scheduled_action_list_request)



C.스케쥴액션리스트조회

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
get_scheduled_action_list_request = ncloud_autoscaling.GetScheduledActionListRequest() # GetScheduledActionListRequest | getScheduledActionListRequest

try:
    api_response = api_instance.get_scheduled_action_list(get_scheduled_action_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_scheduled_action_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_scheduled_action_list_request** | [**GetScheduledActionListRequest**](GetScheduledActionListRequest.md)| getScheduledActionListRequest | 

### Return type

[**GetScheduledActionListResponse**](GetScheduledActionListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_scaling_policy**
> PutScalingPolicyResponse put_scaling_policy(put_scaling_policy_request)



F.스케일링정책생성/변경

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
put_scaling_policy_request = ncloud_autoscaling.PutScalingPolicyRequest() # PutScalingPolicyRequest | putScalingPolicyRequest

try:
    api_response = api_instance.put_scaling_policy(put_scaling_policy_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->put_scaling_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_scaling_policy_request** | [**PutScalingPolicyRequest**](PutScalingPolicyRequest.md)| putScalingPolicyRequest | 

### Return type

[**PutScalingPolicyResponse**](PutScalingPolicyResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_scheduled_update_group_action**
> PutScheduledUpdateGroupActionResponse put_scheduled_update_group_action(put_scheduled_update_group_action_request)



C.스케쥴액션생성|수정

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
put_scheduled_update_group_action_request = ncloud_autoscaling.PutScheduledUpdateGroupActionRequest() # PutScheduledUpdateGroupActionRequest | putScheduledUpdateGroupActionRequest

try:
    api_response = api_instance.put_scheduled_update_group_action(put_scheduled_update_group_action_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->put_scheduled_update_group_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_scheduled_update_group_action_request** | [**PutScheduledUpdateGroupActionRequest**](PutScheduledUpdateGroupActionRequest.md)| putScheduledUpdateGroupActionRequest | 

### Return type

[**PutScheduledUpdateGroupActionResponse**](PutScheduledUpdateGroupActionResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_processes**
> ResumeProcessesResponse resume_processes(resume_processes_request)



D.프로세스재개

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
resume_processes_request = ncloud_autoscaling.ResumeProcessesRequest() # ResumeProcessesRequest | resumeProcessesRequest

try:
    api_response = api_instance.resume_processes(resume_processes_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->resume_processes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resume_processes_request** | [**ResumeProcessesRequest**](ResumeProcessesRequest.md)| resumeProcessesRequest | 

### Return type

[**ResumeProcessesResponse**](ResumeProcessesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_desired_capacity**
> SetDesiredCapacityResponse set_desired_capacity(set_desired_capacity_request)



B.기대용량치갱신

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
set_desired_capacity_request = ncloud_autoscaling.SetDesiredCapacityRequest() # SetDesiredCapacityRequest | setDesiredCapacityRequest

try:
    api_response = api_instance.set_desired_capacity(set_desired_capacity_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->set_desired_capacity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_desired_capacity_request** | [**SetDesiredCapacityRequest**](SetDesiredCapacityRequest.md)| setDesiredCapacityRequest | 

### Return type

[**SetDesiredCapacityResponse**](SetDesiredCapacityResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_server_instance_health**
> SetServerInstanceHealthResponse set_server_instance_health(set_server_instance_health_request)



B.서버인스턴스헬스상태갱신

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
set_server_instance_health_request = ncloud_autoscaling.SetServerInstanceHealthRequest() # SetServerInstanceHealthRequest | setServerInstanceHealthRequest

try:
    api_response = api_instance.set_server_instance_health(set_server_instance_health_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->set_server_instance_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_server_instance_health_request** | [**SetServerInstanceHealthRequest**](SetServerInstanceHealthRequest.md)| setServerInstanceHealthRequest | 

### Return type

[**SetServerInstanceHealthResponse**](SetServerInstanceHealthResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_processes**
> SuspendProcessesResponse suspend_processes(suspend_processes_request)



D.프로세스보류

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
suspend_processes_request = ncloud_autoscaling.SuspendProcessesRequest() # SuspendProcessesRequest | suspendProcessesRequest

try:
    api_response = api_instance.suspend_processes(suspend_processes_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->suspend_processes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suspend_processes_request** | [**SuspendProcessesRequest**](SuspendProcessesRequest.md)| suspendProcessesRequest | 

### Return type

[**SuspendProcessesResponse**](SuspendProcessesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_server_instance_in_auto_scaling_group**
> TerminateServerInstanceInAutoScalingGroupResponse terminate_server_instance_in_auto_scaling_group(terminate_server_instance_in_auto_scaling_group_request)



B.오토스케일링그룹에속한서버인스턴스삭제

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
terminate_server_instance_in_auto_scaling_group_request = ncloud_autoscaling.TerminateServerInstanceInAutoScalingGroupRequest() # TerminateServerInstanceInAutoScalingGroupRequest | terminateServerInstanceInAutoScalingGroupRequest

try:
    api_response = api_instance.terminate_server_instance_in_auto_scaling_group(terminate_server_instance_in_auto_scaling_group_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->terminate_server_instance_in_auto_scaling_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminate_server_instance_in_auto_scaling_group_request** | [**TerminateServerInstanceInAutoScalingGroupRequest**](TerminateServerInstanceInAutoScalingGroupRequest.md)| terminateServerInstanceInAutoScalingGroupRequest | 

### Return type

[**TerminateServerInstanceInAutoScalingGroupResponse**](TerminateServerInstanceInAutoScalingGroupResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_scaling_group**
> UpdateAutoScalingGroupResponse update_auto_scaling_group(update_auto_scaling_group_request)



B.오토스케일링그룹수정

### Example
```python
from __future__ import print_function
import ncloud_autoscaling
from ncloud_autoscaling.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_autoscaling.V2Api(ncloud_autoscaling.ApiClient(configuration))
update_auto_scaling_group_request = ncloud_autoscaling.UpdateAutoScalingGroupRequest() # UpdateAutoScalingGroupRequest | updateAutoScalingGroupRequest

try:
    api_response = api_instance.update_auto_scaling_group(update_auto_scaling_group_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->update_auto_scaling_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_auto_scaling_group_request** | [**UpdateAutoScalingGroupRequest**](UpdateAutoScalingGroupRequest.md)| updateAutoScalingGroupRequest | 

### Return type

[**UpdateAutoScalingGroupResponse**](UpdateAutoScalingGroupResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

