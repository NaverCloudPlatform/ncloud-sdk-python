# UpdateAutoScalingGroupRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_code** | **str** | REGION코드 | [optional] 
**auto_scaling_group_no** | **str** | 오토스케일링그룹번호 | 
**launch_configuration_no** | **str** | 론치설정번호 | [optional] 
**server_name_prefix** | **str** | 서버이름Prefix | [optional] 
**min_size** | **int** | 최소용량 | [optional] 
**max_size** | **int** | 최대용량 | [optional] 
**desired_capacity** | **int** | 기대용량 | [optional] 
**default_cool_down** | **int** | 쿨다운기본값 | [optional] 
**health_check_grace_period** | **int** | 헬스체크보류기간 | [optional] 
**health_check_type_code** | **str** | 헬스체크유형코드 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


