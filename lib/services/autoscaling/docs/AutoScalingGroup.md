# AutoScalingGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_scaling_group_name** | **str** | 오토스케일링그룹명 | [optional] 
**launch_configuration_name** | **str** | 론치설정명 | [optional] 
**desired_capacity** | **int** | 기대능력치 | [optional] 
**min_size** | **int** | 최소사이즈 | [optional] 
**max_size** | **int** | 최대사이즈 | [optional] 
**default_cooldown** | **int** |  | [optional] 
**load_balancer_instance_summary_list** | [**list[LoadBalancerInstanceSummary]**](LoadBalancerInstanceSummary.md) | 로드밸런서인스턴스Summary리스트 | [optional] 
**health_check_grace_period** | **int** | 헬스체크보류기간 | [optional] 
**health_check_type** | [**CommonCode**](CommonCode.md) | 헬스체크유형 | [optional] 
**create_date** | **str** | 생성일시 | [optional] 
**in_auto_scaling_group_server_instance_list** | [**list[InAutoScalingGroupServerInstance]**](InAutoScalingGroupServerInstance.md) | 오토스케일링그룹에속한서버인스턴스리스트 | [optional] 
**suspended_process_list** | [**list[SuspendedProcess]**](SuspendedProcess.md) | 보류된프로세스리스트 | [optional] 
**zone_list** | [**list[Zone]**](Zone.md) | ZONE리스트 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


