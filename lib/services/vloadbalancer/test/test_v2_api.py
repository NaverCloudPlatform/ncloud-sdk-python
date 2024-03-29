# coding: utf-8

"""
    vloadbalancer

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ncloud_vloadbalancer
from ncloud_vloadbalancer.api.v2_api import V2Api  # noqa: E501
from ncloud_vloadbalancer.rest import ApiException


class TestV2Api(unittest.TestCase):
    """V2Api unit test stubs"""

    def setUp(self):
        configuration = ncloud_vloadbalancer.Configuration()
        configuration.access_key = "YOUR ACCESS KEY"
        configuration.secret_key = "YOUR SECRET KEY"
        self.api = ncloud_vloadbalancer.api.v2_api.V2Api(ncloud_vloadbalancer.ApiClient(configuration))  # noqa: E501

    def tearDown(self):
        pass

    def test_add_target(self):
        """Test case for add_target
        add_target_request = ncloud_vloadbalancer.AddTargetRequest()
        try:
            api_response = self.api.add_target(add_target_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->add_target: %s\n" % e)
        """
        pass

    def test_change_load_balancer_instance_configuration(self):
        """Test case for change_load_balancer_instance_configuration
        change_load_balancer_instance_configuration_request = ncloud_vloadbalancer.ChangeLoadBalancerInstanceConfigurationRequest()
        try:
            api_response = self.api.change_load_balancer_instance_configuration(change_load_balancer_instance_configuration_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->change_load_balancer_instance_configuration: %s\n" % e)
        """
        pass

    def test_change_load_balancer_listener_configuration(self):
        """Test case for change_load_balancer_listener_configuration
        change_load_balancer_listener_configuration_request = ncloud_vloadbalancer.ChangeLoadBalancerListenerConfigurationRequest()
        try:
            api_response = self.api.change_load_balancer_listener_configuration(change_load_balancer_listener_configuration_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->change_load_balancer_listener_configuration: %s\n" % e)
        """
        pass

    def test_change_target_group_configuration(self):
        """Test case for change_target_group_configuration
        change_target_group_configuration_request = ncloud_vloadbalancer.ChangeTargetGroupConfigurationRequest()
        try:
            api_response = self.api.change_target_group_configuration(change_target_group_configuration_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->change_target_group_configuration: %s\n" % e)
        """
        pass

    def test_change_target_group_health_check_configuration(self):
        """Test case for change_target_group_health_check_configuration
        change_target_group_health_check_configuration_request = ncloud_vloadbalancer.ChangeTargetGroupHealthCheckConfigurationRequest()
        try:
            api_response = self.api.change_target_group_health_check_configuration(change_target_group_health_check_configuration_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->change_target_group_health_check_configuration: %s\n" % e)
        """
        pass

    def test_create_load_balancer_instance(self):
        """Test case for create_load_balancer_instance
        create_load_balancer_instance_request = ncloud_vloadbalancer.CreateLoadBalancerInstanceRequest()
        try:
            api_response = self.api.create_load_balancer_instance(create_load_balancer_instance_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->create_load_balancer_instance: %s\n" % e)
        """
        pass

    def test_create_load_balancer_listener(self):
        """Test case for create_load_balancer_listener
        create_load_balancer_listener_request = ncloud_vloadbalancer.CreateLoadBalancerListenerRequest()
        try:
            api_response = self.api.create_load_balancer_listener(create_load_balancer_listener_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->create_load_balancer_listener: %s\n" % e)
        """
        pass

    def test_create_target_group(self):
        """Test case for create_target_group
        create_target_group_request = ncloud_vloadbalancer.CreateTargetGroupRequest()
        try:
            api_response = self.api.create_target_group(create_target_group_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->create_target_group: %s\n" % e)
        """
        pass

    def test_delete_load_balancer_instances(self):
        """Test case for delete_load_balancer_instances
        delete_load_balancer_instances_request = ncloud_vloadbalancer.DeleteLoadBalancerInstancesRequest()
        try:
            api_response = self.api.delete_load_balancer_instances(delete_load_balancer_instances_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->delete_load_balancer_instances: %s\n" % e)
        """
        pass

    def test_delete_load_balancer_listeners(self):
        """Test case for delete_load_balancer_listeners
        delete_load_balancer_listeners_request = ncloud_vloadbalancer.DeleteLoadBalancerListenersRequest()
        try:
            api_response = self.api.delete_load_balancer_listeners(delete_load_balancer_listeners_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->delete_load_balancer_listeners: %s\n" % e)
        """
        pass

    def test_delete_target_groups(self):
        """Test case for delete_target_groups
        delete_target_groups_request = ncloud_vloadbalancer.DeleteTargetGroupsRequest()
        try:
            api_response = self.api.delete_target_groups(delete_target_groups_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->delete_target_groups: %s\n" % e)
        """
        pass

    def test_get_load_balancer_instance_detail(self):
        """Test case for get_load_balancer_instance_detail
        get_load_balancer_instance_detail_request = ncloud_vloadbalancer.GetLoadBalancerInstanceDetailRequest()
        try:
            api_response = self.api.get_load_balancer_instance_detail(get_load_balancer_instance_detail_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_load_balancer_instance_detail: %s\n" % e)
        """
        pass

    def test_get_load_balancer_instance_list(self):
        """Test case for get_load_balancer_instance_list
        get_load_balancer_instance_list_request = ncloud_vloadbalancer.GetLoadBalancerInstanceListRequest()
        try:
            api_response = self.api.get_load_balancer_instance_list(get_load_balancer_instance_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_load_balancer_instance_list: %s\n" % e)
        """
        pass

    def test_get_load_balancer_listener_list(self):
        """Test case for get_load_balancer_listener_list
        get_load_balancer_listener_list_request = ncloud_vloadbalancer.GetLoadBalancerListenerListRequest()
        try:
            api_response = self.api.get_load_balancer_listener_list(get_load_balancer_listener_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_load_balancer_listener_list: %s\n" % e)
        """
        pass

    def test_get_load_balancer_rule_list(self):
        """Test case for get_load_balancer_rule_list
        get_load_balancer_rule_list_request = ncloud_vloadbalancer.GetLoadBalancerRuleListRequest()
        try:
            api_response = self.api.get_load_balancer_rule_list(get_load_balancer_rule_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_load_balancer_rule_list: %s\n" % e)
        """
        pass

    def test_get_target_group_detail(self):
        """Test case for get_target_group_detail
        get_target_group_detail_request = ncloud_vloadbalancer.GetTargetGroupDetailRequest()
        try:
            api_response = self.api.get_target_group_detail(get_target_group_detail_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_target_group_detail: %s\n" % e)
        """
        pass

    def test_get_target_group_list(self):
        """Test case for get_target_group_list
        get_target_group_list_request = ncloud_vloadbalancer.GetTargetGroupListRequest()
        try:
            api_response = self.api.get_target_group_list(get_target_group_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_target_group_list: %s\n" % e)
        """
        pass

    def test_get_target_list(self):
        """Test case for get_target_list
        get_target_list_request = ncloud_vloadbalancer.GetTargetListRequest()
        try:
            api_response = self.api.get_target_list(get_target_list_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->get_target_list: %s\n" % e)
        """
        pass

    def test_remove_target(self):
        """Test case for remove_target
        remove_target_request = ncloud_vloadbalancer.RemoveTargetRequest()
        try:
            api_response = self.api.remove_target(remove_target_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->remove_target: %s\n" % e)
        """
        pass

    def test_set_load_balancer_description(self):
        """Test case for set_load_balancer_description
        set_load_balancer_description_request = ncloud_vloadbalancer.SetLoadBalancerDescriptionRequest()
        try:
            api_response = self.api.set_load_balancer_description(set_load_balancer_description_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->set_load_balancer_description: %s\n" % e)
        """
        pass

    def test_set_load_balancer_instance_subnet(self):
        """Test case for set_load_balancer_instance_subnet
        set_load_balancer_instance_subnet_request = ncloud_vloadbalancer.SetLoadBalancerInstanceSubnetRequest()
        try:
            api_response = self.api.set_load_balancer_instance_subnet(set_load_balancer_instance_subnet_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->set_load_balancer_instance_subnet: %s\n" % e)
        """
        pass

    def test_set_target(self):
        """Test case for set_target
        set_target_request = ncloud_vloadbalancer.SetTargetRequest()
        try:
            api_response = self.api.set_target(set_target_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->set_target: %s\n" % e)
        """
        pass

    def test_set_target_group_description(self):
        """Test case for set_target_group_description
        set_target_group_description_request = ncloud_vloadbalancer.SetTargetGroupDescriptionRequest()
        try:
            api_response = self.api.set_target_group_description(set_target_group_description_request)
            print(api_response)
        except ApiException as e:
            print("Exception when calling V2Api->set_target_group_description: %s\n" % e)
        """
        pass


if __name__ == '__main__':
    unittest.main()
