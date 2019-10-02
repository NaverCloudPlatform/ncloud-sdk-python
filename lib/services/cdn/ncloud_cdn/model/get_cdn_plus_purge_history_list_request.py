# coding: utf-8

"""
    cdn

    OpenAPI spec version: 2018-11-13T06:29:10Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetCdnPlusPurgeHistoryListRequest(object):
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
        'cdn_instance_no': 'str',
        'purge_id_list': 'list[str]'
    }

    attribute_map = {
        'cdn_instance_no': 'cdnInstanceNo',
        'purge_id_list': 'purgeIdList'
    }

    def __init__(self, cdn_instance_no=None, purge_id_list=None):  # noqa: E501
        """GetCdnPlusPurgeHistoryListRequest - a model defined in Swagger"""  # noqa: E501

        self._cdn_instance_no = None
        self._purge_id_list = None
        self.discriminator = None

        self.cdn_instance_no = cdn_instance_no
        if purge_id_list is not None:
            self.purge_id_list = purge_id_list

    @property
    def cdn_instance_no(self):
        """Gets the cdn_instance_no of this GetCdnPlusPurgeHistoryListRequest.  # noqa: E501

        CDN인스턴스번호  # noqa: E501

        :return: The cdn_instance_no of this GetCdnPlusPurgeHistoryListRequest.  # noqa: E501
        :rtype: str
        """
        return self._cdn_instance_no

    @cdn_instance_no.setter
    def cdn_instance_no(self, cdn_instance_no):
        """Sets the cdn_instance_no of this GetCdnPlusPurgeHistoryListRequest.

        CDN인스턴스번호  # noqa: E501

        :param cdn_instance_no: The cdn_instance_no of this GetCdnPlusPurgeHistoryListRequest.  # noqa: E501
        :type: str
        """
        if cdn_instance_no is None:
            raise ValueError("Invalid value for `cdn_instance_no`, must not be `None`")  # noqa: E501

        self._cdn_instance_no = cdn_instance_no

    @property
    def purge_id_list(self):
        """Gets the purge_id_list of this GetCdnPlusPurgeHistoryListRequest.  # noqa: E501

        퍼지ID리스트  # noqa: E501

        :return: The purge_id_list of this GetCdnPlusPurgeHistoryListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._purge_id_list

    @purge_id_list.setter
    def purge_id_list(self, purge_id_list):
        """Sets the purge_id_list of this GetCdnPlusPurgeHistoryListRequest.

        퍼지ID리스트  # noqa: E501

        :param purge_id_list: The purge_id_list of this GetCdnPlusPurgeHistoryListRequest.  # noqa: E501
        :type: list[str]
        """

        self._purge_id_list = purge_id_list

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
        if not isinstance(other, GetCdnPlusPurgeHistoryListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
