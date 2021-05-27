# coding: utf-8

"""
    vautoscaling

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetAutoScalingActivityLogListRequest(object):
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
        'auto_scaling_group_no': 'str',
        'activity_no_list': 'list[str]',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'auto_scaling_group_no': 'autoScalingGroupNo',
        'activity_no_list': 'activityNoList',
        'page_no': 'pageNo',
        'page_size': 'pageSize'
    }

    def __init__(self, region_code=None, auto_scaling_group_no=None, activity_no_list=None, page_no=None, page_size=None):  # noqa: E501
        """GetAutoScalingActivityLogListRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._auto_scaling_group_no = None
        self._activity_no_list = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        self.auto_scaling_group_no = auto_scaling_group_no
        if activity_no_list is not None:
            self.activity_no_list = activity_no_list
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def region_code(self):
        """Gets the region_code of this GetAutoScalingActivityLogListRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this GetAutoScalingActivityLogListRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this GetAutoScalingActivityLogListRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this GetAutoScalingActivityLogListRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def auto_scaling_group_no(self):
        """Gets the auto_scaling_group_no of this GetAutoScalingActivityLogListRequest.  # noqa: E501

        오토스케일링그룹번호  # noqa: E501

        :return: The auto_scaling_group_no of this GetAutoScalingActivityLogListRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_scaling_group_no

    @auto_scaling_group_no.setter
    def auto_scaling_group_no(self, auto_scaling_group_no):
        """Sets the auto_scaling_group_no of this GetAutoScalingActivityLogListRequest.

        오토스케일링그룹번호  # noqa: E501

        :param auto_scaling_group_no: The auto_scaling_group_no of this GetAutoScalingActivityLogListRequest.  # noqa: E501
        :type: str
        """
        if auto_scaling_group_no is None:
            raise ValueError("Invalid value for `auto_scaling_group_no`, must not be `None`")  # noqa: E501

        self._auto_scaling_group_no = auto_scaling_group_no

    @property
    def activity_no_list(self):
        """Gets the activity_no_list of this GetAutoScalingActivityLogListRequest.  # noqa: E501

        액티비티번호리스트  # noqa: E501

        :return: The activity_no_list of this GetAutoScalingActivityLogListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._activity_no_list

    @activity_no_list.setter
    def activity_no_list(self, activity_no_list):
        """Sets the activity_no_list of this GetAutoScalingActivityLogListRequest.

        액티비티번호리스트  # noqa: E501

        :param activity_no_list: The activity_no_list of this GetAutoScalingActivityLogListRequest.  # noqa: E501
        :type: list[str]
        """

        self._activity_no_list = activity_no_list

    @property
    def page_no(self):
        """Gets the page_no of this GetAutoScalingActivityLogListRequest.  # noqa: E501

        페이지번호  # noqa: E501

        :return: The page_no of this GetAutoScalingActivityLogListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetAutoScalingActivityLogListRequest.

        페이지번호  # noqa: E501

        :param page_no: The page_no of this GetAutoScalingActivityLogListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetAutoScalingActivityLogListRequest.  # noqa: E501

        페이지사이즈  # noqa: E501

        :return: The page_size of this GetAutoScalingActivityLogListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetAutoScalingActivityLogListRequest.

        페이지사이즈  # noqa: E501

        :param page_size: The page_size of this GetAutoScalingActivityLogListRequest.  # noqa: E501
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
        if not isinstance(other, GetAutoScalingActivityLogListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other