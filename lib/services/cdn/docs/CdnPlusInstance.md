# CdnPlusInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdn_instance_no** | **str** | CDN인스턴스번호 | [optional] 
**cdn_instance_status** | [**CommonCode**](CommonCode.md) | CDN인스턴스상태 | [optional] 
**cdn_instance_operation** | [**CommonCode**](CommonCode.md) | CDN인스턴스OP | [optional] 
**cdn_instance_status_name** | **str** | CDN인스턴스상태명 | [optional] 
**create_date** | **str** | 생성일자 | [optional] 
**last_modified_date** | **str** | UPTIME | [optional] 
**cdn_instance_description** | **str** | CDN인스턴스설명 | [optional] 
**service_name** | **str** | 서비스이름 | [optional] 
**is_for_live_transcoder** | **bool** | 라이브트랜스코더여부 | [optional] 
**live_transcoder_instance_no_list** | **list[str]** | 라이브트랜스코더인스턴스번호리스트 | [optional] 
**is_for_image_optimizer** | **bool** | Image Optimizer여부 | [optional] 
**image_optimizer_instance_no** | **str** | Image Optimizer인스턴스번호 | [optional] 
**is_available_partial_domain_purge** | **bool** |  | [optional] 
**cdn_plus_service_domain_list** | [**list[CdnPlusServiceDomain]**](CdnPlusServiceDomain.md) | CDN+서비스도메인리스트 | [optional] 
**cdn_plus_rule** | [**CdnPlusRule**](CdnPlusRule.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


