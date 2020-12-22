# coding: utf-8

"""
    server

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ChangeNasVolumeSizeRequest(object):
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
        'nas_volume_instance_no': 'str',
        'volume_size': 'int'
    }

    attribute_map = {
        'nas_volume_instance_no': 'nasVolumeInstanceNo',
        'volume_size': 'volumeSize'
    }

    def __init__(self, nas_volume_instance_no=None, volume_size=None):  # noqa: E501
        """ChangeNasVolumeSizeRequest - a model defined in Swagger"""  # noqa: E501

        self._nas_volume_instance_no = None
        self._volume_size = None
        self.discriminator = None

        self.nas_volume_instance_no = nas_volume_instance_no
        self.volume_size = volume_size

    @property
    def nas_volume_instance_no(self):
        """Gets the nas_volume_instance_no of this ChangeNasVolumeSizeRequest.  # noqa: E501

        NAS볼륨인스턴스번호  # noqa: E501

        :return: The nas_volume_instance_no of this ChangeNasVolumeSizeRequest.  # noqa: E501
        :rtype: str
        """
        return self._nas_volume_instance_no

    @nas_volume_instance_no.setter
    def nas_volume_instance_no(self, nas_volume_instance_no):
        """Sets the nas_volume_instance_no of this ChangeNasVolumeSizeRequest.

        NAS볼륨인스턴스번호  # noqa: E501

        :param nas_volume_instance_no: The nas_volume_instance_no of this ChangeNasVolumeSizeRequest.  # noqa: E501
        :type: str
        """
        if nas_volume_instance_no is None:
            raise ValueError("Invalid value for `nas_volume_instance_no`, must not be `None`")  # noqa: E501

        self._nas_volume_instance_no = nas_volume_instance_no

    @property
    def volume_size(self):
        """Gets the volume_size of this ChangeNasVolumeSizeRequest.  # noqa: E501

        NAS볼륨사이즈  # noqa: E501

        :return: The volume_size of this ChangeNasVolumeSizeRequest.  # noqa: E501
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        """Sets the volume_size of this ChangeNasVolumeSizeRequest.

        NAS볼륨사이즈  # noqa: E501

        :param volume_size: The volume_size of this ChangeNasVolumeSizeRequest.  # noqa: E501
        :type: int
        """
        if volume_size is None:
            raise ValueError("Invalid value for `volume_size`, must not be `None`")  # noqa: E501

        self._volume_size = volume_size

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
        if not isinstance(other, ChangeNasVolumeSizeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
