# ncloud-server

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2021-03-04T10:39:42Z
- Package version: 1.1.3
- Build package: io.swagger.codegen.languages.NcpPythonForNcloudClientCodegen

## Requirements.

Python 2.7 and 3.6+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install ncloud-server --user
```
(you may need to run `pip` with root permission: `sudo pip install ncloud-server --user)

Then import the package:
```python
import ncloud_server 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ncloud_server
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import ncloud_server
from ncloud_server.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_server.V2Api(ncloud_server.ApiClient(configuration))
add_nas_volume_access_control_request = ncloud_server.AddNasVolumeAccessControlRequest() # AddNasVolumeAccessControlRequest | addNasVolumeAccessControlRequest

try:
    api_response = api_instance.add_nas_volume_access_control(add_nas_volume_access_control_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->add_nas_volume_access_control: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://ncloud.apigw.ntruss.com/server/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*V2Api* | [**add_nas_volume_access_control**](docs/V2Api.md#add_nas_volume_access_control) | **POST** /addNasVolumeAccessControl | 
*V2Api* | [**add_port_forwarding_rules**](docs/V2Api.md#add_port_forwarding_rules) | **POST** /addPortForwardingRules | 
*V2Api* | [**associate_public_ip_with_server_instance**](docs/V2Api.md#associate_public_ip_with_server_instance) | **POST** /associatePublicIpWithServerInstance | 
*V2Api* | [**attach_block_storage_instance**](docs/V2Api.md#attach_block_storage_instance) | **POST** /attachBlockStorageInstance | 
*V2Api* | [**attach_network_interface**](docs/V2Api.md#attach_network_interface) | **POST** /attachNetworkInterface | 
*V2Api* | [**change_block_storage_volume_size**](docs/V2Api.md#change_block_storage_volume_size) | **POST** /changeBlockStorageVolumeSize | 
*V2Api* | [**change_nas_volume_size**](docs/V2Api.md#change_nas_volume_size) | **POST** /changeNasVolumeSize | 
*V2Api* | [**change_server_instance_spec**](docs/V2Api.md#change_server_instance_spec) | **POST** /changeServerInstanceSpec | 
*V2Api* | [**create_block_storage_instance**](docs/V2Api.md#create_block_storage_instance) | **POST** /createBlockStorageInstance | 
*V2Api* | [**create_block_storage_snapshot_instance**](docs/V2Api.md#create_block_storage_snapshot_instance) | **POST** /createBlockStorageSnapshotInstance | 
*V2Api* | [**create_instance_tags**](docs/V2Api.md#create_instance_tags) | **POST** /createInstanceTags | 
*V2Api* | [**create_login_key**](docs/V2Api.md#create_login_key) | **POST** /createLoginKey | 
*V2Api* | [**create_member_server_image**](docs/V2Api.md#create_member_server_image) | **POST** /createMemberServerImage | 
*V2Api* | [**create_nas_volume_instance**](docs/V2Api.md#create_nas_volume_instance) | **POST** /createNasVolumeInstance | 
*V2Api* | [**create_network_interface**](docs/V2Api.md#create_network_interface) | **POST** /createNetworkInterface | 
*V2Api* | [**create_public_ip_instance**](docs/V2Api.md#create_public_ip_instance) | **POST** /createPublicIpInstance | 
*V2Api* | [**create_server_instances**](docs/V2Api.md#create_server_instances) | **POST** /createServerInstances | 
*V2Api* | [**delete_block_storage_instances**](docs/V2Api.md#delete_block_storage_instances) | **POST** /deleteBlockStorageInstances | 
*V2Api* | [**delete_block_storage_snapshot_instances**](docs/V2Api.md#delete_block_storage_snapshot_instances) | **POST** /deleteBlockStorageSnapshotInstances | 
*V2Api* | [**delete_instance_tags**](docs/V2Api.md#delete_instance_tags) | **POST** /deleteInstanceTags | 
*V2Api* | [**delete_login_key**](docs/V2Api.md#delete_login_key) | **POST** /deleteLoginKey | 
*V2Api* | [**delete_member_server_images**](docs/V2Api.md#delete_member_server_images) | **POST** /deleteMemberServerImages | 
*V2Api* | [**delete_nas_volume_instance**](docs/V2Api.md#delete_nas_volume_instance) | **POST** /deleteNasVolumeInstance | 
*V2Api* | [**delete_network_interface**](docs/V2Api.md#delete_network_interface) | **POST** /deleteNetworkInterface | 
*V2Api* | [**delete_port_forwarding_rules**](docs/V2Api.md#delete_port_forwarding_rules) | **POST** /deletePortForwardingRules | 
*V2Api* | [**delete_public_ip_instances**](docs/V2Api.md#delete_public_ip_instances) | **POST** /deletePublicIpInstances | 
*V2Api* | [**detach_block_storage_instances**](docs/V2Api.md#detach_block_storage_instances) | **POST** /detachBlockStorageInstances | 
*V2Api* | [**detach_network_interface**](docs/V2Api.md#detach_network_interface) | **POST** /detachNetworkInterface | 
*V2Api* | [**disassociate_public_ip_from_server_instance**](docs/V2Api.md#disassociate_public_ip_from_server_instance) | **POST** /disassociatePublicIpFromServerInstance | 
*V2Api* | [**get_access_control_group_list**](docs/V2Api.md#get_access_control_group_list) | **POST** /getAccessControlGroupList | 
*V2Api* | [**get_access_control_group_server_instance_list**](docs/V2Api.md#get_access_control_group_server_instance_list) | **POST** /getAccessControlGroupServerInstanceList | 
*V2Api* | [**get_access_control_rule_list**](docs/V2Api.md#get_access_control_rule_list) | **POST** /getAccessControlRuleList | 
*V2Api* | [**get_block_storage_instance_list**](docs/V2Api.md#get_block_storage_instance_list) | **POST** /getBlockStorageInstanceList | 
*V2Api* | [**get_block_storage_snapshot_instance_list**](docs/V2Api.md#get_block_storage_snapshot_instance_list) | **POST** /getBlockStorageSnapshotInstanceList | 
*V2Api* | [**get_init_script_list**](docs/V2Api.md#get_init_script_list) | **POST** /getInitScriptList | 
*V2Api* | [**get_instance_tag_list**](docs/V2Api.md#get_instance_tag_list) | **POST** /getInstanceTagList | 
*V2Api* | [**get_login_key_list**](docs/V2Api.md#get_login_key_list) | **POST** /getLoginKeyList | 
*V2Api* | [**get_member_server_image_list**](docs/V2Api.md#get_member_server_image_list) | **POST** /getMemberServerImageList | 
*V2Api* | [**get_nas_volume_instance_list**](docs/V2Api.md#get_nas_volume_instance_list) | **POST** /getNasVolumeInstanceList | 
*V2Api* | [**get_nas_volume_instance_rating_list**](docs/V2Api.md#get_nas_volume_instance_rating_list) | **POST** /getNasVolumeInstanceRatingList | 
*V2Api* | [**get_network_interface_list**](docs/V2Api.md#get_network_interface_list) | **POST** /getNetworkInterfaceList | 
*V2Api* | [**get_port_forwarding_rule_list**](docs/V2Api.md#get_port_forwarding_rule_list) | **POST** /getPortForwardingRuleList | 
*V2Api* | [**get_private_subnet_instance_list**](docs/V2Api.md#get_private_subnet_instance_list) | **POST** /getPrivateSubnetInstanceList | 
*V2Api* | [**get_public_ip_instance_list**](docs/V2Api.md#get_public_ip_instance_list) | **POST** /getPublicIpInstanceList | 
*V2Api* | [**get_public_ip_target_server_instance_list**](docs/V2Api.md#get_public_ip_target_server_instance_list) | **POST** /getPublicIpTargetServerInstanceList | 
*V2Api* | [**get_raid_list**](docs/V2Api.md#get_raid_list) | **POST** /getRaidList | 
*V2Api* | [**get_region_list**](docs/V2Api.md#get_region_list) | **POST** /getRegionList | 
*V2Api* | [**get_root_password**](docs/V2Api.md#get_root_password) | **POST** /getRootPassword | 
*V2Api* | [**get_root_password_server_instance_list**](docs/V2Api.md#get_root_password_server_instance_list) | **POST** /getRootPasswordServerInstanceList | 
*V2Api* | [**get_server_image_product_list**](docs/V2Api.md#get_server_image_product_list) | **POST** /getServerImageProductList | 
*V2Api* | [**get_server_instance_list**](docs/V2Api.md#get_server_instance_list) | **POST** /getServerInstanceList | 
*V2Api* | [**get_server_product_list**](docs/V2Api.md#get_server_product_list) | **POST** /getServerProductList | 
*V2Api* | [**get_zone_list**](docs/V2Api.md#get_zone_list) | **POST** /getZoneList | 
*V2Api* | [**import_login_key**](docs/V2Api.md#import_login_key) | **POST** /importLoginKey | 
*V2Api* | [**reboot_server_instances**](docs/V2Api.md#reboot_server_instances) | **POST** /rebootServerInstances | 
*V2Api* | [**recreate_server_instance**](docs/V2Api.md#recreate_server_instance) | **POST** /recreateServerInstance | 
*V2Api* | [**remove_nas_volume_access_control**](docs/V2Api.md#remove_nas_volume_access_control) | **POST** /removeNasVolumeAccessControl | 
*V2Api* | [**replace_server_instance_associated_with_public_ip**](docs/V2Api.md#replace_server_instance_associated_with_public_ip) | **POST** /replaceServerInstanceAssociatedWithPublicIp | 
*V2Api* | [**set_nas_volume_access_control**](docs/V2Api.md#set_nas_volume_access_control) | **POST** /setNasVolumeAccessControl | 
*V2Api* | [**start_server_instances**](docs/V2Api.md#start_server_instances) | **POST** /startServerInstances | 
*V2Api* | [**stop_server_instances**](docs/V2Api.md#stop_server_instances) | **POST** /stopServerInstances | 
*V2Api* | [**terminate_server_instances**](docs/V2Api.md#terminate_server_instances) | **POST** /terminateServerInstances | 


## Documentation For Models

 - [AccessControlGroup](docs/AccessControlGroup.md)
 - [AccessControlRule](docs/AccessControlRule.md)
 - [AddNasVolumeAccessControlRequest](docs/AddNasVolumeAccessControlRequest.md)
 - [AddNasVolumeAccessControlResponse](docs/AddNasVolumeAccessControlResponse.md)
 - [AddPortForwardingRulesRequest](docs/AddPortForwardingRulesRequest.md)
 - [AddPortForwardingRulesResponse](docs/AddPortForwardingRulesResponse.md)
 - [AssociatePublicIpWithServerInstanceRequest](docs/AssociatePublicIpWithServerInstanceRequest.md)
 - [AssociatePublicIpWithServerInstanceResponse](docs/AssociatePublicIpWithServerInstanceResponse.md)
 - [AttachBlockStorageInstanceRequest](docs/AttachBlockStorageInstanceRequest.md)
 - [AttachBlockStorageInstanceResponse](docs/AttachBlockStorageInstanceResponse.md)
 - [AttachNetworkInterfaceRequest](docs/AttachNetworkInterfaceRequest.md)
 - [AttachNetworkInterfaceResponse](docs/AttachNetworkInterfaceResponse.md)
 - [BlockDevicePartition](docs/BlockDevicePartition.md)
 - [BlockStorageInstance](docs/BlockStorageInstance.md)
 - [BlockStorageSnapshotInstance](docs/BlockStorageSnapshotInstance.md)
 - [ChangeBlockStorageVolumeSizeRequest](docs/ChangeBlockStorageVolumeSizeRequest.md)
 - [ChangeBlockStorageVolumeSizeResponse](docs/ChangeBlockStorageVolumeSizeResponse.md)
 - [ChangeNasVolumeSizeRequest](docs/ChangeNasVolumeSizeRequest.md)
 - [ChangeNasVolumeSizeResponse](docs/ChangeNasVolumeSizeResponse.md)
 - [ChangeServerInstanceSpecRequest](docs/ChangeServerInstanceSpecRequest.md)
 - [ChangeServerInstanceSpecResponse](docs/ChangeServerInstanceSpecResponse.md)
 - [CommonCode](docs/CommonCode.md)
 - [CreateBlockStorageInstanceRequest](docs/CreateBlockStorageInstanceRequest.md)
 - [CreateBlockStorageInstanceResponse](docs/CreateBlockStorageInstanceResponse.md)
 - [CreateBlockStorageSnapshotInstanceRequest](docs/CreateBlockStorageSnapshotInstanceRequest.md)
 - [CreateBlockStorageSnapshotInstanceResponse](docs/CreateBlockStorageSnapshotInstanceResponse.md)
 - [CreateInstanceTagsRequest](docs/CreateInstanceTagsRequest.md)
 - [CreateInstanceTagsResponse](docs/CreateInstanceTagsResponse.md)
 - [CreateLoginKeyRequest](docs/CreateLoginKeyRequest.md)
 - [CreateLoginKeyResponse](docs/CreateLoginKeyResponse.md)
 - [CreateMemberServerImageRequest](docs/CreateMemberServerImageRequest.md)
 - [CreateMemberServerImageResponse](docs/CreateMemberServerImageResponse.md)
 - [CreateNasVolumeInstanceRequest](docs/CreateNasVolumeInstanceRequest.md)
 - [CreateNasVolumeInstanceResponse](docs/CreateNasVolumeInstanceResponse.md)
 - [CreateNetworkInterfaceRequest](docs/CreateNetworkInterfaceRequest.md)
 - [CreateNetworkInterfaceResponse](docs/CreateNetworkInterfaceResponse.md)
 - [CreatePublicIpInstanceRequest](docs/CreatePublicIpInstanceRequest.md)
 - [CreatePublicIpInstanceResponse](docs/CreatePublicIpInstanceResponse.md)
 - [CreateServerInstancesRequest](docs/CreateServerInstancesRequest.md)
 - [CreateServerInstancesResponse](docs/CreateServerInstancesResponse.md)
 - [DeleteBlockStorageInstancesRequest](docs/DeleteBlockStorageInstancesRequest.md)
 - [DeleteBlockStorageInstancesResponse](docs/DeleteBlockStorageInstancesResponse.md)
 - [DeleteBlockStorageSnapshotInstancesRequest](docs/DeleteBlockStorageSnapshotInstancesRequest.md)
 - [DeleteBlockStorageSnapshotInstancesResponse](docs/DeleteBlockStorageSnapshotInstancesResponse.md)
 - [DeleteInstanceTagsRequest](docs/DeleteInstanceTagsRequest.md)
 - [DeleteInstanceTagsResponse](docs/DeleteInstanceTagsResponse.md)
 - [DeleteLoginKeyRequest](docs/DeleteLoginKeyRequest.md)
 - [DeleteLoginKeyResponse](docs/DeleteLoginKeyResponse.md)
 - [DeleteMemberServerImagesRequest](docs/DeleteMemberServerImagesRequest.md)
 - [DeleteMemberServerImagesResponse](docs/DeleteMemberServerImagesResponse.md)
 - [DeleteNasVolumeInstanceRequest](docs/DeleteNasVolumeInstanceRequest.md)
 - [DeleteNasVolumeInstanceResponse](docs/DeleteNasVolumeInstanceResponse.md)
 - [DeleteNetworkInterfaceRequest](docs/DeleteNetworkInterfaceRequest.md)
 - [DeleteNetworkInterfaceResponse](docs/DeleteNetworkInterfaceResponse.md)
 - [DeletePortForwardingRulesRequest](docs/DeletePortForwardingRulesRequest.md)
 - [DeletePortForwardingRulesResponse](docs/DeletePortForwardingRulesResponse.md)
 - [DeletePublicIpInstancesRequest](docs/DeletePublicIpInstancesRequest.md)
 - [DeletePublicIpInstancesResponse](docs/DeletePublicIpInstancesResponse.md)
 - [DetachBlockStorageInstancesRequest](docs/DetachBlockStorageInstancesRequest.md)
 - [DetachBlockStorageInstancesResponse](docs/DetachBlockStorageInstancesResponse.md)
 - [DetachNetworkInterfaceRequest](docs/DetachNetworkInterfaceRequest.md)
 - [DetachNetworkInterfaceResponse](docs/DetachNetworkInterfaceResponse.md)
 - [DisassociatePublicIpFromServerInstanceRequest](docs/DisassociatePublicIpFromServerInstanceRequest.md)
 - [DisassociatePublicIpFromServerInstanceResponse](docs/DisassociatePublicIpFromServerInstanceResponse.md)
 - [GetAccessControlGroupListRequest](docs/GetAccessControlGroupListRequest.md)
 - [GetAccessControlGroupListResponse](docs/GetAccessControlGroupListResponse.md)
 - [GetAccessControlGroupServerInstanceListRequest](docs/GetAccessControlGroupServerInstanceListRequest.md)
 - [GetAccessControlGroupServerInstanceListResponse](docs/GetAccessControlGroupServerInstanceListResponse.md)
 - [GetAccessControlRuleListRequest](docs/GetAccessControlRuleListRequest.md)
 - [GetAccessControlRuleListResponse](docs/GetAccessControlRuleListResponse.md)
 - [GetBlockStorageInstanceListRequest](docs/GetBlockStorageInstanceListRequest.md)
 - [GetBlockStorageInstanceListResponse](docs/GetBlockStorageInstanceListResponse.md)
 - [GetBlockStorageSnapshotInstanceListRequest](docs/GetBlockStorageSnapshotInstanceListRequest.md)
 - [GetBlockStorageSnapshotInstanceListResponse](docs/GetBlockStorageSnapshotInstanceListResponse.md)
 - [GetInitScriptListRequest](docs/GetInitScriptListRequest.md)
 - [GetInitScriptListResponse](docs/GetInitScriptListResponse.md)
 - [GetInstanceTagListRequest](docs/GetInstanceTagListRequest.md)
 - [GetInstanceTagListResponse](docs/GetInstanceTagListResponse.md)
 - [GetLoginKeyListRequest](docs/GetLoginKeyListRequest.md)
 - [GetLoginKeyListResponse](docs/GetLoginKeyListResponse.md)
 - [GetMemberServerImageListRequest](docs/GetMemberServerImageListRequest.md)
 - [GetMemberServerImageListResponse](docs/GetMemberServerImageListResponse.md)
 - [GetNasVolumeInstanceListRequest](docs/GetNasVolumeInstanceListRequest.md)
 - [GetNasVolumeInstanceListResponse](docs/GetNasVolumeInstanceListResponse.md)
 - [GetNasVolumeInstanceRatingListRequest](docs/GetNasVolumeInstanceRatingListRequest.md)
 - [GetNasVolumeInstanceRatingListResponse](docs/GetNasVolumeInstanceRatingListResponse.md)
 - [GetNetworkInterfaceListRequest](docs/GetNetworkInterfaceListRequest.md)
 - [GetNetworkInterfaceListResponse](docs/GetNetworkInterfaceListResponse.md)
 - [GetPortForwardingRuleListRequest](docs/GetPortForwardingRuleListRequest.md)
 - [GetPortForwardingRuleListResponse](docs/GetPortForwardingRuleListResponse.md)
 - [GetPrivateSubnetInstanceListRequest](docs/GetPrivateSubnetInstanceListRequest.md)
 - [GetPrivateSubnetInstanceListResponse](docs/GetPrivateSubnetInstanceListResponse.md)
 - [GetPublicIpInstanceListRequest](docs/GetPublicIpInstanceListRequest.md)
 - [GetPublicIpInstanceListResponse](docs/GetPublicIpInstanceListResponse.md)
 - [GetPublicIpTargetServerInstanceListRequest](docs/GetPublicIpTargetServerInstanceListRequest.md)
 - [GetPublicIpTargetServerInstanceListResponse](docs/GetPublicIpTargetServerInstanceListResponse.md)
 - [GetRaidListRequest](docs/GetRaidListRequest.md)
 - [GetRaidListResponse](docs/GetRaidListResponse.md)
 - [GetRegionListRequest](docs/GetRegionListRequest.md)
 - [GetRegionListResponse](docs/GetRegionListResponse.md)
 - [GetRootPasswordRequest](docs/GetRootPasswordRequest.md)
 - [GetRootPasswordResponse](docs/GetRootPasswordResponse.md)
 - [GetRootPasswordServerInstanceListRequest](docs/GetRootPasswordServerInstanceListRequest.md)
 - [GetRootPasswordServerInstanceListResponse](docs/GetRootPasswordServerInstanceListResponse.md)
 - [GetServerImageProductListRequest](docs/GetServerImageProductListRequest.md)
 - [GetServerImageProductListResponse](docs/GetServerImageProductListResponse.md)
 - [GetServerInstanceListRequest](docs/GetServerInstanceListRequest.md)
 - [GetServerInstanceListResponse](docs/GetServerInstanceListResponse.md)
 - [GetServerProductListRequest](docs/GetServerProductListRequest.md)
 - [GetServerProductListResponse](docs/GetServerProductListResponse.md)
 - [GetZoneListRequest](docs/GetZoneListRequest.md)
 - [GetZoneListResponse](docs/GetZoneListResponse.md)
 - [ImportLoginKeyRequest](docs/ImportLoginKeyRequest.md)
 - [ImportLoginKeyResponse](docs/ImportLoginKeyResponse.md)
 - [InitScript](docs/InitScript.md)
 - [InstanceTag](docs/InstanceTag.md)
 - [InstanceTagParameter](docs/InstanceTagParameter.md)
 - [LoginKey](docs/LoginKey.md)
 - [MemberServerImage](docs/MemberServerImage.md)
 - [NasVolumeInstance](docs/NasVolumeInstance.md)
 - [NasVolumeInstanceCustomIp](docs/NasVolumeInstanceCustomIp.md)
 - [NasVolumeInstanceRating](docs/NasVolumeInstanceRating.md)
 - [NetworkInterface](docs/NetworkInterface.md)
 - [PortForwardingRule](docs/PortForwardingRule.md)
 - [PortForwardingRuleParameter](docs/PortForwardingRuleParameter.md)
 - [PrivateSubnetInstance](docs/PrivateSubnetInstance.md)
 - [Product](docs/Product.md)
 - [PublicIpInstance](docs/PublicIpInstance.md)
 - [Raid](docs/Raid.md)
 - [RebootServerInstancesRequest](docs/RebootServerInstancesRequest.md)
 - [RebootServerInstancesResponse](docs/RebootServerInstancesResponse.md)
 - [RecreateServerInstanceRequest](docs/RecreateServerInstanceRequest.md)
 - [RecreateServerInstanceResponse](docs/RecreateServerInstanceResponse.md)
 - [Region](docs/Region.md)
 - [RemoveNasVolumeAccessControlRequest](docs/RemoveNasVolumeAccessControlRequest.md)
 - [RemoveNasVolumeAccessControlResponse](docs/RemoveNasVolumeAccessControlResponse.md)
 - [ReplaceServerInstanceAssociatedWithPublicIpRequest](docs/ReplaceServerInstanceAssociatedWithPublicIpRequest.md)
 - [ReplaceServerInstanceAssociatedWithPublicIpResponse](docs/ReplaceServerInstanceAssociatedWithPublicIpResponse.md)
 - [RootPasswordServerInstance](docs/RootPasswordServerInstance.md)
 - [RootPasswordServerInstanceParameter](docs/RootPasswordServerInstanceParameter.md)
 - [ServerInstance](docs/ServerInstance.md)
 - [SetNasVolumeAccessControlRequest](docs/SetNasVolumeAccessControlRequest.md)
 - [SetNasVolumeAccessControlResponse](docs/SetNasVolumeAccessControlResponse.md)
 - [StartServerInstancesRequest](docs/StartServerInstancesRequest.md)
 - [StartServerInstancesResponse](docs/StartServerInstancesResponse.md)
 - [StopServerInstancesRequest](docs/StopServerInstancesRequest.md)
 - [StopServerInstancesResponse](docs/StopServerInstancesResponse.md)
 - [TerminateServerInstancesRequest](docs/TerminateServerInstancesRequest.md)
 - [TerminateServerInstancesResponse](docs/TerminateServerInstancesResponse.md)
 - [Zone](docs/Zone.md)

