# VpcPeeringInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpc_peering_instance_no** | **str** | VPCPeering인스턴스번호 | [optional] 
**vpc_peering_name** | **str** | VPCPeering이름 | [optional] 
**region_code** | **str** | REGION코드 | [optional] 
**create_date** | **str** | 생성일시 | [optional] 
**last_modifiy_date** | **str** | 마지막수정일시 | [optional] 
**vpc_peering_instance_status** | [**CommonCode**](CommonCode.md) | VPCPeering인스턴스상태 | [optional] 
**vpc_peering_instance_status_name** | **str** | VPCPeering인스턴스상태이름 | [optional] 
**vpc_peering_instance_operation** | [**CommonCode**](CommonCode.md) | VPCPeering인스턴스OP | [optional] 
**source_vpc_no** | **str** | 요청VPC번호 | [optional] 
**source_vpc_name** | **str** | 요청VPC이름 | [optional] 
**source_vpc_ipv4_cidr_block** | **str** | 요청VPC IPv4 CIDR블록 | [optional] 
**source_vpc_login_id** | **str** | 요청VPC소유자ID | [optional] 
**target_vpc_no** | **str** | 수락VPC번호 | [optional] 
**target_vpc_name** | **str** | 수락VPC이름 | [optional] 
**target_vpc_ipv4_cidr_block** | **str** | 수락VPC IPv4 CIDR블록 | [optional] 
**target_vpc_login_id** | **str** | 수락VPC소유자ID | [optional] 
**vpc_peering_description** | **str** | VPCPeering설명 | [optional] 
**has_reverse_vpc_peering** | **bool** | 역방향VPCPeering존재여부 | [optional] 
**is_between_accounts** | **bool** | 계정간의VPCPeering여부 | [optional] 
**reverse_vpc_peering_instance_no** | **str** | 역방향VPCPeering인스턴스번호 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


