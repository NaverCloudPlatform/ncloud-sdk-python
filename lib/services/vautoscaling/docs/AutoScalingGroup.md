# AutoScalingGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpc_no** | **str** | VPC번호 | [optional] 
**subnet_no** | **str** | 서브넷번호 | [optional] 
**server_name_prefix** | **str** | 서버이름Prefix | [optional] 
**auto_scaling_group_no** | **str** | 오토스케일링그룹번호 | [optional] 
**auto_scaling_group_name** | **str** | 오토스케일링그룹이름 | [optional] 
**launch_configuration_no** | **str** | 론치설정번호 | [optional] 
**min_size** | **int** | 최소용량 | [optional] 
**max_size** | **int** | 최대용량 | [optional] 
**desired_capacity** | **int** | 기대용량 | [optional] 
**default_cool_down** | **int** | 쿨다운기본값 | [optional] 
**health_check_grace_period** | **int** | 헬스체크보류기간 | [optional] 
**health_check_type** | [**CommonCode**](CommonCode.md) | 헬스체크유형 | [optional] 
**create_date** | **str** | 생성일시 | [optional] 
**auto_scaling_group_status** | [**CommonCode**](CommonCode.md) | 오토스케일링그룹상태 | [optional] 
**target_group_no_list** | **list[str]** | 타겟그룹번호리스트 | [optional] 
**in_auto_scaling_group_server_instance_list** | [**list[InAutoScalingGroupServerInstance]**](InAutoScalingGroupServerInstance.md) | 오토스케일링그룹에속한서버인스턴스리스트 | [optional] 
**access_control_group_no_list** | **list[str]** | ACG번호리스트 | [optional] 
**suspended_process_list** | [**list[SuspendedProcess]**](SuspendedProcess.md) | 일시정지된프로세스리스트 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


