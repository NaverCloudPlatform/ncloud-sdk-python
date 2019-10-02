# ncloud_clouddb.V2Api

All URIs are relative to *https://ncloud.apigw.ntruss.com/clouddb/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_db_instance**](V2Api.md#create_cloud_db_instance) | **POST** /createCloudDBInstance | 
[**delete_cloud_db_server_instance**](V2Api.md#delete_cloud_db_server_instance) | **POST** /deleteCloudDBServerInstance | 
[**download_dms_file**](V2Api.md#download_dms_file) | **POST** /downloadDmsFile | 
[**flush_cloud_db_instance**](V2Api.md#flush_cloud_db_instance) | **POST** /flushCloudDBInstance | 
[**get_backup_list**](V2Api.md#get_backup_list) | **POST** /getBackupList | 
[**get_cloud_db_config_group_list**](V2Api.md#get_cloud_db_config_group_list) | **POST** /getCloudDBConfigGroupList | 
[**get_cloud_db_image_product_list**](V2Api.md#get_cloud_db_image_product_list) | **POST** /getCloudDBImageProductList | 
[**get_cloud_db_instance_list**](V2Api.md#get_cloud_db_instance_list) | **POST** /getCloudDBInstanceList | 
[**get_cloud_db_product_list**](V2Api.md#get_cloud_db_product_list) | **POST** /getCloudDBProductList | 
[**get_dms_operation**](V2Api.md#get_dms_operation) | **POST** /getDmsOperation | 
[**get_object_storage_backup_list**](V2Api.md#get_object_storage_backup_list) | **POST** /getObjectStorageBackupList | 
[**reboot_cloud_db_server_instance**](V2Api.md#reboot_cloud_db_server_instance) | **POST** /rebootCloudDBServerInstance | 
[**restore_dms_database**](V2Api.md#restore_dms_database) | **POST** /restoreDmsDatabase | 
[**restore_dms_transaction_log**](V2Api.md#restore_dms_transaction_log) | **POST** /restoreDmsTransactionLog | 
[**set_object_storage_info**](V2Api.md#set_object_storage_info) | **POST** /setObjectStorageInfo | 
[**upload_dms_file**](V2Api.md#upload_dms_file) | **POST** /uploadDmsFile | 


# **create_cloud_db_instance**
> CreateCloudDBInstanceResponse create_cloud_db_instance(create_cloud_db_instance_request)



CloudDB인스턴스생성

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
create_cloud_db_instance_request = ncloud_clouddb.CreateCloudDBInstanceRequest() # CreateCloudDBInstanceRequest | createCloudDBInstanceRequest

try:
    api_response = api_instance.create_cloud_db_instance(create_cloud_db_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->create_cloud_db_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_cloud_db_instance_request** | [**CreateCloudDBInstanceRequest**](CreateCloudDBInstanceRequest.md)| createCloudDBInstanceRequest | 

### Return type

[**CreateCloudDBInstanceResponse**](CreateCloudDBInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_db_server_instance**
> DeleteCloudDBServerInstanceResponse delete_cloud_db_server_instance(delete_cloud_db_server_instance_request)



CloudDB서버인스턴스삭제

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
delete_cloud_db_server_instance_request = ncloud_clouddb.DeleteCloudDBServerInstanceRequest() # DeleteCloudDBServerInstanceRequest | deleteCloudDBServerInstanceRequest

try:
    api_response = api_instance.delete_cloud_db_server_instance(delete_cloud_db_server_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->delete_cloud_db_server_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_cloud_db_server_instance_request** | [**DeleteCloudDBServerInstanceRequest**](DeleteCloudDBServerInstanceRequest.md)| deleteCloudDBServerInstanceRequest | 

### Return type

[**DeleteCloudDBServerInstanceResponse**](DeleteCloudDBServerInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_dms_file**
> DownloadDmsFileResponse download_dms_file(download_dms_file_request)



DMS파일다운로드

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
download_dms_file_request = ncloud_clouddb.DownloadDmsFileRequest() # DownloadDmsFileRequest | downloadDmsFileRequest

try:
    api_response = api_instance.download_dms_file(download_dms_file_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->download_dms_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_dms_file_request** | [**DownloadDmsFileRequest**](DownloadDmsFileRequest.md)| downloadDmsFileRequest | 

### Return type

[**DownloadDmsFileResponse**](DownloadDmsFileResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flush_cloud_db_instance**
> FlushCloudDBInstanceResponse flush_cloud_db_instance(flush_cloud_db_instance_request)



CloudDB Flush

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
flush_cloud_db_instance_request = ncloud_clouddb.FlushCloudDBInstanceRequest() # FlushCloudDBInstanceRequest | flushCloudDBInstanceRequest

try:
    api_response = api_instance.flush_cloud_db_instance(flush_cloud_db_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->flush_cloud_db_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flush_cloud_db_instance_request** | [**FlushCloudDBInstanceRequest**](FlushCloudDBInstanceRequest.md)| flushCloudDBInstanceRequest | 

### Return type

[**FlushCloudDBInstanceResponse**](FlushCloudDBInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_list**
> GetBackupListResponse get_backup_list(get_backup_list_request)



백업리스트조회

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
get_backup_list_request = ncloud_clouddb.GetBackupListRequest() # GetBackupListRequest | getBackupListRequest

try:
    api_response = api_instance.get_backup_list(get_backup_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_backup_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_backup_list_request** | [**GetBackupListRequest**](GetBackupListRequest.md)| getBackupListRequest | 

### Return type

[**GetBackupListResponse**](GetBackupListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_db_config_group_list**
> GetCloudDBConfigGroupListResponse get_cloud_db_config_group_list(get_cloud_db_config_group_list_request)



CloudDB설정그룹리스트조회

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
get_cloud_db_config_group_list_request = ncloud_clouddb.GetCloudDBConfigGroupListRequest() # GetCloudDBConfigGroupListRequest | getCloudDBConfigGroupListRequest

try:
    api_response = api_instance.get_cloud_db_config_group_list(get_cloud_db_config_group_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_cloud_db_config_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cloud_db_config_group_list_request** | [**GetCloudDBConfigGroupListRequest**](GetCloudDBConfigGroupListRequest.md)| getCloudDBConfigGroupListRequest | 

### Return type

[**GetCloudDBConfigGroupListResponse**](GetCloudDBConfigGroupListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_db_image_product_list**
> GetCloudDBImageProductListResponse get_cloud_db_image_product_list(get_cloud_db_image_product_list_request)



CloudDB이미지상품리스트

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
get_cloud_db_image_product_list_request = ncloud_clouddb.GetCloudDBImageProductListRequest() # GetCloudDBImageProductListRequest | getCloudDBImageProductListRequest

try:
    api_response = api_instance.get_cloud_db_image_product_list(get_cloud_db_image_product_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_cloud_db_image_product_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cloud_db_image_product_list_request** | [**GetCloudDBImageProductListRequest**](GetCloudDBImageProductListRequest.md)| getCloudDBImageProductListRequest | 

### Return type

[**GetCloudDBImageProductListResponse**](GetCloudDBImageProductListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_db_instance_list**
> GetCloudDBInstanceListResponse get_cloud_db_instance_list(get_cloud_db_instance_list_request)



CloudDB인스턴스리스트조회

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
get_cloud_db_instance_list_request = ncloud_clouddb.GetCloudDBInstanceListRequest() # GetCloudDBInstanceListRequest | getCloudDBInstanceListRequest

try:
    api_response = api_instance.get_cloud_db_instance_list(get_cloud_db_instance_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_cloud_db_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cloud_db_instance_list_request** | [**GetCloudDBInstanceListRequest**](GetCloudDBInstanceListRequest.md)| getCloudDBInstanceListRequest | 

### Return type

[**GetCloudDBInstanceListResponse**](GetCloudDBInstanceListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_db_product_list**
> GetCloudDBProductListResponse get_cloud_db_product_list(get_cloud_db_product_list_request)



CloudDB상품리스트조회

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
get_cloud_db_product_list_request = ncloud_clouddb.GetCloudDBProductListRequest() # GetCloudDBProductListRequest | getCloudDBProductListRequest

try:
    api_response = api_instance.get_cloud_db_product_list(get_cloud_db_product_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_cloud_db_product_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cloud_db_product_list_request** | [**GetCloudDBProductListRequest**](GetCloudDBProductListRequest.md)| getCloudDBProductListRequest | 

### Return type

[**GetCloudDBProductListResponse**](GetCloudDBProductListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dms_operation**
> GetDmsOperationResponse get_dms_operation(get_dms_operation_request)



DMS상태조회

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
get_dms_operation_request = ncloud_clouddb.GetDmsOperationRequest() # GetDmsOperationRequest | getDmsOperationRequest

try:
    api_response = api_instance.get_dms_operation(get_dms_operation_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_dms_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_dms_operation_request** | [**GetDmsOperationRequest**](GetDmsOperationRequest.md)| getDmsOperationRequest | 

### Return type

[**GetDmsOperationResponse**](GetDmsOperationResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_backup_list**
> GetObjectStorageBackupListResponse get_object_storage_backup_list(get_object_storage_backup_list_request)



오브젝트스토리지백업리스트조회

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
get_object_storage_backup_list_request = ncloud_clouddb.GetObjectStorageBackupListRequest() # GetObjectStorageBackupListRequest | getObjectStorageBackupListRequest

try:
    api_response = api_instance.get_object_storage_backup_list(get_object_storage_backup_list_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_object_storage_backup_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_object_storage_backup_list_request** | [**GetObjectStorageBackupListRequest**](GetObjectStorageBackupListRequest.md)| getObjectStorageBackupListRequest | 

### Return type

[**GetObjectStorageBackupListResponse**](GetObjectStorageBackupListResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reboot_cloud_db_server_instance**
> RebootCloudDBServerInstanceResponse reboot_cloud_db_server_instance(reboot_cloud_db_server_instance_request)



CloudDB서버인스턴스재부팅

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
reboot_cloud_db_server_instance_request = ncloud_clouddb.RebootCloudDBServerInstanceRequest() # RebootCloudDBServerInstanceRequest | rebootCloudDBServerInstanceRequest

try:
    api_response = api_instance.reboot_cloud_db_server_instance(reboot_cloud_db_server_instance_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->reboot_cloud_db_server_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reboot_cloud_db_server_instance_request** | [**RebootCloudDBServerInstanceRequest**](RebootCloudDBServerInstanceRequest.md)| rebootCloudDBServerInstanceRequest | 

### Return type

[**RebootCloudDBServerInstanceResponse**](RebootCloudDBServerInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_dms_database**
> RestoreDmsDatabaseResponse restore_dms_database(restore_dms_database_request)



DMS데이터베이스복구

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
restore_dms_database_request = ncloud_clouddb.RestoreDmsDatabaseRequest() # RestoreDmsDatabaseRequest | restoreDmsDatabaseRequest

try:
    api_response = api_instance.restore_dms_database(restore_dms_database_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->restore_dms_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restore_dms_database_request** | [**RestoreDmsDatabaseRequest**](RestoreDmsDatabaseRequest.md)| restoreDmsDatabaseRequest | 

### Return type

[**RestoreDmsDatabaseResponse**](RestoreDmsDatabaseResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_dms_transaction_log**
> RestoreDmsTransactionLogResponse restore_dms_transaction_log(restore_dms_transaction_log_request)



DMS트랜잭션로그복구

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
restore_dms_transaction_log_request = ncloud_clouddb.RestoreDmsTransactionLogRequest() # RestoreDmsTransactionLogRequest | restoreDmsTransactionLogRequest

try:
    api_response = api_instance.restore_dms_transaction_log(restore_dms_transaction_log_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->restore_dms_transaction_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restore_dms_transaction_log_request** | [**RestoreDmsTransactionLogRequest**](RestoreDmsTransactionLogRequest.md)| restoreDmsTransactionLogRequest | 

### Return type

[**RestoreDmsTransactionLogResponse**](RestoreDmsTransactionLogResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_object_storage_info**
> SetObjectStorageInfoResponse set_object_storage_info(set_object_storage_info_request)



오브젝트스토리지정보설정

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
set_object_storage_info_request = ncloud_clouddb.SetObjectStorageInfoRequest() # SetObjectStorageInfoRequest | setObjectStorageInfoRequest

try:
    api_response = api_instance.set_object_storage_info(set_object_storage_info_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->set_object_storage_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_object_storage_info_request** | [**SetObjectStorageInfoRequest**](SetObjectStorageInfoRequest.md)| setObjectStorageInfoRequest | 

### Return type

[**SetObjectStorageInfoResponse**](SetObjectStorageInfoResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_dms_file**
> UploadDmsFileResponse upload_dms_file(upload_dms_file_request)



DMS파일업로드

### Example
```python
from __future__ import print_function
import ncloud_clouddb
from ncloud_clouddb.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_clouddb.V2Api(ncloud_clouddb.ApiClient(configuration))
upload_dms_file_request = ncloud_clouddb.UploadDmsFileRequest() # UploadDmsFileRequest | uploadDmsFileRequest

try:
    api_response = api_instance.upload_dms_file(upload_dms_file_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->upload_dms_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_dms_file_request** | [**UploadDmsFileRequest**](UploadDmsFileRequest.md)| uploadDmsFileRequest | 

### Return type

[**UploadDmsFileResponse**](UploadDmsFileResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

