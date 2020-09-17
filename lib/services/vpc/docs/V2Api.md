# ncloud_vpc.V2Api

All URIs are relative to *https://ncloud.apigw.ntruss.com/vpc/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_or_reject_vpc_peering**](V2Api.md#accept_or_reject_vpc_peering) | **POST** /acceptOrRejectVpcPeering | 
[**add_network_acl_inbound_rule**](V2Api.md#add_network_acl_inbound_rule) | **POST** /addNetworkAclInboundRule | 
[**add_network_acl_outbound_rule**](V2Api.md#add_network_acl_outbound_rule) | **POST** /addNetworkAclOutboundRule | 
[**add_route**](V2Api.md#add_route) | **POST** /addRoute | 
[**add_route_table_subnet**](V2Api.md#add_route_table_subnet) | **POST** /addRouteTableSubnet | 
[**create_nat_gateway_instance**](V2Api.md#create_nat_gateway_instance) | **POST** /createNatGatewayInstance | 
[**create_network_acl**](V2Api.md#create_network_acl) | **POST** /createNetworkAcl | 
[**create_route_table**](V2Api.md#create_route_table) | **POST** /createRouteTable | 
[**create_subnet**](V2Api.md#create_subnet) | **POST** /createSubnet | 
[**create_vpc**](V2Api.md#create_vpc) | **POST** /createVpc | 
[**create_vpc_peering_instance**](V2Api.md#create_vpc_peering_instance) | **POST** /createVpcPeeringInstance | 
[**delete_nat_gateway_instance**](V2Api.md#delete_nat_gateway_instance) | **POST** /deleteNatGatewayInstance | 
[**delete_network_acl**](V2Api.md#delete_network_acl) | **POST** /deleteNetworkAcl | 
[**delete_route_table**](V2Api.md#delete_route_table) | **POST** /deleteRouteTable | 
[**delete_subnet**](V2Api.md#delete_subnet) | **POST** /deleteSubnet | 
[**delete_vpc**](V2Api.md#delete_vpc) | **POST** /deleteVpc | 
[**delete_vpc_peering_instance**](V2Api.md#delete_vpc_peering_instance) | **POST** /deleteVpcPeeringInstance | 
[**get_nat_gateway_instance_detail**](V2Api.md#get_nat_gateway_instance_detail) | **POST** /getNatGatewayInstanceDetail | 
[**get_nat_gateway_instance_list**](V2Api.md#get_nat_gateway_instance_list) | **POST** /getNatGatewayInstanceList | 
[**get_network_acl_detail**](V2Api.md#get_network_acl_detail) | **POST** /getNetworkAclDetail | 
[**get_network_acl_list**](V2Api.md#get_network_acl_list) | **POST** /getNetworkAclList | 
[**get_network_acl_rule_list**](V2Api.md#get_network_acl_rule_list) | **POST** /getNetworkAclRuleList | 
[**get_route_list**](V2Api.md#get_route_list) | **POST** /getRouteList | 
[**get_route_table_detail**](V2Api.md#get_route_table_detail) | **POST** /getRouteTableDetail | 
[**get_route_table_list**](V2Api.md#get_route_table_list) | **POST** /getRouteTableList | 
[**get_route_table_subnet_list**](V2Api.md#get_route_table_subnet_list) | **POST** /getRouteTableSubnetList | 
[**get_subnet_detail**](V2Api.md#get_subnet_detail) | **POST** /getSubnetDetail | 
[**get_subnet_list**](V2Api.md#get_subnet_list) | **POST** /getSubnetList | 
[**get_vpc_detail**](V2Api.md#get_vpc_detail) | **POST** /getVpcDetail | 
[**get_vpc_list**](V2Api.md#get_vpc_list) | **POST** /getVpcList | 
[**get_vpc_peering_instance_detail**](V2Api.md#get_vpc_peering_instance_detail) | **POST** /getVpcPeeringInstanceDetail | 
[**get_vpc_peering_instance_list**](V2Api.md#get_vpc_peering_instance_list) | **POST** /getVpcPeeringInstanceList | 
[**remove_network_acl_inbound_rule**](V2Api.md#remove_network_acl_inbound_rule) | **POST** /removeNetworkAclInboundRule | 
[**remove_network_acl_outbound_rule**](V2Api.md#remove_network_acl_outbound_rule) | **POST** /removeNetworkAclOutboundRule | 
[**remove_route**](V2Api.md#remove_route) | **POST** /removeRoute | 
[**remove_route_table_subnet**](V2Api.md#remove_route_table_subnet) | **POST** /removeRouteTableSubnet | 
[**set_nat_gateway_description**](V2Api.md#set_nat_gateway_description) | **POST** /setNatGatewayDescription | 
[**set_network_acl_description**](V2Api.md#set_network_acl_description) | **POST** /setNetworkAclDescription | 
[**set_route_table_description**](V2Api.md#set_route_table_description) | **POST** /setRouteTableDescription | 
[**set_subnet_network_acl**](V2Api.md#set_subnet_network_acl) | **POST** /setSubnetNetworkAcl | 
[**set_vpc_peering_description**](V2Api.md#set_vpc_peering_description) | **POST** /setVpcPeeringDescription | 


# **accept_or_reject_vpc_peering**
> AcceptOrRejectVpcPeeringResponse accept_or_reject_vpc_peering(accept_or_reject_vpc_peering_request)



VPCPeering요청수락거절

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
accept_or_reject_vpc_peering_request = ncloud_vpc.AcceptOrRejectVpcPeeringRequest() # AcceptOrRejectVpcPeeringRequest | acceptOrRejectVpcPeeringRequest

try:
    api_response = api_instance.accept_or_reject_vpc_peering(accept_or_reject_vpc_peering_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->accept_or_reject_vpc_peering: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_or_reject_vpc_peering_request** | [**AcceptOrRejectVpcPeeringRequest**](AcceptOrRejectVpcPeeringRequest.md)| acceptOrRejectVpcPeeringRequest | 

### Return type

[**AcceptOrRejectVpcPeeringResponse**](AcceptOrRejectVpcPeeringResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_network_acl_inbound_rule**
> AddNetworkAclInboundRuleResponse add_network_acl_inbound_rule(add_network_acl_inbound_rule_request)



네트워크ACLInboundRule추가

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
add_network_acl_inbound_rule_request = ncloud_vpc.AddNetworkAclInboundRuleRequest() # AddNetworkAclInboundRuleRequest | addNetworkAclInboundRuleRequest

try:
    api_response = api_instance.add_network_acl_inbound_rule(add_network_acl_inbound_rule_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->add_network_acl_inbound_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_network_acl_inbound_rule_request** | [**AddNetworkAclInboundRuleRequest**](AddNetworkAclInboundRuleRequest.md)| addNetworkAclInboundRuleRequest | 

### Return type

[**AddNetworkAclInboundRuleResponse**](AddNetworkAclInboundRuleResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_network_acl_outbound_rule**
> AddNetworkAclOutboundRuleResponse add_network_acl_outbound_rule(add_network_acl_outbound_rule_request)



네트워크ACLOutboundRule추가

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
add_network_acl_outbound_rule_request = ncloud_vpc.AddNetworkAclOutboundRuleRequest() # AddNetworkAclOutboundRuleRequest | addNetworkAclOutboundRuleRequest

try:
    api_response = api_instance.add_network_acl_outbound_rule(add_network_acl_outbound_rule_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->add_network_acl_outbound_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_network_acl_outbound_rule_request** | [**AddNetworkAclOutboundRuleRequest**](AddNetworkAclOutboundRuleRequest.md)| addNetworkAclOutboundRuleRequest | 

### Return type

[**AddNetworkAclOutboundRuleResponse**](AddNetworkAclOutboundRuleResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_route**
> AddRouteResponse add_route(add_route_request)



라우트추가

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
add_route_request = ncloud_vpc.AddRouteRequest() # AddRouteRequest | addRouteRequest

try:
    api_response = api_instance.add_route(add_route_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->add_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_route_request** | [**AddRouteRequest**](AddRouteRequest.md)| addRouteRequest | 

### Return type

[**AddRouteResponse**](AddRouteResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_route_table_subnet**
> AddRouteTableSubnetResponse add_route_table_subnet(add_route_table_subnet_request)



라우트테이블의연관서브넷추가

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
add_route_table_subnet_request = ncloud_vpc.AddRouteTableSubnetRequest() # AddRouteTableSubnetRequest | addRouteTableSubnetRequest

try:
    api_response = api_instance.add_route_table_subnet(add_route_table_subnet_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->add_route_table_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_route_table_subnet_request** | [**AddRouteTableSubnetRequest**](AddRouteTableSubnetRequest.md)| addRouteTableSubnetRequest | 

### Return type

[**AddRouteTableSubnetResponse**](AddRouteTableSubnetResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nat_gateway_instance**
> CreateNatGatewayInstanceResponse create_nat_gateway_instance(create_nat_gateway_instance_request)



NATGateway인스턴스생성

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
create_nat_gateway_instance_request = ncloud_vpc.CreateNatGatewayInstanceRequest() # CreateNatGatewayInstanceRequest | createNatGatewayInstanceRequest

try:
    api_response = api_instance.create_nat_gateway_instance(create_nat_gateway_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_nat_gateway_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_nat_gateway_instance_request** | [**CreateNatGatewayInstanceRequest**](CreateNatGatewayInstanceRequest.md)| createNatGatewayInstanceRequest | 

### Return type

[**CreateNatGatewayInstanceResponse**](CreateNatGatewayInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_acl**
> CreateNetworkAclResponse create_network_acl(create_network_acl_request)



네트워크ACL생성

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
create_network_acl_request = ncloud_vpc.CreateNetworkAclRequest() # CreateNetworkAclRequest | createNetworkAclRequest

try:
    api_response = api_instance.create_network_acl(create_network_acl_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_network_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_network_acl_request** | [**CreateNetworkAclRequest**](CreateNetworkAclRequest.md)| createNetworkAclRequest | 

### Return type

[**CreateNetworkAclResponse**](CreateNetworkAclResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_route_table**
> CreateRouteTableResponse create_route_table(create_route_table_request)



라우트테이블생성

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
create_route_table_request = ncloud_vpc.CreateRouteTableRequest() # CreateRouteTableRequest | createRouteTableRequest

try:
    api_response = api_instance.create_route_table(create_route_table_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_route_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_route_table_request** | [**CreateRouteTableRequest**](CreateRouteTableRequest.md)| createRouteTableRequest | 

### Return type

[**CreateRouteTableResponse**](CreateRouteTableResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subnet**
> CreateSubnetResponse create_subnet(create_subnet_request)



서브넷생성

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
create_subnet_request = ncloud_vpc.CreateSubnetRequest() # CreateSubnetRequest | createSubnetRequest

try:
    api_response = api_instance.create_subnet(create_subnet_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_subnet_request** | [**CreateSubnetRequest**](CreateSubnetRequest.md)| createSubnetRequest | 

### Return type

[**CreateSubnetResponse**](CreateSubnetResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vpc**
> CreateVpcResponse create_vpc(create_vpc_request)



VPC생성

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
create_vpc_request = ncloud_vpc.CreateVpcRequest() # CreateVpcRequest | createVpcRequest

try:
    api_response = api_instance.create_vpc(create_vpc_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_vpc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_vpc_request** | [**CreateVpcRequest**](CreateVpcRequest.md)| createVpcRequest | 

### Return type

[**CreateVpcResponse**](CreateVpcResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vpc_peering_instance**
> CreateVpcPeeringInstanceResponse create_vpc_peering_instance(create_vpc_peering_instance_request)



VPCPeering인스턴스생성

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
create_vpc_peering_instance_request = ncloud_vpc.CreateVpcPeeringInstanceRequest() # CreateVpcPeeringInstanceRequest | createVpcPeeringInstanceRequest

try:
    api_response = api_instance.create_vpc_peering_instance(create_vpc_peering_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_vpc_peering_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_vpc_peering_instance_request** | [**CreateVpcPeeringInstanceRequest**](CreateVpcPeeringInstanceRequest.md)| createVpcPeeringInstanceRequest | 

### Return type

[**CreateVpcPeeringInstanceResponse**](CreateVpcPeeringInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nat_gateway_instance**
> DeleteNatGatewayInstanceResponse delete_nat_gateway_instance(delete_nat_gateway_instance_request)



NATGateway인스턴스삭제

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
delete_nat_gateway_instance_request = ncloud_vpc.DeleteNatGatewayInstanceRequest() # DeleteNatGatewayInstanceRequest | deleteNatGatewayInstanceRequest

try:
    api_response = api_instance.delete_nat_gateway_instance(delete_nat_gateway_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_nat_gateway_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_nat_gateway_instance_request** | [**DeleteNatGatewayInstanceRequest**](DeleteNatGatewayInstanceRequest.md)| deleteNatGatewayInstanceRequest | 

### Return type

[**DeleteNatGatewayInstanceResponse**](DeleteNatGatewayInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_acl**
> DeleteNetworkAclResponse delete_network_acl(delete_network_acl_request)



네트워크ACL삭제

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
delete_network_acl_request = ncloud_vpc.DeleteNetworkAclRequest() # DeleteNetworkAclRequest | deleteNetworkAclRequest

try:
    api_response = api_instance.delete_network_acl(delete_network_acl_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_network_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_network_acl_request** | [**DeleteNetworkAclRequest**](DeleteNetworkAclRequest.md)| deleteNetworkAclRequest | 

### Return type

[**DeleteNetworkAclResponse**](DeleteNetworkAclResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_route_table**
> DeleteRouteTableResponse delete_route_table(delete_route_table_request)



라우트테이블삭제

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
delete_route_table_request = ncloud_vpc.DeleteRouteTableRequest() # DeleteRouteTableRequest | deleteRouteTableRequest

try:
    api_response = api_instance.delete_route_table(delete_route_table_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_route_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_route_table_request** | [**DeleteRouteTableRequest**](DeleteRouteTableRequest.md)| deleteRouteTableRequest | 

### Return type

[**DeleteRouteTableResponse**](DeleteRouteTableResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subnet**
> DeleteSubnetResponse delete_subnet(delete_subnet_request)



서브넷삭제

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
delete_subnet_request = ncloud_vpc.DeleteSubnetRequest() # DeleteSubnetRequest | deleteSubnetRequest

try:
    api_response = api_instance.delete_subnet(delete_subnet_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_subnet_request** | [**DeleteSubnetRequest**](DeleteSubnetRequest.md)| deleteSubnetRequest | 

### Return type

[**DeleteSubnetResponse**](DeleteSubnetResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vpc**
> DeleteVpcResponse delete_vpc(delete_vpc_request)



VPC삭제

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
delete_vpc_request = ncloud_vpc.DeleteVpcRequest() # DeleteVpcRequest | deleteVpcRequest

try:
    api_response = api_instance.delete_vpc(delete_vpc_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_vpc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_vpc_request** | [**DeleteVpcRequest**](DeleteVpcRequest.md)| deleteVpcRequest | 

### Return type

[**DeleteVpcResponse**](DeleteVpcResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vpc_peering_instance**
> DeleteVpcPeeringInstanceResponse delete_vpc_peering_instance(delete_vpc_peering_instance_request)



VPCPeering인스턴스삭제

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
delete_vpc_peering_instance_request = ncloud_vpc.DeleteVpcPeeringInstanceRequest() # DeleteVpcPeeringInstanceRequest | deleteVpcPeeringInstanceRequest

try:
    api_response = api_instance.delete_vpc_peering_instance(delete_vpc_peering_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_vpc_peering_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_vpc_peering_instance_request** | [**DeleteVpcPeeringInstanceRequest**](DeleteVpcPeeringInstanceRequest.md)| deleteVpcPeeringInstanceRequest | 

### Return type

[**DeleteVpcPeeringInstanceResponse**](DeleteVpcPeeringInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nat_gateway_instance_detail**
> GetNatGatewayInstanceDetailResponse get_nat_gateway_instance_detail(get_nat_gateway_instance_detail_request)



NATGateway인스턴스상세조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_nat_gateway_instance_detail_request = ncloud_vpc.GetNatGatewayInstanceDetailRequest() # GetNatGatewayInstanceDetailRequest | getNatGatewayInstanceDetailRequest

try:
    api_response = api_instance.get_nat_gateway_instance_detail(get_nat_gateway_instance_detail_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_nat_gateway_instance_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_nat_gateway_instance_detail_request** | [**GetNatGatewayInstanceDetailRequest**](GetNatGatewayInstanceDetailRequest.md)| getNatGatewayInstanceDetailRequest | 

### Return type

[**GetNatGatewayInstanceDetailResponse**](GetNatGatewayInstanceDetailResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nat_gateway_instance_list**
> GetNatGatewayInstanceListResponse get_nat_gateway_instance_list(get_nat_gateway_instance_list_request)



NATGateway인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_nat_gateway_instance_list_request = ncloud_vpc.GetNatGatewayInstanceListRequest() # GetNatGatewayInstanceListRequest | getNatGatewayInstanceListRequest

try:
    api_response = api_instance.get_nat_gateway_instance_list(get_nat_gateway_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_nat_gateway_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_nat_gateway_instance_list_request** | [**GetNatGatewayInstanceListRequest**](GetNatGatewayInstanceListRequest.md)| getNatGatewayInstanceListRequest | 

### Return type

[**GetNatGatewayInstanceListResponse**](GetNatGatewayInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_acl_detail**
> GetNetworkAclDetailResponse get_network_acl_detail(get_network_acl_detail_request)



네트워크ACL상세조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_network_acl_detail_request = ncloud_vpc.GetNetworkAclDetailRequest() # GetNetworkAclDetailRequest | getNetworkAclDetailRequest

try:
    api_response = api_instance.get_network_acl_detail(get_network_acl_detail_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_network_acl_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_network_acl_detail_request** | [**GetNetworkAclDetailRequest**](GetNetworkAclDetailRequest.md)| getNetworkAclDetailRequest | 

### Return type

[**GetNetworkAclDetailResponse**](GetNetworkAclDetailResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_acl_list**
> GetNetworkAclListResponse get_network_acl_list(get_network_acl_list_request)



네트워크ACL리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_network_acl_list_request = ncloud_vpc.GetNetworkAclListRequest() # GetNetworkAclListRequest | getNetworkAclListRequest

try:
    api_response = api_instance.get_network_acl_list(get_network_acl_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_network_acl_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_network_acl_list_request** | [**GetNetworkAclListRequest**](GetNetworkAclListRequest.md)| getNetworkAclListRequest | 

### Return type

[**GetNetworkAclListResponse**](GetNetworkAclListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_acl_rule_list**
> GetNetworkAclRuleListResponse get_network_acl_rule_list(get_network_acl_rule_list_request)



네트워크ACLRule리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_network_acl_rule_list_request = ncloud_vpc.GetNetworkAclRuleListRequest() # GetNetworkAclRuleListRequest | getNetworkAclRuleListRequest

try:
    api_response = api_instance.get_network_acl_rule_list(get_network_acl_rule_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_network_acl_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_network_acl_rule_list_request** | [**GetNetworkAclRuleListRequest**](GetNetworkAclRuleListRequest.md)| getNetworkAclRuleListRequest | 

### Return type

[**GetNetworkAclRuleListResponse**](GetNetworkAclRuleListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_list**
> GetRouteListResponse get_route_list(get_route_list_request)



라우트리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_route_list_request = ncloud_vpc.GetRouteListRequest() # GetRouteListRequest | getRouteListRequest

try:
    api_response = api_instance.get_route_list(get_route_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_route_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_route_list_request** | [**GetRouteListRequest**](GetRouteListRequest.md)| getRouteListRequest | 

### Return type

[**GetRouteListResponse**](GetRouteListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_table_detail**
> GetRouteTableDetailResponse get_route_table_detail(get_route_table_detail_request)



라우트테이블상세조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_route_table_detail_request = ncloud_vpc.GetRouteTableDetailRequest() # GetRouteTableDetailRequest | getRouteTableDetailRequest

try:
    api_response = api_instance.get_route_table_detail(get_route_table_detail_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_route_table_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_route_table_detail_request** | [**GetRouteTableDetailRequest**](GetRouteTableDetailRequest.md)| getRouteTableDetailRequest | 

### Return type

[**GetRouteTableDetailResponse**](GetRouteTableDetailResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_table_list**
> GetRouteTableListResponse get_route_table_list(get_route_table_list_request)



라우트테이블리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_route_table_list_request = ncloud_vpc.GetRouteTableListRequest() # GetRouteTableListRequest | getRouteTableListRequest

try:
    api_response = api_instance.get_route_table_list(get_route_table_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_route_table_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_route_table_list_request** | [**GetRouteTableListRequest**](GetRouteTableListRequest.md)| getRouteTableListRequest | 

### Return type

[**GetRouteTableListResponse**](GetRouteTableListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_table_subnet_list**
> GetRouteTableSubnetListResponse get_route_table_subnet_list(get_route_table_subnet_list_request)



라우트테이블에연관된서브넷리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_route_table_subnet_list_request = ncloud_vpc.GetRouteTableSubnetListRequest() # GetRouteTableSubnetListRequest | getRouteTableSubnetListRequest

try:
    api_response = api_instance.get_route_table_subnet_list(get_route_table_subnet_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_route_table_subnet_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_route_table_subnet_list_request** | [**GetRouteTableSubnetListRequest**](GetRouteTableSubnetListRequest.md)| getRouteTableSubnetListRequest | 

### Return type

[**GetRouteTableSubnetListResponse**](GetRouteTableSubnetListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subnet_detail**
> GetSubnetDetailResponse get_subnet_detail(get_subnet_detail_request)



서브넷상세조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_subnet_detail_request = ncloud_vpc.GetSubnetDetailRequest() # GetSubnetDetailRequest | getSubnetDetailRequest

try:
    api_response = api_instance.get_subnet_detail(get_subnet_detail_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_subnet_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_subnet_detail_request** | [**GetSubnetDetailRequest**](GetSubnetDetailRequest.md)| getSubnetDetailRequest | 

### Return type

[**GetSubnetDetailResponse**](GetSubnetDetailResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subnet_list**
> GetSubnetListResponse get_subnet_list(get_subnet_list_request)



서브넷리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_subnet_list_request = ncloud_vpc.GetSubnetListRequest() # GetSubnetListRequest | getSubnetListRequest

try:
    api_response = api_instance.get_subnet_list(get_subnet_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_subnet_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_subnet_list_request** | [**GetSubnetListRequest**](GetSubnetListRequest.md)| getSubnetListRequest | 

### Return type

[**GetSubnetListResponse**](GetSubnetListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpc_detail**
> GetVpcDetailResponse get_vpc_detail(get_vpc_detail_request)



VPC상세조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_vpc_detail_request = ncloud_vpc.GetVpcDetailRequest() # GetVpcDetailRequest | getVpcDetailRequest

try:
    api_response = api_instance.get_vpc_detail(get_vpc_detail_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_vpc_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_vpc_detail_request** | [**GetVpcDetailRequest**](GetVpcDetailRequest.md)| getVpcDetailRequest | 

### Return type

[**GetVpcDetailResponse**](GetVpcDetailResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpc_list**
> GetVpcListResponse get_vpc_list(get_vpc_list_request)



VPC리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_vpc_list_request = ncloud_vpc.GetVpcListRequest() # GetVpcListRequest | getVpcListRequest

try:
    api_response = api_instance.get_vpc_list(get_vpc_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_vpc_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_vpc_list_request** | [**GetVpcListRequest**](GetVpcListRequest.md)| getVpcListRequest | 

### Return type

[**GetVpcListResponse**](GetVpcListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpc_peering_instance_detail**
> GetVpcPeeringInstanceDetailResponse get_vpc_peering_instance_detail(get_vpc_peering_instance_detail_request)



VPCPeering인스턴스상세조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_vpc_peering_instance_detail_request = ncloud_vpc.GetVpcPeeringInstanceDetailRequest() # GetVpcPeeringInstanceDetailRequest | getVpcPeeringInstanceDetailRequest

try:
    api_response = api_instance.get_vpc_peering_instance_detail(get_vpc_peering_instance_detail_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_vpc_peering_instance_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_vpc_peering_instance_detail_request** | [**GetVpcPeeringInstanceDetailRequest**](GetVpcPeeringInstanceDetailRequest.md)| getVpcPeeringInstanceDetailRequest | 

### Return type

[**GetVpcPeeringInstanceDetailResponse**](GetVpcPeeringInstanceDetailResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpc_peering_instance_list**
> GetVpcPeeringInstanceListResponse get_vpc_peering_instance_list(get_vpc_peering_instance_list_request)



VPCPeering인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
get_vpc_peering_instance_list_request = ncloud_vpc.GetVpcPeeringInstanceListRequest() # GetVpcPeeringInstanceListRequest | getVpcPeeringInstanceListRequest

try:
    api_response = api_instance.get_vpc_peering_instance_list(get_vpc_peering_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_vpc_peering_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_vpc_peering_instance_list_request** | [**GetVpcPeeringInstanceListRequest**](GetVpcPeeringInstanceListRequest.md)| getVpcPeeringInstanceListRequest | 

### Return type

[**GetVpcPeeringInstanceListResponse**](GetVpcPeeringInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_network_acl_inbound_rule**
> RemoveNetworkAclInboundRuleResponse remove_network_acl_inbound_rule(remove_network_acl_inbound_rule_request)



네트워크ACLInboundRule제거

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
remove_network_acl_inbound_rule_request = ncloud_vpc.RemoveNetworkAclInboundRuleRequest() # RemoveNetworkAclInboundRuleRequest | removeNetworkAclInboundRuleRequest

try:
    api_response = api_instance.remove_network_acl_inbound_rule(remove_network_acl_inbound_rule_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->remove_network_acl_inbound_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_network_acl_inbound_rule_request** | [**RemoveNetworkAclInboundRuleRequest**](RemoveNetworkAclInboundRuleRequest.md)| removeNetworkAclInboundRuleRequest | 

### Return type

[**RemoveNetworkAclInboundRuleResponse**](RemoveNetworkAclInboundRuleResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_network_acl_outbound_rule**
> RemoveNetworkAclOutboundRuleResponse remove_network_acl_outbound_rule(remove_network_acl_outbound_rule_request)



네트워크ACLOutboundRule제거

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
remove_network_acl_outbound_rule_request = ncloud_vpc.RemoveNetworkAclOutboundRuleRequest() # RemoveNetworkAclOutboundRuleRequest | removeNetworkAclOutboundRuleRequest

try:
    api_response = api_instance.remove_network_acl_outbound_rule(remove_network_acl_outbound_rule_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->remove_network_acl_outbound_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_network_acl_outbound_rule_request** | [**RemoveNetworkAclOutboundRuleRequest**](RemoveNetworkAclOutboundRuleRequest.md)| removeNetworkAclOutboundRuleRequest | 

### Return type

[**RemoveNetworkAclOutboundRuleResponse**](RemoveNetworkAclOutboundRuleResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_route**
> RemoveRouteResponse remove_route(remove_route_request)



라우트제거

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
remove_route_request = ncloud_vpc.RemoveRouteRequest() # RemoveRouteRequest | removeRouteRequest

try:
    api_response = api_instance.remove_route(remove_route_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->remove_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_route_request** | [**RemoveRouteRequest**](RemoveRouteRequest.md)| removeRouteRequest | 

### Return type

[**RemoveRouteResponse**](RemoveRouteResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_route_table_subnet**
> RemoveRouteTableSubnetResponse remove_route_table_subnet(remove_route_table_subnet_request)



라우트테이블의연관서브넷제거

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
remove_route_table_subnet_request = ncloud_vpc.RemoveRouteTableSubnetRequest() # RemoveRouteTableSubnetRequest | removeRouteTableSubnetRequest

try:
    api_response = api_instance.remove_route_table_subnet(remove_route_table_subnet_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->remove_route_table_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_route_table_subnet_request** | [**RemoveRouteTableSubnetRequest**](RemoveRouteTableSubnetRequest.md)| removeRouteTableSubnetRequest | 

### Return type

[**RemoveRouteTableSubnetResponse**](RemoveRouteTableSubnetResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_nat_gateway_description**
> SetNatGatewayDescriptionResponse set_nat_gateway_description(set_nat_gateway_description_request)



NATGateway설명설정

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
set_nat_gateway_description_request = ncloud_vpc.SetNatGatewayDescriptionRequest() # SetNatGatewayDescriptionRequest | setNatGatewayDescriptionRequest

try:
    api_response = api_instance.set_nat_gateway_description(set_nat_gateway_description_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->set_nat_gateway_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_nat_gateway_description_request** | [**SetNatGatewayDescriptionRequest**](SetNatGatewayDescriptionRequest.md)| setNatGatewayDescriptionRequest | 

### Return type

[**SetNatGatewayDescriptionResponse**](SetNatGatewayDescriptionResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_network_acl_description**
> SetNetworkAclDescriptionResponse set_network_acl_description(set_network_acl_description_request)



네트워크ACL설명설정

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
set_network_acl_description_request = ncloud_vpc.SetNetworkAclDescriptionRequest() # SetNetworkAclDescriptionRequest | setNetworkAclDescriptionRequest

try:
    api_response = api_instance.set_network_acl_description(set_network_acl_description_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->set_network_acl_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_network_acl_description_request** | [**SetNetworkAclDescriptionRequest**](SetNetworkAclDescriptionRequest.md)| setNetworkAclDescriptionRequest | 

### Return type

[**SetNetworkAclDescriptionResponse**](SetNetworkAclDescriptionResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_route_table_description**
> SetRouteTableDescriptionResponse set_route_table_description(set_route_table_description_request)



라우트테이블설명설정

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
set_route_table_description_request = ncloud_vpc.SetRouteTableDescriptionRequest() # SetRouteTableDescriptionRequest | setRouteTableDescriptionRequest

try:
    api_response = api_instance.set_route_table_description(set_route_table_description_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->set_route_table_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_route_table_description_request** | [**SetRouteTableDescriptionRequest**](SetRouteTableDescriptionRequest.md)| setRouteTableDescriptionRequest | 

### Return type

[**SetRouteTableDescriptionResponse**](SetRouteTableDescriptionResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_subnet_network_acl**
> SetSubnetNetworkAclResponse set_subnet_network_acl(set_subnet_network_acl_request)



서브넷의네트워크ACL설정

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
set_subnet_network_acl_request = ncloud_vpc.SetSubnetNetworkAclRequest() # SetSubnetNetworkAclRequest | setSubnetNetworkAclRequest

try:
    api_response = api_instance.set_subnet_network_acl(set_subnet_network_acl_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->set_subnet_network_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_subnet_network_acl_request** | [**SetSubnetNetworkAclRequest**](SetSubnetNetworkAclRequest.md)| setSubnetNetworkAclRequest | 

### Return type

[**SetSubnetNetworkAclResponse**](SetSubnetNetworkAclResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_vpc_peering_description**
> SetVpcPeeringDescriptionResponse set_vpc_peering_description(set_vpc_peering_description_request)



VPCPeering설명설정

### Example
```python
from __future__ import print_function
import ncloud_vpc
from ncloud_vpc.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_vpc.V2Api(ncloud_vpc.ApiClient(configuration))
set_vpc_peering_description_request = ncloud_vpc.SetVpcPeeringDescriptionRequest() # SetVpcPeeringDescriptionRequest | setVpcPeeringDescriptionRequest

try:
    api_response = api_instance.set_vpc_peering_description(set_vpc_peering_description_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->set_vpc_peering_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_vpc_peering_description_request** | [**SetVpcPeeringDescriptionRequest**](SetVpcPeeringDescriptionRequest.md)| setVpcPeeringDescriptionRequest | 

### Return type

[**SetVpcPeeringDescriptionResponse**](SetVpcPeeringDescriptionResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

