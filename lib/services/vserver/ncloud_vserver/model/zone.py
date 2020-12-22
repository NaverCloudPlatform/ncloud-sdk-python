# coding: utf-8

"""
    vserver

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Zone(object):
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
        'zone_name': 'str',
        'zone_code': 'str',
        'region_code': 'str',
        'zone_description': 'str'
    }

    attribute_map = {
        'zone_name': 'zoneName',
        'zone_code': 'zoneCode',
        'region_code': 'regionCode',
        'zone_description': 'zoneDescription'
    }

    def __init__(self, zone_name=None, zone_code=None, region_code=None, zone_description=None):  # noqa: E501
        """Zone - a model defined in Swagger"""  # noqa: E501

        self._zone_name = None
        self._zone_code = None
        self._region_code = None
        self._zone_description = None
        self.discriminator = None

        if zone_name is not None:
            self.zone_name = zone_name
        if zone_code is not None:
            self.zone_code = zone_code
        if region_code is not None:
            self.region_code = region_code
        if zone_description is not None:
            self.zone_description = zone_description

    @property
    def zone_name(self):
        """Gets the zone_name of this Zone.  # noqa: E501

        ZONE이름  # noqa: E501

        :return: The zone_name of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this Zone.

        ZONE이름  # noqa: E501

        :param zone_name: The zone_name of this Zone.  # noqa: E501
        :type: str
        """

        self._zone_name = zone_name

    @property
    def zone_code(self):
        """Gets the zone_code of this Zone.  # noqa: E501

        ZONE코드  # noqa: E501

        :return: The zone_code of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._zone_code

    @zone_code.setter
    def zone_code(self, zone_code):
        """Sets the zone_code of this Zone.

        ZONE코드  # noqa: E501

        :param zone_code: The zone_code of this Zone.  # noqa: E501
        :type: str
        """

        self._zone_code = zone_code

    @property
    def region_code(self):
        """Gets the region_code of this Zone.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this Zone.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this Zone.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def zone_description(self):
        """Gets the zone_description of this Zone.  # noqa: E501

        ZONE설명  # noqa: E501

        :return: The zone_description of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._zone_description

    @zone_description.setter
    def zone_description(self, zone_description):
        """Sets the zone_description of this Zone.

        ZONE설명  # noqa: E501

        :param zone_description: The zone_description of this Zone.  # noqa: E501
        :type: str
        """

        self._zone_description = zone_description

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
        if not isinstance(other, Zone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
