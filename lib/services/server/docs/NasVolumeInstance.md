# NasVolumeInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nas_volume_instance_no** | **str** | NAS볼륨인스턴스번호 | [optional] 
**nas_volume_instance_status** | [**CommonCode**](CommonCode.md) | NAS볼륨인스턴스상태 | [optional] 
**nas_volume_instance_operation** | [**CommonCode**](CommonCode.md) | NAS볼륨인스턴스OP | [optional] 
**nas_volume_instance_status_name** | **str** | 볼륨인스턴스상태명 | [optional] 
**create_date** | **str** | 생성일시 | [optional] 
**nas_volume_instance_description** | **str** | NAS볼륨인스턴스설명 | [optional] 
**mount_information** | **str** | 마운트정보 | [optional] 
**volume_allotment_protocol_type** | [**CommonCode**](CommonCode.md) | 볼륨할당프로토콜구분 | [optional] 
**volume_name** | **str** | 볼륨명 | [optional] 
**volume_total_size** | **int** | 볼륨총사이즈 | [optional] 
**volume_size** | **int** | 볼륨사이즈 | [optional] 
**volume_use_size** | **int** | 볼륨사용사이즈 | [optional] 
**volume_use_ratio** | **float** | 볼륨사용비율 | [optional] 
**snapshot_volume_configuration_ratio** | **float** | 스냅샷볼륨설정비율 | [optional] 
**snapshot_volume_config_period_type** | [**CommonCode**](CommonCode.md) | 스냅샷볼륨설정기간구분 | [optional] 
**snapshot_volume_config_time** | **int** | 스냅샷볼륨설정시간 | [optional] 
**snapshot_volume_size** | **int** | 스냅샷사이즈 | [optional] 
**snapshot_volume_use_size** | **int** | 스냅사용사이즈 | [optional] 
**snapshot_volume_use_ratio** | **float** | 스냅샷사용비율 | [optional] 
**is_snapshot_configuration** | **bool** | 스냅샷설정여부 | [optional] 
**is_event_configuration** | **bool** | 이벤트설정여부 | [optional] 
**region** | [**Region**](Region.md) | 리전 | [optional] 
**zone** | [**Zone**](Zone.md) | ZONE | [optional] 
**nas_volume_instance_custom_ip_list** | [**list[NasVolumeInstanceCustomIp]**](NasVolumeInstanceCustomIp.md) | NAS볼륨커스텀IP리스트 | [optional] 
**nas_volume_server_instance_list** | [**list[ServerInstance]**](ServerInstance.md) | NAS볼륨서버인스턴스리스트 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


