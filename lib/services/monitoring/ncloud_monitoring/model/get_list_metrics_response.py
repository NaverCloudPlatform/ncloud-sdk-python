# coding: utf-8

"""
    monitoring

    OpenAPI spec version: 2018-11-13T06:28:28Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_monitoring.model.metric import Metric  # noqa: F401,E501


class GetListMetricsResponse(object):
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
        'metrics': 'list[Metric]'
    }

    attribute_map = {
        'request_id': 'requestId',
        'return_code': 'returnCode',
        'return_message': 'returnMessage',
        'metrics': 'metrics'
    }

    def __init__(self, request_id=None, return_code=None, return_message=None, metrics=None):  # noqa: E501
        """GetListMetricsResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._return_code = None
        self._return_message = None
        self._metrics = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if return_code is not None:
            self.return_code = return_code
        if return_message is not None:
            self.return_message = return_message
        if metrics is not None:
            self.metrics = metrics

    @property
    def request_id(self):
        """Gets the request_id of this GetListMetricsResponse.  # noqa: E501


        :return: The request_id of this GetListMetricsResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this GetListMetricsResponse.


        :param request_id: The request_id of this GetListMetricsResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def return_code(self):
        """Gets the return_code of this GetListMetricsResponse.  # noqa: E501


        :return: The return_code of this GetListMetricsResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this GetListMetricsResponse.


        :param return_code: The return_code of this GetListMetricsResponse.  # noqa: E501
        :type: str
        """

        self._return_code = return_code

    @property
    def return_message(self):
        """Gets the return_message of this GetListMetricsResponse.  # noqa: E501


        :return: The return_message of this GetListMetricsResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_message

    @return_message.setter
    def return_message(self, return_message):
        """Sets the return_message of this GetListMetricsResponse.


        :param return_message: The return_message of this GetListMetricsResponse.  # noqa: E501
        :type: str
        """

        self._return_message = return_message

    @property
    def metrics(self):
        """Gets the metrics of this GetListMetricsResponse.  # noqa: E501


        :return: The metrics of this GetListMetricsResponse.  # noqa: E501
        :rtype: list[Metric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this GetListMetricsResponse.


        :param metrics: The metrics of this GetListMetricsResponse.  # noqa: E501
        :type: list[Metric]
        """

        self._metrics = metrics

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
        if not isinstance(other, GetListMetricsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
