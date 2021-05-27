# CreateAutoScalingGroupRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_code** | **str** | REGION코드 | [optional] 
**launch_configuration_no** | **str** | 론치설정번호 | 
**auto_scaling_group_name** | **str** | 오토스케일링그룹이름 | [optional] 
**vpc_no** | **str** | VPC번호 | 
**subnet_no** | **str** | 서브넷번호 | 
**access_control_group_no_list** | **list[str]** | ACG번호리스트 | 
**server_name_prefix** | **str** | 서버이름Prefix | [optional] 
**min_size** | **int** | 최소용량 | 
**max_size** | **int** | 최대용량 | 
**desired_capacity** | **int** | 기대용량 | [optional] 
**default_cool_down** | **int** | 쿨다운기본값 | [optional] 
**health_check_grace_period** | **int** | 헬스체크보류기간 | [optional] 
**health_check_type_code** | **str** | 헬스체크유형코드 | [optional] 
**target_group_no_list** | **list[str]** | 타겟그룹번호리스트 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


