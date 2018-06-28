# CloudDBInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_db_instance_no** | **str** | CloudDB인스턴스번호 | [optional] 
**cloud_db_service_name** | **str** | CloudDB서비스이름 | [optional] 
**db_kind_code** | **str** | DB유형코드 | [optional] 
**engine_version** | **str** | 엔진버전 | [optional] 
**cpu_count** | **int** | CPU개수 | [optional] 
**memory_size** | **int** | 메모리사이즈 | [optional] 
**data_storage_type** | [**CommonCode**](CommonCode.md) | 데이터스토리지타입 | [optional] 
**license_code** | **str** | 라이센스코드 | [optional] 
**cloud_db_port** | **int** | CloudDB포트 | [optional] 
**is_ha** | **bool** | HA여부 | [optional] 
**backup_time** | **str** | 백업시간 | [optional] 
**backup_file_retention_period** | **int** | 백업파일유지기간 | [optional] 
**cloud_db_instance_status_name** | **str** | CloudDB인스턴스상태이름 | [optional] 
**collation** | **str** | Collation | [optional] 
**reboot_schedule_time** | **str** | 재부팅예약시간 | [optional] 
**create_date** | **str** | 생성일시 | [optional] 
**cloud_db_image_product_code** | **str** | CloudDB이미지상품코드 | [optional] 
**cloud_db_product_code** | **str** | CloudDB상품코드 | [optional] 
**is_cloud_db_config_need_reboot** | **bool** | CloudDB설정재부팅필요여부 | [optional] 
**is_cloud_db_need_reboot** | **bool** | CloudDB재부팅필요여부 | [optional] 
**zone** | [**Zone**](Zone.md) | Zone | [optional] 
**region** | [**Region**](Region.md) | 리전 | [optional] 
**cloud_db_config_list** | [**list[CloudDBConfig]**](CloudDBConfig.md) |  | [optional] 
**cloud_db_config_group_list** | [**list[CloudDBConfigGroup]**](CloudDBConfigGroup.md) |  | [optional] 
**access_control_group_list** | [**list[AccessControlGroup]**](AccessControlGroup.md) |  | [optional] 
**cloud_db_server_instance_list** | [**list[CloudDBServerInstance]**](CloudDBServerInstance.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


