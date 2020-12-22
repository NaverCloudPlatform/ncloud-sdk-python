# coding: utf-8

"""
    autoscaling

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SuspendProcessesRequest(object):
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
        'scaling_process_code_list': 'list[str]'
    }

    attribute_map = {
        'auto_scaling_group_name': 'autoScalingGroupName',
        'scaling_process_code_list': 'scalingProcessCodeList'
    }

    def __init__(self, auto_scaling_group_name=None, scaling_process_code_list=None):  # noqa: E501
        """SuspendProcessesRequest - a model defined in Swagger"""  # noqa: E501

        self._auto_scaling_group_name = None
        self._scaling_process_code_list = None
        self.discriminator = None

        self.auto_scaling_group_name = auto_scaling_group_name
        if scaling_process_code_list is not None:
            self.scaling_process_code_list = scaling_process_code_list

    @property
    def auto_scaling_group_name(self):
        """Gets the auto_scaling_group_name of this SuspendProcessesRequest.  # noqa: E501

        오토스케일링그룹명  # noqa: E501

        :return: The auto_scaling_group_name of this SuspendProcessesRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_scaling_group_name

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, auto_scaling_group_name):
        """Sets the auto_scaling_group_name of this SuspendProcessesRequest.

        오토스케일링그룹명  # noqa: E501

        :param auto_scaling_group_name: The auto_scaling_group_name of this SuspendProcessesRequest.  # noqa: E501
        :type: str
        """
        if auto_scaling_group_name is None:
            raise ValueError("Invalid value for `auto_scaling_group_name`, must not be `None`")  # noqa: E501

        self._auto_scaling_group_name = auto_scaling_group_name

    @property
    def scaling_process_code_list(self):
        """Gets the scaling_process_code_list of this SuspendProcessesRequest.  # noqa: E501

        분류프로세스코드리스트  # noqa: E501

        :return: The scaling_process_code_list of this SuspendProcessesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._scaling_process_code_list

    @scaling_process_code_list.setter
    def scaling_process_code_list(self, scaling_process_code_list):
        """Sets the scaling_process_code_list of this SuspendProcessesRequest.

        분류프로세스코드리스트  # noqa: E501

        :param scaling_process_code_list: The scaling_process_code_list of this SuspendProcessesRequest.  # noqa: E501
        :type: list[str]
        """

        self._scaling_process_code_list = scaling_process_code_list

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
        if not isinstance(other, SuspendProcessesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
