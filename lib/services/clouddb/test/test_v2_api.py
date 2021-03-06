# coding: utf-8

"""
    clouddb

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ncloud_clouddb
from ncloud_clouddb.api.v2_api import V2Api  # noqa: E501
from ncloud_clouddb.rest import ApiException


class TestV2Api(unittest.TestCase):
    """V2Api unit test stubs"""

    def setUp(self):
        configuration = ncloud_clouddb.Configuration()
        configuration.access_key = "YOUR ACCESS KEY"
        configuration.secret_key = "YOUR SECRET KEY"
        self.api = ncloud_clouddb.api.v2_api.V2Api(ncloud_clouddb.ApiClient(configuration))  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cloud_db_instance(self):
        """Test case for create_cloud_db_instance
        create_cloud_db_instance_request = ncloud_clouddb.CreateCloudDBInstanceRequest()
        try:
            api_response = self.api.create_cloud_db_instance(create_cloud_db_instance_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->create_cloud_db_instance: %s\n" % e)
        """
        pass

    def test_delete_cloud_db_server_instance(self):
        """Test case for delete_cloud_db_server_instance
        delete_cloud_db_server_instance_request = ncloud_clouddb.DeleteCloudDBServerInstanceRequest()
        try:
            api_response = self.api.delete_cloud_db_server_instance(delete_cloud_db_server_instance_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->delete_cloud_db_server_instance: %s\n" % e)
        """
        pass

    def test_download_dms_file(self):
        """Test case for download_dms_file
        download_dms_file_request = ncloud_clouddb.DownloadDmsFileRequest()
        try:
            api_response = self.api.download_dms_file(download_dms_file_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->download_dms_file: %s\n" % e)
        """
        pass

    def test_flush_cloud_db_instance(self):
        """Test case for flush_cloud_db_instance
        flush_cloud_db_instance_request = ncloud_clouddb.FlushCloudDBInstanceRequest()
        try:
            api_response = self.api.flush_cloud_db_instance(flush_cloud_db_instance_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->flush_cloud_db_instance: %s\n" % e)
        """
        pass

    def test_get_backup_list(self):
        """Test case for get_backup_list
        get_backup_list_request = ncloud_clouddb.GetBackupListRequest()
        try:
            api_response = self.api.get_backup_list(get_backup_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_backup_list: %s\n" % e)
        """
        pass

    def test_get_cloud_db_config_group_list(self):
        """Test case for get_cloud_db_config_group_list
        get_cloud_db_config_group_list_request = ncloud_clouddb.GetCloudDBConfigGroupListRequest()
        try:
            api_response = self.api.get_cloud_db_config_group_list(get_cloud_db_config_group_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_cloud_db_config_group_list: %s\n" % e)
        """
        pass

    def test_get_cloud_db_image_product_list(self):
        """Test case for get_cloud_db_image_product_list
        get_cloud_db_image_product_list_request = ncloud_clouddb.GetCloudDBImageProductListRequest()
        try:
            api_response = self.api.get_cloud_db_image_product_list(get_cloud_db_image_product_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_cloud_db_image_product_list: %s\n" % e)
        """
        pass

    def test_get_cloud_db_instance_list(self):
        """Test case for get_cloud_db_instance_list
        get_cloud_db_instance_list_request = ncloud_clouddb.GetCloudDBInstanceListRequest()
        try:
            api_response = self.api.get_cloud_db_instance_list(get_cloud_db_instance_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_cloud_db_instance_list: %s\n" % e)
        """
        pass

    def test_get_cloud_db_product_list(self):
        """Test case for get_cloud_db_product_list
        get_cloud_db_product_list_request = ncloud_clouddb.GetCloudDBProductListRequest()
        try:
            api_response = self.api.get_cloud_db_product_list(get_cloud_db_product_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_cloud_db_product_list: %s\n" % e)
        """
        pass

    def test_get_dms_operation(self):
        """Test case for get_dms_operation
        get_dms_operation_request = ncloud_clouddb.GetDmsOperationRequest()
        try:
            api_response = self.api.get_dms_operation(get_dms_operation_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_dms_operation: %s\n" % e)
        """
        pass

    def test_get_object_storage_backup_list(self):
        """Test case for get_object_storage_backup_list
        get_object_storage_backup_list_request = ncloud_clouddb.GetObjectStorageBackupListRequest()
        try:
            api_response = self.api.get_object_storage_backup_list(get_object_storage_backup_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_object_storage_backup_list: %s\n" % e)
        """
        pass

    def test_reboot_cloud_db_server_instance(self):
        """Test case for reboot_cloud_db_server_instance
        reboot_cloud_db_server_instance_request = ncloud_clouddb.RebootCloudDBServerInstanceRequest()
        try:
            api_response = self.api.reboot_cloud_db_server_instance(reboot_cloud_db_server_instance_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->reboot_cloud_db_server_instance: %s\n" % e)
        """
        pass

    def test_restore_dms_database(self):
        """Test case for restore_dms_database
        restore_dms_database_request = ncloud_clouddb.RestoreDmsDatabaseRequest()
        try:
            api_response = self.api.restore_dms_database(restore_dms_database_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->restore_dms_database: %s\n" % e)
        """
        pass

    def test_restore_dms_transaction_log(self):
        """Test case for restore_dms_transaction_log
        restore_dms_transaction_log_request = ncloud_clouddb.RestoreDmsTransactionLogRequest()
        try:
            api_response = self.api.restore_dms_transaction_log(restore_dms_transaction_log_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->restore_dms_transaction_log: %s\n" % e)
        """
        pass

    def test_set_object_storage_info(self):
        """Test case for set_object_storage_info
        set_object_storage_info_request = ncloud_clouddb.SetObjectStorageInfoRequest()
        try:
            api_response = self.api.set_object_storage_info(set_object_storage_info_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->set_object_storage_info: %s\n" % e)
        """
        pass

    def test_upload_dms_file(self):
        """Test case for upload_dms_file
        upload_dms_file_request = ncloud_clouddb.UploadDmsFileRequest()
        try:
            api_response = self.api.upload_dms_file(upload_dms_file_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->upload_dms_file: %s\n" % e)
        """
        pass


if __name__ == '__main__':
    unittest.main()
