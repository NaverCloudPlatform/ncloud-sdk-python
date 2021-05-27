# CreateTargetGroupRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_code** | **str** | REGION코드 | [optional] 
**target_group_port** | **int** | 타겟그룹포트 | [optional] 
**target_group_protocol_type_code** | [**CommonCode**](CommonCode.md) | 타겟그룹프로토콜유형코드 | 
**target_group_description** | **str** | 타겟그룹설명 | [optional] 
**health_check_cycle** | **int** | 헬스체크주기 | [optional] 
**health_check_down_threshold** | **int** | 헬스체크실패임계값 | [optional] 
**health_check_http_method_type_code** | **str** | 헬스체크HTTP메소드유형코드 | [optional] 
**health_check_port** | **int** | 헬스체크포트 | [optional] 
**health_check_protocol_type_code** | **str** | 헬스체크프로토콜유형코드 | 
**health_check_up_threshold** | **int** | 헬스체크정상임계값 | [optional] 
**health_check_url_path** | **str** | 헬스체크URL경로 | [optional] 
**target_group_name** | **str** | 타겟그룹이름 | [optional] 
**target_no_list** | **list[str]** | 타겟번호리스트 | [optional] 
**target_type_code** | **str** | 타겟유형코드 | [optional] 
**vpc_no** | **str** | VPC번호 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


