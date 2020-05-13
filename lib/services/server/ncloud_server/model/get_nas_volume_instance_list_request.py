# coding: utf-8

"""
    server

    OpenAPI spec version: 2019-10-17T10:28:43Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetNasVolumeInstanceListRequest(object):
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
        'volume_allotment_protocol_type_code': 'str',
        'is_event_configuration': 'bool',
        'is_snapshot_configuration': 'bool',
        'nas_volume_instance_no_list': 'list[str]',
        'region_no': 'str',
        'zone_no': 'str'
    }

    attribute_map = {
        'volume_allotment_protocol_type_code': 'volumeAllotmentProtocolTypeCode',
        'is_event_configuration': 'isEventConfiguration',
        'is_snapshot_configuration': 'isSnapshotConfiguration',
        'nas_volume_instance_no_list': 'nasVolumeInstanceNoList',
        'region_no': 'regionNo',
        'zone_no': 'zoneNo'
    }

    def __init__(self, volume_allotment_protocol_type_code=None, is_event_configuration=None, is_snapshot_configuration=None, nas_volume_instance_no_list=None, region_no=None, zone_no=None):  # noqa: E501
        """GetNasVolumeInstanceListRequest - a model defined in Swagger"""  # noqa: E501

        self._volume_allotment_protocol_type_code = None
        self._is_event_configuration = None
        self._is_snapshot_configuration = None
        self._nas_volume_instance_no_list = None
        self._region_no = None
        self._zone_no = None
        self.discriminator = None

        if volume_allotment_protocol_type_code is not None:
            self.volume_allotment_protocol_type_code = volume_allotment_protocol_type_code
        if is_event_configuration is not None:
            self.is_event_configuration = is_event_configuration
        if is_snapshot_configuration is not None:
            self.is_snapshot_configuration = is_snapshot_configuration
        if nas_volume_instance_no_list is not None:
            self.nas_volume_instance_no_list = nas_volume_instance_no_list
        if region_no is not None:
            self.region_no = region_no
        if zone_no is not None:
            self.zone_no = zone_no

    @property
    def volume_allotment_protocol_type_code(self):
        """Gets the volume_allotment_protocol_type_code of this GetNasVolumeInstanceListRequest.  # noqa: E501

        볼륨할당프로토콜유형코드  # noqa: E501

        :return: The volume_allotment_protocol_type_code of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_allotment_protocol_type_code

    @volume_allotment_protocol_type_code.setter
    def volume_allotment_protocol_type_code(self, volume_allotment_protocol_type_code):
        """Sets the volume_allotment_protocol_type_code of this GetNasVolumeInstanceListRequest.

        볼륨할당프로토콜유형코드  # noqa: E501

        :param volume_allotment_protocol_type_code: The volume_allotment_protocol_type_code of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._volume_allotment_protocol_type_code = volume_allotment_protocol_type_code

    @property
    def is_event_configuration(self):
        """Gets the is_event_configuration of this GetNasVolumeInstanceListRequest.  # noqa: E501

        이벤트설정여부  # noqa: E501

        :return: The is_event_configuration of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_event_configuration

    @is_event_configuration.setter
    def is_event_configuration(self, is_event_configuration):
        """Sets the is_event_configuration of this GetNasVolumeInstanceListRequest.

        이벤트설정여부  # noqa: E501

        :param is_event_configuration: The is_event_configuration of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :type: bool
        """

        self._is_event_configuration = is_event_configuration

    @property
    def is_snapshot_configuration(self):
        """Gets the is_snapshot_configuration of this GetNasVolumeInstanceListRequest.  # noqa: E501

        스냅샷볼륨설정여부  # noqa: E501

        :return: The is_snapshot_configuration of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_snapshot_configuration

    @is_snapshot_configuration.setter
    def is_snapshot_configuration(self, is_snapshot_configuration):
        """Sets the is_snapshot_configuration of this GetNasVolumeInstanceListRequest.

        스냅샷볼륨설정여부  # noqa: E501

        :param is_snapshot_configuration: The is_snapshot_configuration of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :type: bool
        """

        self._is_snapshot_configuration = is_snapshot_configuration

    @property
    def nas_volume_instance_no_list(self):
        """Gets the nas_volume_instance_no_list of this GetNasVolumeInstanceListRequest.  # noqa: E501

        NAS볼륨인스턴스번호리스트  # noqa: E501

        :return: The nas_volume_instance_no_list of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._nas_volume_instance_no_list

    @nas_volume_instance_no_list.setter
    def nas_volume_instance_no_list(self, nas_volume_instance_no_list):
        """Sets the nas_volume_instance_no_list of this GetNasVolumeInstanceListRequest.

        NAS볼륨인스턴스번호리스트  # noqa: E501

        :param nas_volume_instance_no_list: The nas_volume_instance_no_list of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :type: list[str]
        """

        self._nas_volume_instance_no_list = nas_volume_instance_no_list

    @property
    def region_no(self):
        """Gets the region_no of this GetNasVolumeInstanceListRequest.  # noqa: E501

        리전번호  # noqa: E501

        :return: The region_no of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_no

    @region_no.setter
    def region_no(self, region_no):
        """Sets the region_no of this GetNasVolumeInstanceListRequest.

        리전번호  # noqa: E501

        :param region_no: The region_no of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._region_no = region_no

    @property
    def zone_no(self):
        """Gets the zone_no of this GetNasVolumeInstanceListRequest.  # noqa: E501

        ZONE번호  # noqa: E501

        :return: The zone_no of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_no

    @zone_no.setter
    def zone_no(self, zone_no):
        """Sets the zone_no of this GetNasVolumeInstanceListRequest.

        ZONE번호  # noqa: E501

        :param zone_no: The zone_no of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._zone_no = zone_no

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
        if not isinstance(other, GetNasVolumeInstanceListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
