# ncloud_server.V2Api

All URIs are relative to *https://ncloud.apigw.ntruss.com/server/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_nas_volume_access_control**](V2Api.md#add_nas_volume_access_control) | **POST** /addNasVolumeAccessControl | 
[**add_port_forwarding_rules**](V2Api.md#add_port_forwarding_rules) | **POST** /addPortForwardingRules | 
[**associate_public_ip_with_server_instance**](V2Api.md#associate_public_ip_with_server_instance) | **POST** /associatePublicIpWithServerInstance | 
[**change_nas_volume_size**](V2Api.md#change_nas_volume_size) | **POST** /changeNasVolumeSize | 
[**change_server_instance_spec**](V2Api.md#change_server_instance_spec) | **POST** /changeServerInstanceSpec | 
[**create_block_storage_instance**](V2Api.md#create_block_storage_instance) | **POST** /createBlockStorageInstance | 
[**create_login_key**](V2Api.md#create_login_key) | **POST** /createLoginKey | 
[**create_member_server_image**](V2Api.md#create_member_server_image) | **POST** /createMemberServerImage | 
[**create_nas_volume_instance**](V2Api.md#create_nas_volume_instance) | **POST** /createNasVolumeInstance | 
[**create_public_ip_instance**](V2Api.md#create_public_ip_instance) | **POST** /createPublicIpInstance | 
[**create_server_instances**](V2Api.md#create_server_instances) | **POST** /createServerInstances | 
[**delete_block_storage_instances**](V2Api.md#delete_block_storage_instances) | **POST** /deleteBlockStorageInstances | 
[**delete_login_key**](V2Api.md#delete_login_key) | **POST** /deleteLoginKey | 
[**delete_member_server_images**](V2Api.md#delete_member_server_images) | **POST** /deleteMemberServerImages | 
[**delete_nas_volume_instance**](V2Api.md#delete_nas_volume_instance) | **POST** /deleteNasVolumeInstance | 
[**delete_port_forwarding_rules**](V2Api.md#delete_port_forwarding_rules) | **POST** /deletePortForwardingRules | 
[**delete_public_ip_instances**](V2Api.md#delete_public_ip_instances) | **POST** /deletePublicIpInstances | 
[**disassociate_public_ip_from_server_instance**](V2Api.md#disassociate_public_ip_from_server_instance) | **POST** /disassociatePublicIpFromServerInstance | 
[**get_access_control_group_list**](V2Api.md#get_access_control_group_list) | **POST** /getAccessControlGroupList | 
[**get_access_control_group_server_instance_list**](V2Api.md#get_access_control_group_server_instance_list) | **POST** /getAccessControlGroupServerInstanceList | 
[**get_access_control_rule_list**](V2Api.md#get_access_control_rule_list) | **POST** /getAccessControlRuleList | 
[**get_block_storage_instance_list**](V2Api.md#get_block_storage_instance_list) | **POST** /getBlockStorageInstanceList | 
[**get_block_storage_snapshot_instance_list**](V2Api.md#get_block_storage_snapshot_instance_list) | **POST** /getBlockStorageSnapshotInstanceList | 
[**get_login_key_list**](V2Api.md#get_login_key_list) | **POST** /getLoginKeyList | 
[**get_member_server_image_list**](V2Api.md#get_member_server_image_list) | **POST** /getMemberServerImageList | 
[**get_nas_volume_instance_list**](V2Api.md#get_nas_volume_instance_list) | **POST** /getNasVolumeInstanceList | 
[**get_nas_volume_instance_rating_list**](V2Api.md#get_nas_volume_instance_rating_list) | **POST** /getNasVolumeInstanceRatingList | 
[**get_port_forwarding_rule_list**](V2Api.md#get_port_forwarding_rule_list) | **POST** /getPortForwardingRuleList | 
[**get_public_ip_instance_list**](V2Api.md#get_public_ip_instance_list) | **POST** /getPublicIpInstanceList | 
[**get_public_ip_target_server_instance_list**](V2Api.md#get_public_ip_target_server_instance_list) | **POST** /getPublicIpTargetServerInstanceList | 
[**get_raid_list**](V2Api.md#get_raid_list) | **POST** /getRaidList | 
[**get_region_list**](V2Api.md#get_region_list) | **POST** /getRegionList | 
[**get_root_password**](V2Api.md#get_root_password) | **POST** /getRootPassword | 
[**get_server_image_product_list**](V2Api.md#get_server_image_product_list) | **POST** /getServerImageProductList | 
[**get_server_instance_list**](V2Api.md#get_server_instance_list) | **POST** /getServerInstanceList | 
[**get_server_product_list**](V2Api.md#get_server_product_list) | **POST** /getServerProductList | 
[**get_zone_list**](V2Api.md#get_zone_list) | **POST** /getZoneList | 
[**reboot_server_instances**](V2Api.md#reboot_server_instances) | **POST** /rebootServerInstances | 
[**recreate_server_instance**](V2Api.md#recreate_server_instance) | **POST** /recreateServerInstance | 
[**remove_nas_volume_access_control**](V2Api.md#remove_nas_volume_access_control) | **POST** /removeNasVolumeAccessControl | 
[**set_nas_volume_access_control**](V2Api.md#set_nas_volume_access_control) | **POST** /setNasVolumeAccessControl | 
[**start_server_instances**](V2Api.md#start_server_instances) | **POST** /startServerInstances | 
[**stop_server_instances**](V2Api.md#stop_server_instances) | **POST** /stopServerInstances | 
[**terminate_server_instances**](V2Api.md#terminate_server_instances) | **POST** /terminateServerInstances | 


# **add_nas_volume_access_control**
> AddNasVolumeAccessControlResponse add_nas_volume_access_control(add_nas_volume_access_control_request)



NAS볼륨인스턴스접근제어추가

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
add_nas_volume_access_control_request = ncloud_server.AddNasVolumeAccessControlRequest() # AddNasVolumeAccessControlRequest | addNasVolumeAccessControlRequest

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

# **add_port_forwarding_rules**
> AddPortForwardingRulesResponse add_port_forwarding_rules(add_port_forwarding_rules_request)



포트포워딩Rule추가

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
add_port_forwarding_rules_request = ncloud_server.AddPortForwardingRulesRequest() # AddPortForwardingRulesRequest | addPortForwardingRulesRequest

try:
    api_response = api_instance.add_port_forwarding_rules(add_port_forwarding_rules_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->add_port_forwarding_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_port_forwarding_rules_request** | [**AddPortForwardingRulesRequest**](AddPortForwardingRulesRequest.md)| addPortForwardingRulesRequest | 

### Return type

[**AddPortForwardingRulesResponse**](AddPortForwardingRulesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **associate_public_ip_with_server_instance**
> AssociatePublicIpWithServerInstanceResponse associate_public_ip_with_server_instance(associate_public_ip_with_server_instance_request)



공인IP를서버인스턴스에할당

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
associate_public_ip_with_server_instance_request = ncloud_server.AssociatePublicIpWithServerInstanceRequest() # AssociatePublicIpWithServerInstanceRequest | associatePublicIpWithServerInstanceRequest

try:
    api_response = api_instance.associate_public_ip_with_server_instance(associate_public_ip_with_server_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->associate_public_ip_with_server_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **associate_public_ip_with_server_instance_request** | [**AssociatePublicIpWithServerInstanceRequest**](AssociatePublicIpWithServerInstanceRequest.md)| associatePublicIpWithServerInstanceRequest | 

### Return type

[**AssociatePublicIpWithServerInstanceResponse**](AssociatePublicIpWithServerInstanceResponse.md)

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
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
change_nas_volume_size_request = ncloud_server.ChangeNasVolumeSizeRequest() # ChangeNasVolumeSizeRequest | changeNasVolumeSizeRequest

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

# **change_server_instance_spec**
> ChangeServerInstanceSpecResponse change_server_instance_spec(change_server_instance_spec_request)



서버인스턴스스팩변경

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
change_server_instance_spec_request = ncloud_server.ChangeServerInstanceSpecRequest() # ChangeServerInstanceSpecRequest | changeServerInstanceSpecRequest

try:
    api_response = api_instance.change_server_instance_spec(change_server_instance_spec_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->change_server_instance_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_server_instance_spec_request** | [**ChangeServerInstanceSpecRequest**](ChangeServerInstanceSpecRequest.md)| changeServerInstanceSpecRequest | 

### Return type

[**ChangeServerInstanceSpecResponse**](ChangeServerInstanceSpecResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_block_storage_instance**
> CreateBlockStorageInstanceResponse create_block_storage_instance(create_block_storage_instance_request)



블록스토리지인스턴스생성

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
create_block_storage_instance_request = ncloud_server.CreateBlockStorageInstanceRequest() # CreateBlockStorageInstanceRequest | createBlockStorageInstanceRequest

try:
    api_response = api_instance.create_block_storage_instance(create_block_storage_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_block_storage_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_block_storage_instance_request** | [**CreateBlockStorageInstanceRequest**](CreateBlockStorageInstanceRequest.md)| createBlockStorageInstanceRequest | 

### Return type

[**CreateBlockStorageInstanceResponse**](CreateBlockStorageInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_login_key**
> CreateLoginKeyResponse create_login_key(create_login_key_request)



로그인키생성

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
create_login_key_request = ncloud_server.CreateLoginKeyRequest() # CreateLoginKeyRequest | createLoginKeyRequest

try:
    api_response = api_instance.create_login_key(create_login_key_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_login_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_login_key_request** | [**CreateLoginKeyRequest**](CreateLoginKeyRequest.md)| createLoginKeyRequest | 

### Return type

[**CreateLoginKeyResponse**](CreateLoginKeyResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_member_server_image**
> CreateMemberServerImageResponse create_member_server_image(create_member_server_image_request)



회원서버이미지생성

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
create_member_server_image_request = ncloud_server.CreateMemberServerImageRequest() # CreateMemberServerImageRequest | createMemberServerImageRequest

try:
    api_response = api_instance.create_member_server_image(create_member_server_image_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_member_server_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_member_server_image_request** | [**CreateMemberServerImageRequest**](CreateMemberServerImageRequest.md)| createMemberServerImageRequest | 

### Return type

[**CreateMemberServerImageResponse**](CreateMemberServerImageResponse.md)

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
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
create_nas_volume_instance_request = ncloud_server.CreateNasVolumeInstanceRequest() # CreateNasVolumeInstanceRequest | createNasVolumeInstanceRequest

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

# **create_public_ip_instance**
> CreatePublicIpInstanceResponse create_public_ip_instance(create_public_ip_instance_request)



공인IP인스턴스생성

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
create_public_ip_instance_request = ncloud_server.CreatePublicIpInstanceRequest() # CreatePublicIpInstanceRequest | createPublicIpInstanceRequest

try:
    api_response = api_instance.create_public_ip_instance(create_public_ip_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_public_ip_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_public_ip_instance_request** | [**CreatePublicIpInstanceRequest**](CreatePublicIpInstanceRequest.md)| createPublicIpInstanceRequest | 

### Return type

[**CreatePublicIpInstanceResponse**](CreatePublicIpInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_server_instances**
> CreateServerInstancesResponse create_server_instances(create_server_instances_request)



서버인스턴스생성

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
create_server_instances_request = ncloud_server.CreateServerInstancesRequest() # CreateServerInstancesRequest | createServerInstancesRequest

try:
    api_response = api_instance.create_server_instances(create_server_instances_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_server_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_server_instances_request** | [**CreateServerInstancesRequest**](CreateServerInstancesRequest.md)| createServerInstancesRequest | 

### Return type

[**CreateServerInstancesResponse**](CreateServerInstancesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_block_storage_instances**
> DeleteBlockStorageInstancesResponse delete_block_storage_instances(delete_block_storage_instances_request)



블록스토리지인스턴스삭제

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
delete_block_storage_instances_request = ncloud_server.DeleteBlockStorageInstancesRequest() # DeleteBlockStorageInstancesRequest | deleteBlockStorageInstancesRequest

try:
    api_response = api_instance.delete_block_storage_instances(delete_block_storage_instances_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_block_storage_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_block_storage_instances_request** | [**DeleteBlockStorageInstancesRequest**](DeleteBlockStorageInstancesRequest.md)| deleteBlockStorageInstancesRequest | 

### Return type

[**DeleteBlockStorageInstancesResponse**](DeleteBlockStorageInstancesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_login_key**
> DeleteLoginKeyResponse delete_login_key(delete_login_key_request)



로그인키삭제

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
delete_login_key_request = ncloud_server.DeleteLoginKeyRequest() # DeleteLoginKeyRequest | deleteLoginKeyRequest

try:
    api_response = api_instance.delete_login_key(delete_login_key_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_login_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_login_key_request** | [**DeleteLoginKeyRequest**](DeleteLoginKeyRequest.md)| deleteLoginKeyRequest | 

### Return type

[**DeleteLoginKeyResponse**](DeleteLoginKeyResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_member_server_images**
> DeleteMemberServerImagesResponse delete_member_server_images(delete_member_server_images_request)



회원서버이미지삭제

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
delete_member_server_images_request = ncloud_server.DeleteMemberServerImagesRequest() # DeleteMemberServerImagesRequest | deleteMemberServerImagesRequest

try:
    api_response = api_instance.delete_member_server_images(delete_member_server_images_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_member_server_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_member_server_images_request** | [**DeleteMemberServerImagesRequest**](DeleteMemberServerImagesRequest.md)| deleteMemberServerImagesRequest | 

### Return type

[**DeleteMemberServerImagesResponse**](DeleteMemberServerImagesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nas_volume_instance**
> DeleteNasVolumeInstanceResponse delete_nas_volume_instance(delete_nas_volume_instance_request)



NAS볼륨인스턴스삭제

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
delete_nas_volume_instance_request = ncloud_server.DeleteNasVolumeInstanceRequest() # DeleteNasVolumeInstanceRequest | deleteNasVolumeInstanceRequest

try:
    api_response = api_instance.delete_nas_volume_instance(delete_nas_volume_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_nas_volume_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_nas_volume_instance_request** | [**DeleteNasVolumeInstanceRequest**](DeleteNasVolumeInstanceRequest.md)| deleteNasVolumeInstanceRequest | 

### Return type

[**DeleteNasVolumeInstanceResponse**](DeleteNasVolumeInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_port_forwarding_rules**
> DeletePortForwardingRulesResponse delete_port_forwarding_rules(delete_port_forwarding_rules_request)



포트포워딩Rule삭제

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
delete_port_forwarding_rules_request = ncloud_server.DeletePortForwardingRulesRequest() # DeletePortForwardingRulesRequest | deletePortForwardingRulesRequest

try:
    api_response = api_instance.delete_port_forwarding_rules(delete_port_forwarding_rules_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_port_forwarding_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_port_forwarding_rules_request** | [**DeletePortForwardingRulesRequest**](DeletePortForwardingRulesRequest.md)| deletePortForwardingRulesRequest | 

### Return type

[**DeletePortForwardingRulesResponse**](DeletePortForwardingRulesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_public_ip_instances**
> DeletePublicIpInstancesResponse delete_public_ip_instances(delete_public_ip_instances_request)



공인IP인스턴스삭제

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
delete_public_ip_instances_request = ncloud_server.DeletePublicIpInstancesRequest() # DeletePublicIpInstancesRequest | deletePublicIpInstancesRequest

try:
    api_response = api_instance.delete_public_ip_instances(delete_public_ip_instances_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_public_ip_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_public_ip_instances_request** | [**DeletePublicIpInstancesRequest**](DeletePublicIpInstancesRequest.md)| deletePublicIpInstancesRequest | 

### Return type

[**DeletePublicIpInstancesResponse**](DeletePublicIpInstancesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disassociate_public_ip_from_server_instance**
> DisassociatePublicIpFromServerInstanceResponse disassociate_public_ip_from_server_instance(disassociate_public_ip_from_server_instance_request)



공인IP를서버인스턴스에할당해제

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
disassociate_public_ip_from_server_instance_request = ncloud_server.DisassociatePublicIpFromServerInstanceRequest() # DisassociatePublicIpFromServerInstanceRequest | disassociatePublicIpFromServerInstanceRequest

try:
    api_response = api_instance.disassociate_public_ip_from_server_instance(disassociate_public_ip_from_server_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->disassociate_public_ip_from_server_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disassociate_public_ip_from_server_instance_request** | [**DisassociatePublicIpFromServerInstanceRequest**](DisassociatePublicIpFromServerInstanceRequest.md)| disassociatePublicIpFromServerInstanceRequest | 

### Return type

[**DisassociatePublicIpFromServerInstanceResponse**](DisassociatePublicIpFromServerInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_control_group_list**
> GetAccessControlGroupListResponse get_access_control_group_list(get_access_control_group_list_request)



접근제어그룹리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_access_control_group_list_request = ncloud_server.GetAccessControlGroupListRequest() # GetAccessControlGroupListRequest | getAccessControlGroupListRequest

try:
    api_response = api_instance.get_access_control_group_list(get_access_control_group_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_access_control_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_access_control_group_list_request** | [**GetAccessControlGroupListRequest**](GetAccessControlGroupListRequest.md)| getAccessControlGroupListRequest | 

### Return type

[**GetAccessControlGroupListResponse**](GetAccessControlGroupListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_control_group_server_instance_list**
> GetAccessControlGroupServerInstanceListResponse get_access_control_group_server_instance_list(get_access_control_group_server_instance_list_request)



접근제어그룹적용된서버인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_access_control_group_server_instance_list_request = ncloud_server.GetAccessControlGroupServerInstanceListRequest() # GetAccessControlGroupServerInstanceListRequest | getAccessControlGroupServerInstanceListRequest

try:
    api_response = api_instance.get_access_control_group_server_instance_list(get_access_control_group_server_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_access_control_group_server_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_access_control_group_server_instance_list_request** | [**GetAccessControlGroupServerInstanceListRequest**](GetAccessControlGroupServerInstanceListRequest.md)| getAccessControlGroupServerInstanceListRequest | 

### Return type

[**GetAccessControlGroupServerInstanceListResponse**](GetAccessControlGroupServerInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_control_rule_list**
> GetAccessControlRuleListResponse get_access_control_rule_list(get_access_control_rule_list_request)



접근제어규칙리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_access_control_rule_list_request = ncloud_server.GetAccessControlRuleListRequest() # GetAccessControlRuleListRequest | getAccessControlRuleListRequest

try:
    api_response = api_instance.get_access_control_rule_list(get_access_control_rule_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_access_control_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_access_control_rule_list_request** | [**GetAccessControlRuleListRequest**](GetAccessControlRuleListRequest.md)| getAccessControlRuleListRequest | 

### Return type

[**GetAccessControlRuleListResponse**](GetAccessControlRuleListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_storage_instance_list**
> GetBlockStorageInstanceListResponse get_block_storage_instance_list(get_block_storage_instance_list_request)



블록스토리지인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_block_storage_instance_list_request = ncloud_server.GetBlockStorageInstanceListRequest() # GetBlockStorageInstanceListRequest | getBlockStorageInstanceListRequest

try:
    api_response = api_instance.get_block_storage_instance_list(get_block_storage_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_block_storage_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_block_storage_instance_list_request** | [**GetBlockStorageInstanceListRequest**](GetBlockStorageInstanceListRequest.md)| getBlockStorageInstanceListRequest | 

### Return type

[**GetBlockStorageInstanceListResponse**](GetBlockStorageInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_storage_snapshot_instance_list**
> GetBlockStorageSnapshotInstanceListResponse get_block_storage_snapshot_instance_list(get_block_storage_snapshot_instance_list_request)



블록스토리지스냅샷인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_block_storage_snapshot_instance_list_request = ncloud_server.GetBlockStorageSnapshotInstanceListRequest() # GetBlockStorageSnapshotInstanceListRequest | getBlockStorageSnapshotInstanceListRequest

try:
    api_response = api_instance.get_block_storage_snapshot_instance_list(get_block_storage_snapshot_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_block_storage_snapshot_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_block_storage_snapshot_instance_list_request** | [**GetBlockStorageSnapshotInstanceListRequest**](GetBlockStorageSnapshotInstanceListRequest.md)| getBlockStorageSnapshotInstanceListRequest | 

### Return type

[**GetBlockStorageSnapshotInstanceListResponse**](GetBlockStorageSnapshotInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_key_list**
> GetLoginKeyListResponse get_login_key_list(get_login_key_list_request)



로그인키리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_login_key_list_request = ncloud_server.GetLoginKeyListRequest() # GetLoginKeyListRequest | getLoginKeyListRequest

try:
    api_response = api_instance.get_login_key_list(get_login_key_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_login_key_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_login_key_list_request** | [**GetLoginKeyListRequest**](GetLoginKeyListRequest.md)| getLoginKeyListRequest | 

### Return type

[**GetLoginKeyListResponse**](GetLoginKeyListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member_server_image_list**
> GetMemberServerImageListResponse get_member_server_image_list(get_member_server_image_list_request)



회원서버이미지리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_member_server_image_list_request = ncloud_server.GetMemberServerImageListRequest() # GetMemberServerImageListRequest | getMemberServerImageListRequest

try:
    api_response = api_instance.get_member_server_image_list(get_member_server_image_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_member_server_image_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_member_server_image_list_request** | [**GetMemberServerImageListRequest**](GetMemberServerImageListRequest.md)| getMemberServerImageListRequest | 

### Return type

[**GetMemberServerImageListResponse**](GetMemberServerImageListResponse.md)

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
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_nas_volume_instance_list_request = ncloud_server.GetNasVolumeInstanceListRequest() # GetNasVolumeInstanceListRequest | getNasVolumeInstanceListRequest

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

# **get_nas_volume_instance_rating_list**
> GetNasVolumeInstanceRatingListResponse get_nas_volume_instance_rating_list(get_nas_volume_instance_rating_list_request)



NAS볼륨인스턴스측정리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_nas_volume_instance_rating_list_request = ncloud_server.GetNasVolumeInstanceRatingListRequest() # GetNasVolumeInstanceRatingListRequest | getNasVolumeInstanceRatingListRequest

try:
    api_response = api_instance.get_nas_volume_instance_rating_list(get_nas_volume_instance_rating_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_nas_volume_instance_rating_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_nas_volume_instance_rating_list_request** | [**GetNasVolumeInstanceRatingListRequest**](GetNasVolumeInstanceRatingListRequest.md)| getNasVolumeInstanceRatingListRequest | 

### Return type

[**GetNasVolumeInstanceRatingListResponse**](GetNasVolumeInstanceRatingListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_forwarding_rule_list**
> GetPortForwardingRuleListResponse get_port_forwarding_rule_list(get_port_forwarding_rule_list_request)



포트포워딩Rule리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_port_forwarding_rule_list_request = ncloud_server.GetPortForwardingRuleListRequest() # GetPortForwardingRuleListRequest | getPortForwardingRuleListRequest

try:
    api_response = api_instance.get_port_forwarding_rule_list(get_port_forwarding_rule_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_port_forwarding_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_port_forwarding_rule_list_request** | [**GetPortForwardingRuleListRequest**](GetPortForwardingRuleListRequest.md)| getPortForwardingRuleListRequest | 

### Return type

[**GetPortForwardingRuleListResponse**](GetPortForwardingRuleListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_ip_instance_list**
> GetPublicIpInstanceListResponse get_public_ip_instance_list(get_public_ip_instance_list_request)



공인IP인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_public_ip_instance_list_request = ncloud_server.GetPublicIpInstanceListRequest() # GetPublicIpInstanceListRequest | getPublicIpInstanceListRequest

try:
    api_response = api_instance.get_public_ip_instance_list(get_public_ip_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_public_ip_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_public_ip_instance_list_request** | [**GetPublicIpInstanceListRequest**](GetPublicIpInstanceListRequest.md)| getPublicIpInstanceListRequest | 

### Return type

[**GetPublicIpInstanceListResponse**](GetPublicIpInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_ip_target_server_instance_list**
> GetPublicIpTargetServerInstanceListResponse get_public_ip_target_server_instance_list(get_public_ip_target_server_instance_list_request)



공인IP할당(가능)서버인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_public_ip_target_server_instance_list_request = ncloud_server.GetPublicIpTargetServerInstanceListRequest() # GetPublicIpTargetServerInstanceListRequest | getPublicIpTargetServerInstanceListRequest

try:
    api_response = api_instance.get_public_ip_target_server_instance_list(get_public_ip_target_server_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_public_ip_target_server_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_public_ip_target_server_instance_list_request** | [**GetPublicIpTargetServerInstanceListRequest**](GetPublicIpTargetServerInstanceListRequest.md)| getPublicIpTargetServerInstanceListRequest | 

### Return type

[**GetPublicIpTargetServerInstanceListResponse**](GetPublicIpTargetServerInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raid_list**
> GetRaidListResponse get_raid_list(get_raid_list_request)



RAID리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_raid_list_request = ncloud_server.GetRaidListRequest() # GetRaidListRequest | getRaidListRequest

try:
    api_response = api_instance.get_raid_list(get_raid_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_raid_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_raid_list_request** | [**GetRaidListRequest**](GetRaidListRequest.md)| getRaidListRequest | 

### Return type

[**GetRaidListResponse**](GetRaidListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_region_list**
> GetRegionListResponse get_region_list(get_region_list_request)



REGION리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_region_list_request = ncloud_server.GetRegionListRequest() # GetRegionListRequest | getRegionListRequest

try:
    api_response = api_instance.get_region_list(get_region_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_region_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_region_list_request** | [**GetRegionListRequest**](GetRegionListRequest.md)| getRegionListRequest | 

### Return type

[**GetRegionListResponse**](GetRegionListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_password**
> GetRootPasswordResponse get_root_password(get_root_password_request)



루트패스워드조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_root_password_request = ncloud_server.GetRootPasswordRequest() # GetRootPasswordRequest | getRootPasswordRequest

try:
    api_response = api_instance.get_root_password(get_root_password_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_root_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_root_password_request** | [**GetRootPasswordRequest**](GetRootPasswordRequest.md)| getRootPasswordRequest | 

### Return type

[**GetRootPasswordResponse**](GetRootPasswordResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_image_product_list**
> GetServerImageProductListResponse get_server_image_product_list(get_server_image_product_list_request)



서버이미지상품리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_server_image_product_list_request = ncloud_server.GetServerImageProductListRequest() # GetServerImageProductListRequest | getServerImageProductListRequest

try:
    api_response = api_instance.get_server_image_product_list(get_server_image_product_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_server_image_product_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_server_image_product_list_request** | [**GetServerImageProductListRequest**](GetServerImageProductListRequest.md)| getServerImageProductListRequest | 

### Return type

[**GetServerImageProductListResponse**](GetServerImageProductListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_instance_list**
> GetServerInstanceListResponse get_server_instance_list(get_server_instance_list_request)



서버인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_server_instance_list_request = ncloud_server.GetServerInstanceListRequest() # GetServerInstanceListRequest | getServerInstanceListRequest

try:
    api_response = api_instance.get_server_instance_list(get_server_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_server_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_server_instance_list_request** | [**GetServerInstanceListRequest**](GetServerInstanceListRequest.md)| getServerInstanceListRequest | 

### Return type

[**GetServerInstanceListResponse**](GetServerInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_product_list**
> GetServerProductListResponse get_server_product_list(get_server_product_list_request)



서버상품리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_server_product_list_request = ncloud_server.GetServerProductListRequest() # GetServerProductListRequest | getServerProductListRequest

try:
    api_response = api_instance.get_server_product_list(get_server_product_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_server_product_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_server_product_list_request** | [**GetServerProductListRequest**](GetServerProductListRequest.md)| getServerProductListRequest | 

### Return type

[**GetServerProductListResponse**](GetServerProductListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_list**
> GetZoneListResponse get_zone_list(get_zone_list_request)



ZONE리스트조회

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
get_zone_list_request = ncloud_server.GetZoneListRequest() # GetZoneListRequest | getZoneListRequest

try:
    api_response = api_instance.get_zone_list(get_zone_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_zone_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_zone_list_request** | [**GetZoneListRequest**](GetZoneListRequest.md)| getZoneListRequest | 

### Return type

[**GetZoneListResponse**](GetZoneListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reboot_server_instances**
> RebootServerInstancesResponse reboot_server_instances(reboot_server_instances_request)



서버인스턴스재시작

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
reboot_server_instances_request = ncloud_server.RebootServerInstancesRequest() # RebootServerInstancesRequest | rebootServerInstancesRequest

try:
    api_response = api_instance.reboot_server_instances(reboot_server_instances_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->reboot_server_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reboot_server_instances_request** | [**RebootServerInstancesRequest**](RebootServerInstancesRequest.md)| rebootServerInstancesRequest | 

### Return type

[**RebootServerInstancesResponse**](RebootServerInstancesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recreate_server_instance**
> RecreateServerInstanceResponse recreate_server_instance(recreate_server_instance_request)



서버인스턴스재생성

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
recreate_server_instance_request = ncloud_server.RecreateServerInstanceRequest() # RecreateServerInstanceRequest | recreateServerInstanceRequest

try:
    api_response = api_instance.recreate_server_instance(recreate_server_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->recreate_server_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recreate_server_instance_request** | [**RecreateServerInstanceRequest**](RecreateServerInstanceRequest.md)| recreateServerInstanceRequest | 

### Return type

[**RecreateServerInstanceResponse**](RecreateServerInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_nas_volume_access_control**
> RemoveNasVolumeAccessControlResponse remove_nas_volume_access_control(remove_nas_volume_access_control_request)



NAS볼륨인스턴스접근제어제거

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
remove_nas_volume_access_control_request = ncloud_server.RemoveNasVolumeAccessControlRequest() # RemoveNasVolumeAccessControlRequest | removeNasVolumeAccessControlRequest

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



NAS볼륨인스턴스접근제어설정

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
set_nas_volume_access_control_request = ncloud_server.SetNasVolumeAccessControlRequest() # SetNasVolumeAccessControlRequest | setNasVolumeAccessControlRequest

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

# **start_server_instances**
> StartServerInstancesResponse start_server_instances(start_server_instances_request)



서버인스턴스시작

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
start_server_instances_request = ncloud_server.StartServerInstancesRequest() # StartServerInstancesRequest | startServerInstancesRequest

try:
    api_response = api_instance.start_server_instances(start_server_instances_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->start_server_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_server_instances_request** | [**StartServerInstancesRequest**](StartServerInstancesRequest.md)| startServerInstancesRequest | 

### Return type

[**StartServerInstancesResponse**](StartServerInstancesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_server_instances**
> StopServerInstancesResponse stop_server_instances(stop_server_instances_request)



서버인스턴스종료

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
stop_server_instances_request = ncloud_server.StopServerInstancesRequest() # StopServerInstancesRequest | stopServerInstancesRequest

try:
    api_response = api_instance.stop_server_instances(stop_server_instances_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->stop_server_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop_server_instances_request** | [**StopServerInstancesRequest**](StopServerInstancesRequest.md)| stopServerInstancesRequest | 

### Return type

[**StopServerInstancesResponse**](StopServerInstancesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_server_instances**
> TerminateServerInstancesResponse terminate_server_instances(terminate_server_instances_request)



서버인스턴스반납

### Example
```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
terminate_server_instances_request = ncloud_server.TerminateServerInstancesRequest() # TerminateServerInstancesRequest | terminateServerInstancesRequest

try:
    api_response = api_instance.terminate_server_instances(terminate_server_instances_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->terminate_server_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminate_server_instances_request** | [**TerminateServerInstancesRequest**](TerminateServerInstancesRequest.md)| terminateServerInstancesRequest | 

### Return type

[**TerminateServerInstancesResponse**](TerminateServerInstancesResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

