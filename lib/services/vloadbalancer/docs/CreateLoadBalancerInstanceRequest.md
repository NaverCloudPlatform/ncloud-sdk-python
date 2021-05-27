# CreateLoadBalancerInstanceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_code** | **str** | REGION코드 | [optional] 
**idle_timeout** | **int** | 연결타임아웃 | [optional] 
**load_balancer_description** | **str** | 로드밸런서설명 | [optional] 
**load_balancer_network_type_code** | **str** | 로드밸런서네트워크유형코드 | [optional] 
**load_balancer_type_code** | **str** | 로드밸런서유형코드 | 
**load_balancer_listener_list** | [**list[LoadBalancerListenerParameter]**](LoadBalancerListenerParameter.md) | 로드밸런서리스너리스트 | [optional] 
**load_balancer_name** | **str** | 로드밸런서이름 | [optional] 
**throughput_type_code** | **str** | 부하처리성능유형코드 | [optional] 
**vpc_no** | **str** | VPC번호 | 
**subnet_no_list** | **list[str]** | 서브넷번호리스트 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


