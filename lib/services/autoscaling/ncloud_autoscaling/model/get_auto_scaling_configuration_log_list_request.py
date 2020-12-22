# coding: utf-8

"""
    autoscaling

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetAutoScalingConfigurationLogListRequest(object):
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
        'configuration_no_list': 'list[str]',
        'auto_scaling_group_name': 'str',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'configuration_no_list': 'configurationNoList',
        'auto_scaling_group_name': 'autoScalingGroupName',
        'page_no': 'pageNo',
        'page_size': 'pageSize'
    }

    def __init__(self, configuration_no_list=None, auto_scaling_group_name=None, page_no=None, page_size=None):  # noqa: E501
        """GetAutoScalingConfigurationLogListRequest - a model defined in Swagger"""  # noqa: E501

        self._configuration_no_list = None
        self._auto_scaling_group_name = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        if configuration_no_list is not None:
            self.configuration_no_list = configuration_no_list
        if auto_scaling_group_name is not None:
            self.auto_scaling_group_name = auto_scaling_group_name
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def configuration_no_list(self):
        """Gets the configuration_no_list of this GetAutoScalingConfigurationLogListRequest.  # noqa: E501

        설정번호리스트  # noqa: E501

        :return: The configuration_no_list of this GetAutoScalingConfigurationLogListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._configuration_no_list

    @configuration_no_list.setter
    def configuration_no_list(self, configuration_no_list):
        """Sets the configuration_no_list of this GetAutoScalingConfigurationLogListRequest.

        설정번호리스트  # noqa: E501

        :param configuration_no_list: The configuration_no_list of this GetAutoScalingConfigurationLogListRequest.  # noqa: E501
        :type: list[str]
        """

        self._configuration_no_list = configuration_no_list

    @property
    def auto_scaling_group_name(self):
        """Gets the auto_scaling_group_name of this GetAutoScalingConfigurationLogListRequest.  # noqa: E501

        오토스케일링그룹명  # noqa: E501

        :return: The auto_scaling_group_name of this GetAutoScalingConfigurationLogListRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_scaling_group_name

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, auto_scaling_group_name):
        """Sets the auto_scaling_group_name of this GetAutoScalingConfigurationLogListRequest.

        오토스케일링그룹명  # noqa: E501

        :param auto_scaling_group_name: The auto_scaling_group_name of this GetAutoScalingConfigurationLogListRequest.  # noqa: E501
        :type: str
        """

        self._auto_scaling_group_name = auto_scaling_group_name

    @property
    def page_no(self):
        """Gets the page_no of this GetAutoScalingConfigurationLogListRequest.  # noqa: E501

        페이지번호  # noqa: E501

        :return: The page_no of this GetAutoScalingConfigurationLogListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetAutoScalingConfigurationLogListRequest.

        페이지번호  # noqa: E501

        :param page_no: The page_no of this GetAutoScalingConfigurationLogListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetAutoScalingConfigurationLogListRequest.  # noqa: E501

        페이지사이즈  # noqa: E501

        :return: The page_size of this GetAutoScalingConfigurationLogListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetAutoScalingConfigurationLogListRequest.

        페이지사이즈  # noqa: E501

        :param page_size: The page_size of this GetAutoScalingConfigurationLogListRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if not isinstance(other, GetAutoScalingConfigurationLogListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
