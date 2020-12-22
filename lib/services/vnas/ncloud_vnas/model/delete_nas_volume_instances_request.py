# coding: utf-8

"""
    vnas

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeleteNasVolumeInstancesRequest(object):
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
        'nas_volume_instance_no_list': 'list[str]'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'nas_volume_instance_no_list': 'nasVolumeInstanceNoList'
    }

    def __init__(self, region_code=None, nas_volume_instance_no_list=None):  # noqa: E501
        """DeleteNasVolumeInstancesRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._nas_volume_instance_no_list = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        self.nas_volume_instance_no_list = nas_volume_instance_no_list

    @property
    def region_code(self):
        """Gets the region_code of this DeleteNasVolumeInstancesRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this DeleteNasVolumeInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this DeleteNasVolumeInstancesRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this DeleteNasVolumeInstancesRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def nas_volume_instance_no_list(self):
        """Gets the nas_volume_instance_no_list of this DeleteNasVolumeInstancesRequest.  # noqa: E501

        NAS볼륨인스턴스번호리스트  # noqa: E501

        :return: The nas_volume_instance_no_list of this DeleteNasVolumeInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._nas_volume_instance_no_list

    @nas_volume_instance_no_list.setter
    def nas_volume_instance_no_list(self, nas_volume_instance_no_list):
        """Sets the nas_volume_instance_no_list of this DeleteNasVolumeInstancesRequest.

        NAS볼륨인스턴스번호리스트  # noqa: E501

        :param nas_volume_instance_no_list: The nas_volume_instance_no_list of this DeleteNasVolumeInstancesRequest.  # noqa: E501
        :type: list[str]
        """
        if nas_volume_instance_no_list is None:
            raise ValueError("Invalid value for `nas_volume_instance_no_list`, must not be `None`")  # noqa: E501

        self._nas_volume_instance_no_list = nas_volume_instance_no_list

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
        if not isinstance(other, DeleteNasVolumeInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
