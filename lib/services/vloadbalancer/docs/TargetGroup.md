# TargetGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_group_no** | **str** | 타겟그룹번호 | [optional] 
**target_group_name** | **str** | 타겟그룹이름 | [optional] 
**target_type** | [**CommonCode**](CommonCode.md) | 타겟유형 | [optional] 
**vpc_no** | **str** | VPC번호 | [optional] 
**target_group_protocol_type** | [**CommonCode**](CommonCode.md) | 타겟그룹프로토콜유형 | [optional] 
**target_group_port** | **int** | 타겟그룹포트 | [optional] 
**target_group_description** | **str** | 타겟그룹설명 | [optional] 
**use_sticky_session** | **bool** | 세션별접근사용여부 | [optional] 
**use_proxy_protocol** | **bool** | 프록시프로토콜사용여부 | [optional] 
**algorithm_type** | [**CommonCode**](CommonCode.md) | 알고리즘유형 | [optional] 
**create_date** | **str** | 생성일시 | [optional] 
**region_code** | **str** | REGION코드 | [optional] 
**load_balancer_instance_no** | **str** | 로드밸런서인스턴스번호 | [optional] 
**health_check_protocol_type** | [**CommonCode**](CommonCode.md) | 헬스체크프로토콜유형 | [optional] 
**health_check_port** | **int** | 타겟그룹포트 | [optional] 
**health_check_url_path** | **str** | 헬스체크URL경로 | [optional] 
**health_check_http_method_type** | [**CommonCode**](CommonCode.md) | 헬스체크HTTP메소드유형 | [optional] 
**health_check_cycle** | **int** | 헬스체크주기 | [optional] 
**health_check_up_threshold** | **int** | 헬스체크정상임계값 | [optional] 
**health_check_down_threshold** | **int** | 헬스체크실패임계값 | [optional] 
**target_no_list** | **list[str]** | 타겟번호리스트 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


