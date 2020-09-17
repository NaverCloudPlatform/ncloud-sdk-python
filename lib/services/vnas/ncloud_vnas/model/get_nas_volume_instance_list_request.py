# coding: utf-8

"""
    vnas

    OpenAPI spec version: 2020-09-17T02:28:41Z
    
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
        'region_code': 'str',
        'volume_allotment_protocol_type_code': 'str',
        'is_event_configuration': 'bool',
        'is_snapshot_configuration': 'bool',
        'nas_volume_instance_no_list': 'list[str]',
        'zone_code': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'volume_name': 'str',
        'sorted_by': 'str',
        'sorting_order': 'str'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'volume_allotment_protocol_type_code': 'volumeAllotmentProtocolTypeCode',
        'is_event_configuration': 'isEventConfiguration',
        'is_snapshot_configuration': 'isSnapshotConfiguration',
        'nas_volume_instance_no_list': 'nasVolumeInstanceNoList',
        'zone_code': 'zoneCode',
        'page_no': 'pageNo',
        'page_size': 'pageSize',
        'volume_name': 'volumeName',
        'sorted_by': 'sortedBy',
        'sorting_order': 'sortingOrder'
    }

    def __init__(self, region_code=None, volume_allotment_protocol_type_code=None, is_event_configuration=None, is_snapshot_configuration=None, nas_volume_instance_no_list=None, zone_code=None, page_no=None, page_size=None, volume_name=None, sorted_by=None, sorting_order=None):  # noqa: E501
        """GetNasVolumeInstanceListRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._volume_allotment_protocol_type_code = None
        self._is_event_configuration = None
        self._is_snapshot_configuration = None
        self._nas_volume_instance_no_list = None
        self._zone_code = None
        self._page_no = None
        self._page_size = None
        self._volume_name = None
        self._sorted_by = None
        self._sorting_order = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        if volume_allotment_protocol_type_code is not None:
            self.volume_allotment_protocol_type_code = volume_allotment_protocol_type_code
        if is_event_configuration is not None:
            self.is_event_configuration = is_event_configuration
        if is_snapshot_configuration is not None:
            self.is_snapshot_configuration = is_snapshot_configuration
        if nas_volume_instance_no_list is not None:
            self.nas_volume_instance_no_list = nas_volume_instance_no_list
        if zone_code is not None:
            self.zone_code = zone_code
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if volume_name is not None:
            self.volume_name = volume_name
        if sorted_by is not None:
            self.sorted_by = sorted_by
        if sorting_order is not None:
            self.sorting_order = sorting_order

    @property
    def region_code(self):
        """Gets the region_code of this GetNasVolumeInstanceListRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this GetNasVolumeInstanceListRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

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

        스냅샷설정여부  # noqa: E501

        :return: The is_snapshot_configuration of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_snapshot_configuration

    @is_snapshot_configuration.setter
    def is_snapshot_configuration(self, is_snapshot_configuration):
        """Sets the is_snapshot_configuration of this GetNasVolumeInstanceListRequest.

        스냅샷설정여부  # noqa: E501

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
    def zone_code(self):
        """Gets the zone_code of this GetNasVolumeInstanceListRequest.  # noqa: E501

        ZONE코드  # noqa: E501

        :return: The zone_code of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_code

    @zone_code.setter
    def zone_code(self, zone_code):
        """Sets the zone_code of this GetNasVolumeInstanceListRequest.

        ZONE코드  # noqa: E501

        :param zone_code: The zone_code of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._zone_code = zone_code

    @property
    def page_no(self):
        """Gets the page_no of this GetNasVolumeInstanceListRequest.  # noqa: E501

        페이지번호  # noqa: E501

        :return: The page_no of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetNasVolumeInstanceListRequest.

        페이지번호  # noqa: E501

        :param page_no: The page_no of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetNasVolumeInstanceListRequest.  # noqa: E501

        페이지사이즈  # noqa: E501

        :return: The page_size of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetNasVolumeInstanceListRequest.

        페이지사이즈  # noqa: E501

        :param page_size: The page_size of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def volume_name(self):
        """Gets the volume_name of this GetNasVolumeInstanceListRequest.  # noqa: E501

        볼륨이름  # noqa: E501

        :return: The volume_name of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this GetNasVolumeInstanceListRequest.

        볼륨이름  # noqa: E501

        :param volume_name: The volume_name of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._volume_name = volume_name

    @property
    def sorted_by(self):
        """Gets the sorted_by of this GetNasVolumeInstanceListRequest.  # noqa: E501

        정렬대상  # noqa: E501

        :return: The sorted_by of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorted_by

    @sorted_by.setter
    def sorted_by(self, sorted_by):
        """Sets the sorted_by of this GetNasVolumeInstanceListRequest.

        정렬대상  # noqa: E501

        :param sorted_by: The sorted_by of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._sorted_by = sorted_by

    @property
    def sorting_order(self):
        """Gets the sorting_order of this GetNasVolumeInstanceListRequest.  # noqa: E501

        정렬순서  # noqa: E501

        :return: The sorting_order of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorting_order

    @sorting_order.setter
    def sorting_order(self, sorting_order):
        """Sets the sorting_order of this GetNasVolumeInstanceListRequest.

        정렬순서  # noqa: E501

        :param sorting_order: The sorting_order of this GetNasVolumeInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._sorting_order = sorting_order

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
