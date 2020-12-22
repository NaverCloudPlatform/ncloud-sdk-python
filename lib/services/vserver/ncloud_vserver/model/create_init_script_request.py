# coding: utf-8

"""
    vserver

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateInitScriptRequest(object):
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
        'init_script_content': 'str',
        'init_script_name': 'str',
        'init_script_description': 'str',
        'os_type_code': 'str'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'init_script_content': 'initScriptContent',
        'init_script_name': 'initScriptName',
        'init_script_description': 'initScriptDescription',
        'os_type_code': 'osTypeCode'
    }

    def __init__(self, region_code=None, init_script_content=None, init_script_name=None, init_script_description=None, os_type_code=None):  # noqa: E501
        """CreateInitScriptRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._init_script_content = None
        self._init_script_name = None
        self._init_script_description = None
        self._os_type_code = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        self.init_script_content = init_script_content
        if init_script_name is not None:
            self.init_script_name = init_script_name
        if init_script_description is not None:
            self.init_script_description = init_script_description
        self.os_type_code = os_type_code

    @property
    def region_code(self):
        """Gets the region_code of this CreateInitScriptRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this CreateInitScriptRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this CreateInitScriptRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this CreateInitScriptRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def init_script_content(self):
        """Gets the init_script_content of this CreateInitScriptRequest.  # noqa: E501

        초기화스크립트내용  # noqa: E501

        :return: The init_script_content of this CreateInitScriptRequest.  # noqa: E501
        :rtype: str
        """
        return self._init_script_content

    @init_script_content.setter
    def init_script_content(self, init_script_content):
        """Sets the init_script_content of this CreateInitScriptRequest.

        초기화스크립트내용  # noqa: E501

        :param init_script_content: The init_script_content of this CreateInitScriptRequest.  # noqa: E501
        :type: str
        """
        if init_script_content is None:
            raise ValueError("Invalid value for `init_script_content`, must not be `None`")  # noqa: E501

        self._init_script_content = init_script_content

    @property
    def init_script_name(self):
        """Gets the init_script_name of this CreateInitScriptRequest.  # noqa: E501

        초기화스크립트이름  # noqa: E501

        :return: The init_script_name of this CreateInitScriptRequest.  # noqa: E501
        :rtype: str
        """
        return self._init_script_name

    @init_script_name.setter
    def init_script_name(self, init_script_name):
        """Sets the init_script_name of this CreateInitScriptRequest.

        초기화스크립트이름  # noqa: E501

        :param init_script_name: The init_script_name of this CreateInitScriptRequest.  # noqa: E501
        :type: str
        """

        self._init_script_name = init_script_name

    @property
    def init_script_description(self):
        """Gets the init_script_description of this CreateInitScriptRequest.  # noqa: E501

        초기화스크립트설명  # noqa: E501

        :return: The init_script_description of this CreateInitScriptRequest.  # noqa: E501
        :rtype: str
        """
        return self._init_script_description

    @init_script_description.setter
    def init_script_description(self, init_script_description):
        """Sets the init_script_description of this CreateInitScriptRequest.

        초기화스크립트설명  # noqa: E501

        :param init_script_description: The init_script_description of this CreateInitScriptRequest.  # noqa: E501
        :type: str
        """

        self._init_script_description = init_script_description

    @property
    def os_type_code(self):
        """Gets the os_type_code of this CreateInitScriptRequest.  # noqa: E501

        OS유형코드  # noqa: E501

        :return: The os_type_code of this CreateInitScriptRequest.  # noqa: E501
        :rtype: str
        """
        return self._os_type_code

    @os_type_code.setter
    def os_type_code(self, os_type_code):
        """Sets the os_type_code of this CreateInitScriptRequest.

        OS유형코드  # noqa: E501

        :param os_type_code: The os_type_code of this CreateInitScriptRequest.  # noqa: E501
        :type: str
        """
        if os_type_code is None:
            raise ValueError("Invalid value for `os_type_code`, must not be `None`")  # noqa: E501

        self._os_type_code = os_type_code

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
        if not isinstance(other, CreateInitScriptRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
