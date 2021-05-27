# coding: utf-8

"""
    vloadbalancer

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vloadbalancer.model.target import Target  # noqa: F401,E501


class SetTargetResponse(object):
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
        'request_id': 'str',
        'return_code': 'str',
        'return_message': 'str',
        'total_rows': 'int',
        'target_list': 'list[Target]'
    }

    attribute_map = {
        'request_id': 'requestId',
        'return_code': 'returnCode',
        'return_message': 'returnMessage',
        'total_rows': 'totalRows',
        'target_list': 'targetList'
    }

    def __init__(self, request_id=None, return_code=None, return_message=None, total_rows=None, target_list=None):  # noqa: E501
        """SetTargetResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._return_code = None
        self._return_message = None
        self._total_rows = None
        self._target_list = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if return_code is not None:
            self.return_code = return_code
        if return_message is not None:
            self.return_message = return_message
        if total_rows is not None:
            self.total_rows = total_rows
        if target_list is not None:
            self.target_list = target_list

    @property
    def request_id(self):
        """Gets the request_id of this SetTargetResponse.  # noqa: E501


        :return: The request_id of this SetTargetResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this SetTargetResponse.


        :param request_id: The request_id of this SetTargetResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def return_code(self):
        """Gets the return_code of this SetTargetResponse.  # noqa: E501


        :return: The return_code of this SetTargetResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this SetTargetResponse.


        :param return_code: The return_code of this SetTargetResponse.  # noqa: E501
        :type: str
        """

        self._return_code = return_code

    @property
    def return_message(self):
        """Gets the return_message of this SetTargetResponse.  # noqa: E501


        :return: The return_message of this SetTargetResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_message

    @return_message.setter
    def return_message(self, return_message):
        """Sets the return_message of this SetTargetResponse.


        :param return_message: The return_message of this SetTargetResponse.  # noqa: E501
        :type: str
        """

        self._return_message = return_message

    @property
    def total_rows(self):
        """Gets the total_rows of this SetTargetResponse.  # noqa: E501


        :return: The total_rows of this SetTargetResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """Sets the total_rows of this SetTargetResponse.


        :param total_rows: The total_rows of this SetTargetResponse.  # noqa: E501
        :type: int
        """

        self._total_rows = total_rows

    @property
    def target_list(self):
        """Gets the target_list of this SetTargetResponse.  # noqa: E501


        :return: The target_list of this SetTargetResponse.  # noqa: E501
        :rtype: list[Target]
        """
        return self._target_list

    @target_list.setter
    def target_list(self, target_list):
        """Sets the target_list of this SetTargetResponse.


        :param target_list: The target_list of this SetTargetResponse.  # noqa: E501
        :type: list[Target]
        """

        self._target_list = target_list

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
        if not isinstance(other, SetTargetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
