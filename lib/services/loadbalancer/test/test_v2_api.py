# coding: utf-8

"""
    loadbalancer

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ncloud_loadbalancer
from ncloud_loadbalancer.api.v2_api import V2Api  # noqa: E501
from ncloud_loadbalancer.rest import ApiException


class TestV2Api(unittest.TestCase):
    """V2Api unit test stubs"""

    def setUp(self):
        configuration = ncloud_loadbalancer.Configuration()
        configuration.access_key = "YOUR ACCESS KEY"
        configuration.secret_key = "YOUR SECRET KEY"
        self.api = ncloud_loadbalancer.api.v2_api.V2Api(ncloud_loadbalancer.ApiClient(configuration))  # noqa: E501

    def tearDown(self):
        pass

    def test_add_load_balancer_ssl_certificate(self):
        """Test case for add_load_balancer_ssl_certificate
        add_load_balancer_ssl_certificate_request = ncloud_loadbalancer.AddLoadBalancerSslCertificateRequest()
        try:
            api_response = self.api.add_load_balancer_ssl_certificate(add_load_balancer_ssl_certificate_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->add_load_balancer_ssl_certificate: %s\n" % e)
        """
        pass

    def test_change_load_balanced_server_instances(self):
        """Test case for change_load_balanced_server_instances
        change_load_balanced_server_instances_request = ncloud_loadbalancer.ChangeLoadBalancedServerInstancesRequest()
        try:
            api_response = self.api.change_load_balanced_server_instances(change_load_balanced_server_instances_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->change_load_balanced_server_instances: %s\n" % e)
        """
        pass

    def test_change_load_balancer_instance_configuration(self):
        """Test case for change_load_balancer_instance_configuration
        change_load_balancer_instance_configuration_request = ncloud_loadbalancer.ChangeLoadBalancerInstanceConfigurationRequest()
        try:
            api_response = self.api.change_load_balancer_instance_configuration(change_load_balancer_instance_configuration_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->change_load_balancer_instance_configuration: %s\n" % e)
        """
        pass

    def test_create_load_balancer_instance(self):
        """Test case for create_load_balancer_instance
        create_load_balancer_instance_request = ncloud_loadbalancer.CreateLoadBalancerInstanceRequest()
        try:
            api_response = self.api.create_load_balancer_instance(create_load_balancer_instance_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->create_load_balancer_instance: %s\n" % e)
        """
        pass

    def test_delete_load_balancer_instances(self):
        """Test case for delete_load_balancer_instances
        delete_load_balancer_instances_request = ncloud_loadbalancer.DeleteLoadBalancerInstancesRequest()
        try:
            api_response = self.api.delete_load_balancer_instances(delete_load_balancer_instances_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->delete_load_balancer_instances: %s\n" % e)
        """
        pass

    def test_delete_load_balancer_ssl_certificate(self):
        """Test case for delete_load_balancer_ssl_certificate
        delete_load_balancer_ssl_certificate_request = ncloud_loadbalancer.DeleteLoadBalancerSslCertificateRequest()
        try:
            api_response = self.api.delete_load_balancer_ssl_certificate(delete_load_balancer_ssl_certificate_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->delete_load_balancer_ssl_certificate: %s\n" % e)
        """
        pass

    def test_get_load_balanced_server_instance_list(self):
        """Test case for get_load_balanced_server_instance_list
        get_load_balanced_server_instance_list_request = ncloud_loadbalancer.GetLoadBalancedServerInstanceListRequest()
        try:
            api_response = self.api.get_load_balanced_server_instance_list(get_load_balanced_server_instance_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_load_balanced_server_instance_list: %s\n" % e)
        """
        pass

    def test_get_load_balancer_instance_list(self):
        """Test case for get_load_balancer_instance_list
        get_load_balancer_instance_list_request = ncloud_loadbalancer.GetLoadBalancerInstanceListRequest()
        try:
            api_response = self.api.get_load_balancer_instance_list(get_load_balancer_instance_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_load_balancer_instance_list: %s\n" % e)
        """
        pass

    def test_get_load_balancer_ssl_certificate_list(self):
        """Test case for get_load_balancer_ssl_certificate_list
        get_load_balancer_ssl_certificate_list_request = ncloud_loadbalancer.GetLoadBalancerSslCertificateListRequest()
        try:
            api_response = self.api.get_load_balancer_ssl_certificate_list(get_load_balancer_ssl_certificate_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_load_balancer_ssl_certificate_list: %s\n" % e)
        """
        pass

    def test_get_load_balancer_target_server_instance_list(self):
        """Test case for get_load_balancer_target_server_instance_list
        get_load_balancer_target_server_instance_list_request = ncloud_loadbalancer.GetLoadBalancerTargetServerInstanceListRequest()
        try:
            api_response = self.api.get_load_balancer_target_server_instance_list(get_load_balancer_target_server_instance_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_load_balancer_target_server_instance_list: %s\n" % e)
        """
        pass


if __name__ == '__main__':
    unittest.main()
