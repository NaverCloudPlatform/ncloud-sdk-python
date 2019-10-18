# coding: utf-8

"""
    autoscaling

    OpenAPI spec version: 2018-11-13T06:27:22Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_autoscaling.model.process import Process  # noqa: F401,E501


class GetScalingProcessTypeListResponse(object):
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
        'process_list': 'list[Process]'
    }

    attribute_map = {
        'request_id': 'requestId',
        'return_code': 'returnCode',
        'return_message': 'returnMessage',
        'total_rows': 'totalRows',
        'process_list': 'processList'
    }

    def __init__(self, request_id=None, return_code=None, return_message=None, total_rows=None, process_list=None):  # noqa: E501
        """GetScalingProcessTypeListResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._return_code = None
        self._return_message = None
        self._total_rows = None
        self._process_list = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if return_code is not None:
            self.return_code = return_code
        if return_message is not None:
            self.return_message = return_message
        if total_rows is not None:
            self.total_rows = total_rows
        if process_list is not None:
            self.process_list = process_list

    @property
    def request_id(self):
        """Gets the request_id of this GetScalingProcessTypeListResponse.  # noqa: E501


        :return: The request_id of this GetScalingProcessTypeListResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this GetScalingProcessTypeListResponse.


        :param request_id: The request_id of this GetScalingProcessTypeListResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def return_code(self):
        """Gets the return_code of this GetScalingProcessTypeListResponse.  # noqa: E501


        :return: The return_code of this GetScalingProcessTypeListResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this GetScalingProcessTypeListResponse.


        :param return_code: The return_code of this GetScalingProcessTypeListResponse.  # noqa: E501
        :type: str
        """

        self._return_code = return_code

    @property
    def return_message(self):
        """Gets the return_message of this GetScalingProcessTypeListResponse.  # noqa: E501


        :return: The return_message of this GetScalingProcessTypeListResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_message

    @return_message.setter
    def return_message(self, return_message):
        """Sets the return_message of this GetScalingProcessTypeListResponse.


        :param return_message: The return_message of this GetScalingProcessTypeListResponse.  # noqa: E501
        :type: str
        """

        self._return_message = return_message

    @property
    def total_rows(self):
        """Gets the total_rows of this GetScalingProcessTypeListResponse.  # noqa: E501


        :return: The total_rows of this GetScalingProcessTypeListResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """Sets the total_rows of this GetScalingProcessTypeListResponse.


        :param total_rows: The total_rows of this GetScalingProcessTypeListResponse.  # noqa: E501
        :type: int
        """

        self._total_rows = total_rows

    @property
    def process_list(self):
        """Gets the process_list of this GetScalingProcessTypeListResponse.  # noqa: E501


        :return: The process_list of this GetScalingProcessTypeListResponse.  # noqa: E501
        :rtype: list[Process]
        """
        return self._process_list

    @process_list.setter
    def process_list(self, process_list):
        """Sets the process_list of this GetScalingProcessTypeListResponse.


        :param process_list: The process_list of this GetScalingProcessTypeListResponse.  # noqa: E501
        :type: list[Process]
        """

        self._process_list = process_list

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
        if not isinstance(other, GetScalingProcessTypeListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
