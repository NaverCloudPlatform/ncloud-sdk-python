# coding: utf-8

"""
    autoscaling

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateAutoScalingGroupRequest(object):
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
        'load_balancer_name_list': 'list[str]',
        'health_check_grace_period': 'int',
        'health_check_type_code': 'str',
        'zone_no_list': 'list[str]'
    }

    attribute_map = {
        'auto_scaling_group_name': 'autoScalingGroupName',
        'launch_configuration_name': 'launchConfigurationName',
        'desired_capacity': 'desiredCapacity',
        'min_size': 'minSize',
        'max_size': 'maxSize',
        'default_cooldown': 'defaultCooldown',
        'load_balancer_name_list': 'loadBalancerNameList',
        'health_check_grace_period': 'healthCheckGracePeriod',
        'health_check_type_code': 'healthCheckTypeCode',
        'zone_no_list': 'zoneNoList'
    }

    def __init__(self, auto_scaling_group_name=None, launch_configuration_name=None, desired_capacity=None, min_size=None, max_size=None, default_cooldown=None, load_balancer_name_list=None, health_check_grace_period=None, health_check_type_code=None, zone_no_list=None):  # noqa: E501
        """CreateAutoScalingGroupRequest - a model defined in Swagger"""  # noqa: E501

        self._auto_scaling_group_name = None
        self._launch_configuration_name = None
        self._desired_capacity = None
        self._min_size = None
        self._max_size = None
        self._default_cooldown = None
        self._load_balancer_name_list = None
        self._health_check_grace_period = None
        self._health_check_type_code = None
        self._zone_no_list = None
        self.discriminator = None

        if auto_scaling_group_name is not None:
            self.auto_scaling_group_name = auto_scaling_group_name
        self.launch_configuration_name = launch_configuration_name
        if desired_capacity is not None:
            self.desired_capacity = desired_capacity
        self.min_size = min_size
        self.max_size = max_size
        if default_cooldown is not None:
            self.default_cooldown = default_cooldown
        if load_balancer_name_list is not None:
            self.load_balancer_name_list = load_balancer_name_list
        if health_check_grace_period is not None:
            self.health_check_grace_period = health_check_grace_period
        if health_check_type_code is not None:
            self.health_check_type_code = health_check_type_code
        self.zone_no_list = zone_no_list

    @property
    def auto_scaling_group_name(self):
        """Gets the auto_scaling_group_name of this CreateAutoScalingGroupRequest.  # noqa: E501

        오토스케일링그룹명  # noqa: E501

        :return: The auto_scaling_group_name of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_scaling_group_name

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, auto_scaling_group_name):
        """Sets the auto_scaling_group_name of this CreateAutoScalingGroupRequest.

        오토스케일링그룹명  # noqa: E501

        :param auto_scaling_group_name: The auto_scaling_group_name of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: str
        """

        self._auto_scaling_group_name = auto_scaling_group_name

    @property
    def launch_configuration_name(self):
        """Gets the launch_configuration_name of this CreateAutoScalingGroupRequest.  # noqa: E501

        론치설정명  # noqa: E501

        :return: The launch_configuration_name of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._launch_configuration_name

    @launch_configuration_name.setter
    def launch_configuration_name(self, launch_configuration_name):
        """Sets the launch_configuration_name of this CreateAutoScalingGroupRequest.

        론치설정명  # noqa: E501

        :param launch_configuration_name: The launch_configuration_name of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: str
        """
        if launch_configuration_name is None:
            raise ValueError("Invalid value for `launch_configuration_name`, must not be `None`")  # noqa: E501

        self._launch_configuration_name = launch_configuration_name

    @property
    def desired_capacity(self):
        """Gets the desired_capacity of this CreateAutoScalingGroupRequest.  # noqa: E501

        기대용량치  # noqa: E501

        :return: The desired_capacity of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._desired_capacity

    @desired_capacity.setter
    def desired_capacity(self, desired_capacity):
        """Sets the desired_capacity of this CreateAutoScalingGroupRequest.

        기대용량치  # noqa: E501

        :param desired_capacity: The desired_capacity of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: int
        """

        self._desired_capacity = desired_capacity

    @property
    def min_size(self):
        """Gets the min_size of this CreateAutoScalingGroupRequest.  # noqa: E501

        최소사이즈  # noqa: E501

        :return: The min_size of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        """Sets the min_size of this CreateAutoScalingGroupRequest.

        최소사이즈  # noqa: E501

        :param min_size: The min_size of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: int
        """
        if min_size is None:
            raise ValueError("Invalid value for `min_size`, must not be `None`")  # noqa: E501

        self._min_size = min_size

    @property
    def max_size(self):
        """Gets the max_size of this CreateAutoScalingGroupRequest.  # noqa: E501

        최대사이즈  # noqa: E501

        :return: The max_size of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """Sets the max_size of this CreateAutoScalingGroupRequest.

        최대사이즈  # noqa: E501

        :param max_size: The max_size of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: int
        """
        if max_size is None:
            raise ValueError("Invalid value for `max_size`, must not be `None`")  # noqa: E501

        self._max_size = max_size

    @property
    def default_cooldown(self):
        """Gets the default_cooldown of this CreateAutoScalingGroupRequest.  # noqa: E501

        디폴트쿨다운타임  # noqa: E501

        :return: The default_cooldown of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._default_cooldown

    @default_cooldown.setter
    def default_cooldown(self, default_cooldown):
        """Sets the default_cooldown of this CreateAutoScalingGroupRequest.

        디폴트쿨다운타임  # noqa: E501

        :param default_cooldown: The default_cooldown of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: int
        """

        self._default_cooldown = default_cooldown

    @property
    def load_balancer_name_list(self):
        """Gets the load_balancer_name_list of this CreateAutoScalingGroupRequest.  # noqa: E501

        로드밸런서명리스트  # noqa: E501

        :return: The load_balancer_name_list of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._load_balancer_name_list

    @load_balancer_name_list.setter
    def load_balancer_name_list(self, load_balancer_name_list):
        """Sets the load_balancer_name_list of this CreateAutoScalingGroupRequest.

        로드밸런서명리스트  # noqa: E501

        :param load_balancer_name_list: The load_balancer_name_list of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: list[str]
        """

        self._load_balancer_name_list = load_balancer_name_list

    @property
    def health_check_grace_period(self):
        """Gets the health_check_grace_period of this CreateAutoScalingGroupRequest.  # noqa: E501

        헬스체크보류기간  # noqa: E501

        :return: The health_check_grace_period of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._health_check_grace_period

    @health_check_grace_period.setter
    def health_check_grace_period(self, health_check_grace_period):
        """Sets the health_check_grace_period of this CreateAutoScalingGroupRequest.

        헬스체크보류기간  # noqa: E501

        :param health_check_grace_period: The health_check_grace_period of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: int
        """

        self._health_check_grace_period = health_check_grace_period

    @property
    def health_check_type_code(self):
        """Gets the health_check_type_code of this CreateAutoScalingGroupRequest.  # noqa: E501

        헬스체크유형코드  # noqa: E501

        :return: The health_check_type_code of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._health_check_type_code

    @health_check_type_code.setter
    def health_check_type_code(self, health_check_type_code):
        """Sets the health_check_type_code of this CreateAutoScalingGroupRequest.

        헬스체크유형코드  # noqa: E501

        :param health_check_type_code: The health_check_type_code of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: str
        """

        self._health_check_type_code = health_check_type_code

    @property
    def zone_no_list(self):
        """Gets the zone_no_list of this CreateAutoScalingGroupRequest.  # noqa: E501

        ZONE번호리스트  # noqa: E501

        :return: The zone_no_list of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._zone_no_list

    @zone_no_list.setter
    def zone_no_list(self, zone_no_list):
        """Sets the zone_no_list of this CreateAutoScalingGroupRequest.

        ZONE번호리스트  # noqa: E501

        :param zone_no_list: The zone_no_list of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: list[str]
        """
        if zone_no_list is None:
            raise ValueError("Invalid value for `zone_no_list`, must not be `None`")  # noqa: E501

        self._zone_no_list = zone_no_list

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
        if not isinstance(other, CreateAutoScalingGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
