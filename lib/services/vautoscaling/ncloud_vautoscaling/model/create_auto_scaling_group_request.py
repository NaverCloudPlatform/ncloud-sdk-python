# coding: utf-8

"""
    vautoscaling

    
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
        'region_code': 'str',
        'launch_configuration_no': 'str',
        'auto_scaling_group_name': 'str',
        'vpc_no': 'str',
        'subnet_no': 'str',
        'access_control_group_no_list': 'list[str]',
        'server_name_prefix': 'str',
        'min_size': 'int',
        'max_size': 'int',
        'desired_capacity': 'int',
        'default_cool_down': 'int',
        'health_check_grace_period': 'int',
        'health_check_type_code': 'str',
        'target_group_no_list': 'list[str]'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'launch_configuration_no': 'launchConfigurationNo',
        'auto_scaling_group_name': 'autoScalingGroupName',
        'vpc_no': 'vpcNo',
        'subnet_no': 'subnetNo',
        'access_control_group_no_list': 'accessControlGroupNoList',
        'server_name_prefix': 'serverNamePrefix',
        'min_size': 'minSize',
        'max_size': 'maxSize',
        'desired_capacity': 'desiredCapacity',
        'default_cool_down': 'defaultCoolDown',
        'health_check_grace_period': 'healthCheckGracePeriod',
        'health_check_type_code': 'healthCheckTypeCode',
        'target_group_no_list': 'targetGroupNoList'
    }

    def __init__(self, region_code=None, launch_configuration_no=None, auto_scaling_group_name=None, vpc_no=None, subnet_no=None, access_control_group_no_list=None, server_name_prefix=None, min_size=None, max_size=None, desired_capacity=None, default_cool_down=None, health_check_grace_period=None, health_check_type_code=None, target_group_no_list=None):  # noqa: E501
        """CreateAutoScalingGroupRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._launch_configuration_no = None
        self._auto_scaling_group_name = None
        self._vpc_no = None
        self._subnet_no = None
        self._access_control_group_no_list = None
        self._server_name_prefix = None
        self._min_size = None
        self._max_size = None
        self._desired_capacity = None
        self._default_cool_down = None
        self._health_check_grace_period = None
        self._health_check_type_code = None
        self._target_group_no_list = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        self.launch_configuration_no = launch_configuration_no
        if auto_scaling_group_name is not None:
            self.auto_scaling_group_name = auto_scaling_group_name
        self.vpc_no = vpc_no
        self.subnet_no = subnet_no
        self.access_control_group_no_list = access_control_group_no_list
        if server_name_prefix is not None:
            self.server_name_prefix = server_name_prefix
        self.min_size = min_size
        self.max_size = max_size
        if desired_capacity is not None:
            self.desired_capacity = desired_capacity
        if default_cool_down is not None:
            self.default_cool_down = default_cool_down
        if health_check_grace_period is not None:
            self.health_check_grace_period = health_check_grace_period
        if health_check_type_code is not None:
            self.health_check_type_code = health_check_type_code
        if target_group_no_list is not None:
            self.target_group_no_list = target_group_no_list

    @property
    def region_code(self):
        """Gets the region_code of this CreateAutoScalingGroupRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this CreateAutoScalingGroupRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def launch_configuration_no(self):
        """Gets the launch_configuration_no of this CreateAutoScalingGroupRequest.  # noqa: E501

        론치설정번호  # noqa: E501

        :return: The launch_configuration_no of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._launch_configuration_no

    @launch_configuration_no.setter
    def launch_configuration_no(self, launch_configuration_no):
        """Sets the launch_configuration_no of this CreateAutoScalingGroupRequest.

        론치설정번호  # noqa: E501

        :param launch_configuration_no: The launch_configuration_no of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: str
        """
        if launch_configuration_no is None:
            raise ValueError("Invalid value for `launch_configuration_no`, must not be `None`")  # noqa: E501

        self._launch_configuration_no = launch_configuration_no

    @property
    def auto_scaling_group_name(self):
        """Gets the auto_scaling_group_name of this CreateAutoScalingGroupRequest.  # noqa: E501

        오토스케일링그룹이름  # noqa: E501

        :return: The auto_scaling_group_name of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_scaling_group_name

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, auto_scaling_group_name):
        """Sets the auto_scaling_group_name of this CreateAutoScalingGroupRequest.

        오토스케일링그룹이름  # noqa: E501

        :param auto_scaling_group_name: The auto_scaling_group_name of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: str
        """

        self._auto_scaling_group_name = auto_scaling_group_name

    @property
    def vpc_no(self):
        """Gets the vpc_no of this CreateAutoScalingGroupRequest.  # noqa: E501

        VPC번호  # noqa: E501

        :return: The vpc_no of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_no

    @vpc_no.setter
    def vpc_no(self, vpc_no):
        """Sets the vpc_no of this CreateAutoScalingGroupRequest.

        VPC번호  # noqa: E501

        :param vpc_no: The vpc_no of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: str
        """
        if vpc_no is None:
            raise ValueError("Invalid value for `vpc_no`, must not be `None`")  # noqa: E501

        self._vpc_no = vpc_no

    @property
    def subnet_no(self):
        """Gets the subnet_no of this CreateAutoScalingGroupRequest.  # noqa: E501

        서브넷번호  # noqa: E501

        :return: The subnet_no of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_no

    @subnet_no.setter
    def subnet_no(self, subnet_no):
        """Sets the subnet_no of this CreateAutoScalingGroupRequest.

        서브넷번호  # noqa: E501

        :param subnet_no: The subnet_no of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: str
        """
        if subnet_no is None:
            raise ValueError("Invalid value for `subnet_no`, must not be `None`")  # noqa: E501

        self._subnet_no = subnet_no

    @property
    def access_control_group_no_list(self):
        """Gets the access_control_group_no_list of this CreateAutoScalingGroupRequest.  # noqa: E501

        ACG번호리스트  # noqa: E501

        :return: The access_control_group_no_list of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_control_group_no_list

    @access_control_group_no_list.setter
    def access_control_group_no_list(self, access_control_group_no_list):
        """Sets the access_control_group_no_list of this CreateAutoScalingGroupRequest.

        ACG번호리스트  # noqa: E501

        :param access_control_group_no_list: The access_control_group_no_list of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: list[str]
        """
        if access_control_group_no_list is None:
            raise ValueError("Invalid value for `access_control_group_no_list`, must not be `None`")  # noqa: E501

        self._access_control_group_no_list = access_control_group_no_list

    @property
    def server_name_prefix(self):
        """Gets the server_name_prefix of this CreateAutoScalingGroupRequest.  # noqa: E501

        서버이름Prefix  # noqa: E501

        :return: The server_name_prefix of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_name_prefix

    @server_name_prefix.setter
    def server_name_prefix(self, server_name_prefix):
        """Sets the server_name_prefix of this CreateAutoScalingGroupRequest.

        서버이름Prefix  # noqa: E501

        :param server_name_prefix: The server_name_prefix of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: str
        """

        self._server_name_prefix = server_name_prefix

    @property
    def min_size(self):
        """Gets the min_size of this CreateAutoScalingGroupRequest.  # noqa: E501

        최소용량  # noqa: E501

        :return: The min_size of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        """Sets the min_size of this CreateAutoScalingGroupRequest.

        최소용량  # noqa: E501

        :param min_size: The min_size of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: int
        """
        if min_size is None:
            raise ValueError("Invalid value for `min_size`, must not be `None`")  # noqa: E501

        self._min_size = min_size

    @property
    def max_size(self):
        """Gets the max_size of this CreateAutoScalingGroupRequest.  # noqa: E501

        최대용량  # noqa: E501

        :return: The max_size of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """Sets the max_size of this CreateAutoScalingGroupRequest.

        최대용량  # noqa: E501

        :param max_size: The max_size of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: int
        """
        if max_size is None:
            raise ValueError("Invalid value for `max_size`, must not be `None`")  # noqa: E501

        self._max_size = max_size

    @property
    def desired_capacity(self):
        """Gets the desired_capacity of this CreateAutoScalingGroupRequest.  # noqa: E501

        기대용량  # noqa: E501

        :return: The desired_capacity of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._desired_capacity

    @desired_capacity.setter
    def desired_capacity(self, desired_capacity):
        """Sets the desired_capacity of this CreateAutoScalingGroupRequest.

        기대용량  # noqa: E501

        :param desired_capacity: The desired_capacity of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: int
        """

        self._desired_capacity = desired_capacity

    @property
    def default_cool_down(self):
        """Gets the default_cool_down of this CreateAutoScalingGroupRequest.  # noqa: E501

        쿨다운기본값  # noqa: E501

        :return: The default_cool_down of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._default_cool_down

    @default_cool_down.setter
    def default_cool_down(self, default_cool_down):
        """Sets the default_cool_down of this CreateAutoScalingGroupRequest.

        쿨다운기본값  # noqa: E501

        :param default_cool_down: The default_cool_down of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: int
        """

        self._default_cool_down = default_cool_down

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
    def target_group_no_list(self):
        """Gets the target_group_no_list of this CreateAutoScalingGroupRequest.  # noqa: E501

        타겟그룹번호리스트  # noqa: E501

        :return: The target_group_no_list of this CreateAutoScalingGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_group_no_list

    @target_group_no_list.setter
    def target_group_no_list(self, target_group_no_list):
        """Sets the target_group_no_list of this CreateAutoScalingGroupRequest.

        타겟그룹번호리스트  # noqa: E501

        :param target_group_no_list: The target_group_no_list of this CreateAutoScalingGroupRequest.  # noqa: E501
        :type: list[str]
        """

        self._target_group_no_list = target_group_no_list

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