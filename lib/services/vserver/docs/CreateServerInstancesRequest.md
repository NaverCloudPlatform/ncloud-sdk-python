# CreateServerInstancesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_code** | **str** | REGION코드 | [optional] 
**server_product_code** | **str** | 서버상품코드 | [optional] 
**server_image_product_code** | **str** | 서버이미지상품코드 | [optional] 
**member_server_image_instance_no** | **str** | 회원서버이미지인스턴스번호 | [optional] 
**server_name** | **str** | 서버이름 | [optional] 
**server_description** | **str** | 서버설명 | [optional] 
**login_key_name** | **str** | 로그인키이름 | [optional] 
**is_protect_server_termination** | **bool** | 반납보호여부 | [optional] 
**server_create_count** | **int** | 서버생성개수 | [optional] 
**server_create_start_no** | **int** | 서버생성시작번호 | [optional] 
**fee_system_type_code** | **str** | 요금제유형코드 | [optional] 
**init_script_no** | **str** | 초기화스크립트번호 | [optional] 
**vpc_no** | **str** | VPC번호 | 
**subnet_no** | **str** | 서브넷번호 | 
**network_interface_list** | [**list[NetworkInterfaceParameter]**](NetworkInterfaceParameter.md) | 네트워크인터페이스리스트 | 
**placement_group_no** | **str** | 물리배치그룹번호 | [optional] 
**is_encrypted_base_block_storage_volume** | **bool** | 기본블록스토리지볼륨암호화여부 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


