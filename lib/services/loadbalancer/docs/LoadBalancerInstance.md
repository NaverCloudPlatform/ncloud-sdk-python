# LoadBalancerInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**load_balancer_instance_no** | **str** | 로드밸런서인스턴스번호 | [optional] 
**virtual_ip** | **str** | virtualIp | [optional] 
**load_balancer_name** | **str** | 로드밸런서명 | [optional] 
**load_balancer_algorithm_type** | [**CommonCode**](CommonCode.md) | 로드밸런서알고리즘구분코 | [optional] 
**load_balancer_description** | **str** | 로드밸런서설명 | [optional] 
**create_date** | **str** | 생성일자 | [optional] 
**domain_name** | **str** | 도메인명 | [optional] 
**internet_line_type** | [**CommonCode**](CommonCode.md) | 인터넷회선구분 | [optional] 
**load_balancer_instance_status_name** | **str** | 로드밸런서인스턴스상태명 | [optional] 
**load_balancer_instance_status** | [**CommonCode**](CommonCode.md) | 로드밸런서인스턴스상태 | [optional] 
**load_balancer_instance_operation** | [**CommonCode**](CommonCode.md) | 로드밸런서인스턴스OP | [optional] 
**network_usage_type** | [**CommonCode**](CommonCode.md) | 네트워크사용구분 | [optional] 
**is_http_keep_alive** | **bool** | httpKeepAlive사용여부 | [optional] 
**connection_timeout** | **int** | 커넥션타임아웃 | [optional] 
**certificate_name** | **str** | SSL인증명 | [optional] 
**load_balancer_rule_list** | [**list[LoadBalancerRule]**](LoadBalancerRule.md) |  | [optional] 
**load_balanced_server_instance_list** | [**list[LoadBalancedServerInstance]**](LoadBalancedServerInstance.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


