# ServerInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_instance_no** | **str** | 서버인스턴스번호 | [optional] 
**server_name** | **str** | 서버명 | [optional] 
**server_description** | **str** | 서버설명 | [optional] 
**cpu_count** | **int** | CPU수 | [optional] 
**memory_size** | **int** | 메모리사이즈 | [optional] 
**base_block_storage_size** | **int** | 기본블럭스토리지사이즈 | [optional] 
**platform_type** | [**CommonCode**](CommonCode.md) | 플랫폼구분 | [optional] 
**login_key_name** | **str** | 로그인키명 | [optional] 
**is_fee_charging_monitoring** | **bool** | 유료모니터링여부 | [optional] 
**public_ip** | **str** | 공인IP | [optional] 
**private_ip** | **str** | 사설IP | [optional] 
**server_image_name** | **str** | 서버이미지명 | [optional] 
**server_instance_status** | [**CommonCode**](CommonCode.md) | 서버인스턴스상태 | [optional] 
**server_instance_operation** | [**CommonCode**](CommonCode.md) | 서버인스턴스OP | [optional] 
**server_instance_status_name** | **str** | 서버인스턴스상태명 | [optional] 
**create_date** | **str** | 생성일자 | [optional] 
**uptime** | **str** | UPTIME | [optional] 
**server_image_product_code** | **str** | 서버이미지상품코드 | [optional] 
**server_product_code** | **str** | 서버상품코드 | [optional] 
**is_protect_server_termination** | **bool** | 반납보호여부 | [optional] 
**port_forwarding_public_ip** | **str** | portForwarding 공인 Ip | [optional] 
**port_forwarding_external_port** | **int** | portForwarding 외부 포트 | [optional] 
**port_forwarding_internal_port** | **int** | portForwarding 내부 포트 | [optional] 
**zone** | [**Zone**](Zone.md) | Zone | [optional] 
**region** | [**Region**](Region.md) | 리전 | [optional] 
**base_block_storage_disk_type** | [**CommonCode**](CommonCode.md) | 기본블록스토리지디스크유형 | [optional] 
**base_block_stroage_disk_detail_type** | [**CommonCode**](CommonCode.md) | 기본블록스토리지디스크상세유형 | [optional] 
**internet_line_type** | [**CommonCode**](CommonCode.md) | 인터넷라인구분 | [optional] 
**user_data** | **str** | 사용자데이타 | [optional] 
**access_control_group_list** | [**list[AccessControlGroup]**](AccessControlGroup.md) | ACG리스트 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


