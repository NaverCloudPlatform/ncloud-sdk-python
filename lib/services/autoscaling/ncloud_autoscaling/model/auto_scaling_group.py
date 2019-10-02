# coding: utf-8

"""
    autoscaling

    OpenAPI spec version: 2018-11-13T06:27:22Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_autoscaling.model.common_code import CommonCode  # noqa: F401,E501
from ncloud_autoscaling.model.in_auto_scaling_group_server_instance import InAutoScalingGroupServerInstance  # noqa: F401,E501
from ncloud_autoscaling.model.load_balancer_instance_summary import LoadBalancerInstanceSummary  # noqa: F401,E501
from ncloud_autoscaling.model.suspended_process import SuspendedProcess  # noqa: F401,E501
from ncloud_autoscaling.model.zone import Zone  # noqa: F401,E501


class AutoScalingGroup(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'auto_scaling_group_name': 'str',
        'launch_configuration_name': 'str',
        'desired_capacity': 'int',
        'min_size': 'int',
        'max_size': 'int',
        'default_cooldown': 'int',
        'load_balancer_instance_summary_list': 'list[LoadBalancerInstanceSummary]',
        'health_check_grace_period': 'int',
        'health_check_type': 'CommonCode',
        'create_date': 'str',
        'in_auto_scaling_group_server_instance_list': 'list[InAutoScalingGroupServerInstance]',
        'suspended_process_list': 'list[SuspendedProcess]',
        'zone_list': 'list[Zone]'
    }

    attribute_map = {
        'auto_scaling_group_name': 'autoScalingGroupName',
        'launch_configuration_name': 'launchConfigurationName',
        'desired_capacity': 'desiredCapacity',
        'min_size': 'minSize',
        'max_size': 'maxSize',
        'default_cooldown': 'defaultCooldown',
        'load_balancer_instance_summary_list': 'loadBalancerInstanceSummaryList',
        'health_check_grace_period': 'healthCheckGracePeriod',
        'health_check_type': 'healthCheckType',
        'create_date': 'createDate',
        'in_auto_scaling_group_server_instance_list': 'inAutoScalingGroupServerInstanceList',
        'suspended_process_list': 'suspendedProcessList',
        'zone_list': 'zoneList'
    }

    def __init__(self, auto_scaling_group_name=None, launch_configuration_name=None, desired_capacity=None, min_size=None, max_size=None, default_cooldown=None, load_balancer_instance_summary_list=None, health_check_grace_period=None, health_check_type=None, create_date=None, in_auto_scaling_group_server_instance_list=None, suspended_process_list=None, zone_list=None):  # noqa: E501
        """AutoScalingGroup - a model defined in Swagger"""  # noqa: E501

        self._auto_scaling_group_name = None
        self._launch_configuration_name = None
        self._desired_capacity = None
        self._min_size = None
        self._max_size = None
        self._default_cooldown = None
        self._load_balancer_instance_summary_list = None
        self._health_check_grace_period = None
        self._health_check_type = None
        self._create_date = None
        self._in_auto_scaling_group_server_instance_list = None
        self._suspended_process_list = None
        self._zone_list = None
        self.discriminator = None

        if auto_scaling_group_name is not None:
            self.auto_scaling_group_name = auto_scaling_group_name
        if launch_configuration_name is not None:
            self.launch_configuration_name = launch_configuration_name
        if desired_capacity is not None:
            self.desired_capacity = desired_capacity
        if min_size is not None:
            self.min_size = min_size
        if max_size is not None:
            self.max_size = max_size
        if default_cooldown is not None:
            self.default_cooldown = default_cooldown
        if load_balancer_instance_summary_list is not None:
            self.load_balancer_instance_summary_list = load_balancer_instance_summary_list
        if health_check_grace_period is not None:
            self.health_check_grace_period = health_check_grace_period
        if health_check_type is not None:
            self.health_check_type = health_check_type
        if create_date is not None:
            self.create_date = create_date
        if in_auto_scaling_group_server_instance_list is not None:
            self.in_auto_scaling_group_server_instance_list = in_auto_scaling_group_server_instance_list
        if suspended_process_list is not None:
            self.suspended_process_list = suspended_process_list
        if zone_list is not None:
            self.zone_list = zone_list

    @property
    def auto_scaling_group_name(self):
        """Gets the auto_scaling_group_name of this AutoScalingGroup.  # noqa: E501

        오토스케일링그룹명  # noqa: E501

        :return: The auto_scaling_group_name of this AutoScalingGroup.  # noqa: E501
        :rtype: str
        """
        return self._auto_scaling_group_name

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, auto_scaling_group_name):
        """Sets the auto_scaling_group_name of this AutoScalingGroup.

        오토스케일링그룹명  # noqa: E501

        :param auto_scaling_group_name: The auto_scaling_group_name of this AutoScalingGroup.  # noqa: E501
        :type: str
        """

        self._auto_scaling_group_name = auto_scaling_group_name

    @property
    def launch_configuration_name(self):
        """Gets the launch_configuration_name of this AutoScalingGroup.  # noqa: E501

        론치설정명  # noqa: E501

        :return: The launch_configuration_name of this AutoScalingGroup.  # noqa: E501
        :rtype: str
        """
        return self._launch_configuration_name

    @launch_configuration_name.setter
    def launch_configuration_name(self, launch_configuration_name):
        """Sets the launch_configuration_name of this AutoScalingGroup.

        론치설정명  # noqa: E501

        :param launch_configuration_name: The launch_configuration_name of this AutoScalingGroup.  # noqa: E501
        :type: str
        """

        self._launch_configuration_name = launch_configuration_name

    @property
    def desired_capacity(self):
        """Gets the desired_capacity of this AutoScalingGroup.  # noqa: E501

        기대능력치  # noqa: E501

        :return: The desired_capacity of this AutoScalingGroup.  # noqa: E501
        :rtype: int
        """
        return self._desired_capacity

    @desired_capacity.setter
    def desired_capacity(self, desired_capacity):
        """Sets the desired_capacity of this AutoScalingGroup.

        기대능력치  # noqa: E501

        :param desired_capacity: The desired_capacity of this AutoScalingGroup.  # noqa: E501
        :type: int
        """

        self._desired_capacity = desired_capacity

    @property
    def min_size(self):
        """Gets the min_size of this AutoScalingGroup.  # noqa: E501

        최소사이즈  # noqa: E501

        :return: The min_size of this AutoScalingGroup.  # noqa: E501
        :rtype: int
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        """Sets the min_size of this AutoScalingGroup.

        최소사이즈  # noqa: E501

        :param min_size: The min_size of this AutoScalingGroup.  # noqa: E501
        :type: int
        """

        self._min_size = min_size

    @property
    def max_size(self):
        """Gets the max_size of this AutoScalingGroup.  # noqa: E501

        최대사이즈  # noqa: E501

        :return: The max_size of this AutoScalingGroup.  # noqa: E501
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """Sets the max_size of this AutoScalingGroup.

        최대사이즈  # noqa: E501

        :param max_size: The max_size of this AutoScalingGroup.  # noqa: E501
        :type: int
        """

        self._max_size = max_size

    @property
    def default_cooldown(self):
        """Gets the default_cooldown of this AutoScalingGroup.  # noqa: E501


        :return: The default_cooldown of this AutoScalingGroup.  # noqa: E501
        :rtype: int
        """
        return self._default_cooldown

    @default_cooldown.setter
    def default_cooldown(self, default_cooldown):
        """Sets the default_cooldown of this AutoScalingGroup.


        :param default_cooldown: The default_cooldown of this AutoScalingGroup.  # noqa: E501
        :type: int
        """

        self._default_cooldown = default_cooldown

    @property
    def load_balancer_instance_summary_list(self):
        """Gets the load_balancer_instance_summary_list of this AutoScalingGroup.  # noqa: E501

        로드밸런서인스턴스Summary리스트  # noqa: E501

        :return: The load_balancer_instance_summary_list of this AutoScalingGroup.  # noqa: E501
        :rtype: list[LoadBalancerInstanceSummary]
        """
        return self._load_balancer_instance_summary_list

    @load_balancer_instance_summary_list.setter
    def load_balancer_instance_summary_list(self, load_balancer_instance_summary_list):
        """Sets the load_balancer_instance_summary_list of this AutoScalingGroup.

        로드밸런서인스턴스Summary리스트  # noqa: E501

        :param load_balancer_instance_summary_list: The load_balancer_instance_summary_list of this AutoScalingGroup.  # noqa: E501
        :type: list[LoadBalancerInstanceSummary]
        """

        self._load_balancer_instance_summary_list = load_balancer_instance_summary_list

    @property
    def health_check_grace_period(self):
        """Gets the health_check_grace_period of this AutoScalingGroup.  # noqa: E501

        헬스체크보류기간  # noqa: E501

        :return: The health_check_grace_period of this AutoScalingGroup.  # noqa: E501
        :rtype: int
        """
        return self._health_check_grace_period

    @health_check_grace_period.setter
    def health_check_grace_period(self, health_check_grace_period):
        """Sets the health_check_grace_period of this AutoScalingGroup.

        헬스체크보류기간  # noqa: E501

        :param health_check_grace_period: The health_check_grace_period of this AutoScalingGroup.  # noqa: E501
        :type: int
        """

        self._health_check_grace_period = health_check_grace_period

    @property
    def health_check_type(self):
        """Gets the health_check_type of this AutoScalingGroup.  # noqa: E501

        헬스체크유형  # noqa: E501

        :return: The health_check_type of this AutoScalingGroup.  # noqa: E501
        :rtype: CommonCode
        """
        return self._health_check_type

    @health_check_type.setter
    def health_check_type(self, health_check_type):
        """Sets the health_check_type of this AutoScalingGroup.

        헬스체크유형  # noqa: E501

        :param health_check_type: The health_check_type of this AutoScalingGroup.  # noqa: E501
        :type: CommonCode
        """

        self._health_check_type = health_check_type

    @property
    def create_date(self):
        """Gets the create_date of this AutoScalingGroup.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this AutoScalingGroup.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this AutoScalingGroup.

        생성일시  # noqa: E501

        :param create_date: The create_date of this AutoScalingGroup.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def in_auto_scaling_group_server_instance_list(self):
        """Gets the in_auto_scaling_group_server_instance_list of this AutoScalingGroup.  # noqa: E501

        오토스케일링그룹에속한서버인스턴스리스트  # noqa: E501

        :return: The in_auto_scaling_group_server_instance_list of this AutoScalingGroup.  # noqa: E501
        :rtype: list[InAutoScalingGroupServerInstance]
        """
        return self._in_auto_scaling_group_server_instance_list

    @in_auto_scaling_group_server_instance_list.setter
    def in_auto_scaling_group_server_instance_list(self, in_auto_scaling_group_server_instance_list):
        """Sets the in_auto_scaling_group_server_instance_list of this AutoScalingGroup.

        오토스케일링그룹에속한서버인스턴스리스트  # noqa: E501

        :param in_auto_scaling_group_server_instance_list: The in_auto_scaling_group_server_instance_list of this AutoScalingGroup.  # noqa: E501
        :type: list[InAutoScalingGroupServerInstance]
        """

        self._in_auto_scaling_group_server_instance_list = in_auto_scaling_group_server_instance_list

    @property
    def suspended_process_list(self):
        """Gets the suspended_process_list of this AutoScalingGroup.  # noqa: E501

        보류된프로세스리스트  # noqa: E501

        :return: The suspended_process_list of this AutoScalingGroup.  # noqa: E501
        :rtype: list[SuspendedProcess]
        """
        return self._suspended_process_list

    @suspended_process_list.setter
    def suspended_process_list(self, suspended_process_list):
        """Sets the suspended_process_list of this AutoScalingGroup.

        보류된프로세스리스트  # noqa: E501

        :param suspended_process_list: The suspended_process_list of this AutoScalingGroup.  # noqa: E501
        :type: list[SuspendedProcess]
        """

        self._suspended_process_list = suspended_process_list

    @property
    def zone_list(self):
        """Gets the zone_list of this AutoScalingGroup.  # noqa: E501

        ZONE리스트  # noqa: E501

        :return: The zone_list of this AutoScalingGroup.  # noqa: E501
        :rtype: list[Zone]
        """
        return self._zone_list

    @zone_list.setter
    def zone_list(self, zone_list):
        """Sets the zone_list of this AutoScalingGroup.

        ZONE리스트  # noqa: E501

        :param zone_list: The zone_list of this AutoScalingGroup.  # noqa: E501
        :type: list[Zone]
        """

        self._zone_list = zone_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AutoScalingGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
