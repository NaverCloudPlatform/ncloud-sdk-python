# coding: utf-8

"""
    autoscaling

    OpenAPI spec version: 2018-11-13T06:27:22Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccessControlGroup(object):
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
        'access_control_group_configuration_no': 'str',
        'access_control_group_name': 'str',
        'access_control_group_description': 'str',
        'is_default_group': 'bool',
        'create_date': 'str'
    }

    attribute_map = {
        'access_control_group_configuration_no': 'accessControlGroupConfigurationNo',
        'access_control_group_name': 'accessControlGroupName',
        'access_control_group_description': 'accessControlGroupDescription',
        'is_default_group': 'isDefaultGroup',
        'create_date': 'createDate'
    }

    def __init__(self, access_control_group_configuration_no=None, access_control_group_name=None, access_control_group_description=None, is_default_group=None, create_date=None):  # noqa: E501
        """AccessControlGroup - a model defined in Swagger"""  # noqa: E501

        self._access_control_group_configuration_no = None
        self._access_control_group_name = None
        self._access_control_group_description = None
        self._is_default_group = None
        self._create_date = None
        self.discriminator = None

        if access_control_group_configuration_no is not None:
            self.access_control_group_configuration_no = access_control_group_configuration_no
        if access_control_group_name is not None:
            self.access_control_group_name = access_control_group_name
        if access_control_group_description is not None:
            self.access_control_group_description = access_control_group_description
        if is_default_group is not None:
            self.is_default_group = is_default_group
        if create_date is not None:
            self.create_date = create_date

    @property
    def access_control_group_configuration_no(self):
        """Gets the access_control_group_configuration_no of this AccessControlGroup.  # noqa: E501

        접근제어그룹설정번호  # noqa: E501

        :return: The access_control_group_configuration_no of this AccessControlGroup.  # noqa: E501
        :rtype: str
        """
        return self._access_control_group_configuration_no

    @access_control_group_configuration_no.setter
    def access_control_group_configuration_no(self, access_control_group_configuration_no):
        """Sets the access_control_group_configuration_no of this AccessControlGroup.

        접근제어그룹설정번호  # noqa: E501

        :param access_control_group_configuration_no: The access_control_group_configuration_no of this AccessControlGroup.  # noqa: E501
        :type: str
        """

        self._access_control_group_configuration_no = access_control_group_configuration_no

    @property
    def access_control_group_name(self):
        """Gets the access_control_group_name of this AccessControlGroup.  # noqa: E501

        접근제어그룹명  # noqa: E501

        :return: The access_control_group_name of this AccessControlGroup.  # noqa: E501
        :rtype: str
        """
        return self._access_control_group_name

    @access_control_group_name.setter
    def access_control_group_name(self, access_control_group_name):
        """Sets the access_control_group_name of this AccessControlGroup.

        접근제어그룹명  # noqa: E501

        :param access_control_group_name: The access_control_group_name of this AccessControlGroup.  # noqa: E501
        :type: str
        """

        self._access_control_group_name = access_control_group_name

    @property
    def access_control_group_description(self):
        """Gets the access_control_group_description of this AccessControlGroup.  # noqa: E501

        접근제어그룹설명  # noqa: E501

        :return: The access_control_group_description of this AccessControlGroup.  # noqa: E501
        :rtype: str
        """
        return self._access_control_group_description

    @access_control_group_description.setter
    def access_control_group_description(self, access_control_group_description):
        """Sets the access_control_group_description of this AccessControlGroup.

        접근제어그룹설명  # noqa: E501

        :param access_control_group_description: The access_control_group_description of this AccessControlGroup.  # noqa: E501
        :type: str
        """

        self._access_control_group_description = access_control_group_description

    @property
    def is_default_group(self):
        """Gets the is_default_group of this AccessControlGroup.  # noqa: E501

        디폴트그룹여부  # noqa: E501

        :return: The is_default_group of this AccessControlGroup.  # noqa: E501
        :rtype: bool
        """
        return self._is_default_group

    @is_default_group.setter
    def is_default_group(self, is_default_group):
        """Sets the is_default_group of this AccessControlGroup.

        디폴트그룹여부  # noqa: E501

        :param is_default_group: The is_default_group of this AccessControlGroup.  # noqa: E501
        :type: bool
        """

        self._is_default_group = is_default_group

    @property
    def create_date(self):
        """Gets the create_date of this AccessControlGroup.  # noqa: E501

        생성일자  # noqa: E501

        :return: The create_date of this AccessControlGroup.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this AccessControlGroup.

        생성일자  # noqa: E501

        :param create_date: The create_date of this AccessControlGroup.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

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
        if not isinstance(other, AccessControlGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
