# UpdateAutoScalingGroupRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_scaling_group_name** | **str** | 오토스케일링그룹명 | [optional] 
**launch_configuration_name** | **str** | 론치설정명 | 
**desired_capacity** | **int** | 기대용량치 | [optional] 
**min_size** | **int** | 최소사이즈 | [optional] 
**max_size** | **int** | 최대사이즈 | [optional] 
**default_cooldown** | **int** | 디폴트쿨다운타임 | [optional] 
**health_check_grace_period** | **int** | 헬스체크보류기간 | [optional] 
**health_check_type_code** | **str** | 헬스체크유형코드 | [optional] 
**zone_no_list** | **list[str]** | ZONE번호리스트 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


