# coding: utf-8

"""
    vnas

    OpenAPI spec version: 2020-09-17T02:28:41Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vnas.model.common_code import CommonCode  # noqa: F401,E501


class NasVolumeInstance(object):
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
        'nas_volume_instance_status': 'CommonCode',
        'nas_volume_instance_operation': 'CommonCode',
        'nas_volume_instance_status_name': 'str',
        'create_date': 'str',
        'nas_volume_description': 'str',
        'mount_information': 'str',
        'volume_allotment_protocol_type': 'CommonCode',
        'volume_name': 'str',
        'volume_total_size': 'int',
        'volume_size': 'int',
        'volume_use_size': 'int',
        'volume_use_ratio': 'float',
        'snapshot_volume_configuration_ratio': 'float',
        'snapshot_volume_config_period_type': 'CommonCode',
        'snapshot_volume_config_time': 'int',
        'snapshot_volume_size': 'int',
        'snapshot_volume_use_size': 'int',
        'snapshot_volume_use_ratio': 'float',
        'is_snapshot_configuration': 'bool',
        'is_event_configuration': 'bool',
        'region_code': 'str',
        'zone_code': 'str',
        'init_script_no': 'str',
        'nas_volume_server_instance_no_list': 'list[str]',
        'is_encrypted_volume': 'bool'
    }

    attribute_map = {
        'nas_volume_instance_no': 'nasVolumeInstanceNo',
        'nas_volume_instance_status': 'nasVolumeInstanceStatus',
        'nas_volume_instance_operation': 'nasVolumeInstanceOperation',
        'nas_volume_instance_status_name': 'nasVolumeInstanceStatusName',
        'create_date': 'createDate',
        'nas_volume_description': 'nasVolumeDescription',
        'mount_information': 'mountInformation',
        'volume_allotment_protocol_type': 'volumeAllotmentProtocolType',
        'volume_name': 'volumeName',
        'volume_total_size': 'volumeTotalSize',
        'volume_size': 'volumeSize',
        'volume_use_size': 'volumeUseSize',
        'volume_use_ratio': 'volumeUseRatio',
        'snapshot_volume_configuration_ratio': 'snapshotVolumeConfigurationRatio',
        'snapshot_volume_config_period_type': 'snapshotVolumeConfigPeriodType',
        'snapshot_volume_config_time': 'snapshotVolumeConfigTime',
        'snapshot_volume_size': 'snapshotVolumeSize',
        'snapshot_volume_use_size': 'snapshotVolumeUseSize',
        'snapshot_volume_use_ratio': 'snapshotVolumeUseRatio',
        'is_snapshot_configuration': 'isSnapshotConfiguration',
        'is_event_configuration': 'isEventConfiguration',
        'region_code': 'regionCode',
        'zone_code': 'zoneCode',
        'init_script_no': 'initScriptNo',
        'nas_volume_server_instance_no_list': 'nasVolumeServerInstanceNoList',
        'is_encrypted_volume': 'isEncryptedVolume'
    }

    def __init__(self, nas_volume_instance_no=None, nas_volume_instance_status=None, nas_volume_instance_operation=None, nas_volume_instance_status_name=None, create_date=None, nas_volume_description=None, mount_information=None, volume_allotment_protocol_type=None, volume_name=None, volume_total_size=None, volume_size=None, volume_use_size=None, volume_use_ratio=None, snapshot_volume_configuration_ratio=None, snapshot_volume_config_period_type=None, snapshot_volume_config_time=None, snapshot_volume_size=None, snapshot_volume_use_size=None, snapshot_volume_use_ratio=None, is_snapshot_configuration=None, is_event_configuration=None, region_code=None, zone_code=None, init_script_no=None, nas_volume_server_instance_no_list=None, is_encrypted_volume=None):  # noqa: E501
        """NasVolumeInstance - a model defined in Swagger"""  # noqa: E501

        self._nas_volume_instance_no = None
        self._nas_volume_instance_status = None
        self._nas_volume_instance_operation = None
        self._nas_volume_instance_status_name = None
        self._create_date = None
        self._nas_volume_description = None
        self._mount_information = None
        self._volume_allotment_protocol_type = None
        self._volume_name = None
        self._volume_total_size = None
        self._volume_size = None
        self._volume_use_size = None
        self._volume_use_ratio = None
        self._snapshot_volume_configuration_ratio = None
        self._snapshot_volume_config_period_type = None
        self._snapshot_volume_config_time = None
        self._snapshot_volume_size = None
        self._snapshot_volume_use_size = None
        self._snapshot_volume_use_ratio = None
        self._is_snapshot_configuration = None
        self._is_event_configuration = None
        self._region_code = None
        self._zone_code = None
        self._init_script_no = None
        self._nas_volume_server_instance_no_list = None
        self._is_encrypted_volume = None
        self.discriminator = None

        if nas_volume_instance_no is not None:
            self.nas_volume_instance_no = nas_volume_instance_no
        if nas_volume_instance_status is not None:
            self.nas_volume_instance_status = nas_volume_instance_status
        if nas_volume_instance_operation is not None:
            self.nas_volume_instance_operation = nas_volume_instance_operation
        if nas_volume_instance_status_name is not None:
            self.nas_volume_instance_status_name = nas_volume_instance_status_name
        if create_date is not None:
            self.create_date = create_date
        if nas_volume_description is not None:
            self.nas_volume_description = nas_volume_description
        if mount_information is not None:
            self.mount_information = mount_information
        if volume_allotment_protocol_type is not None:
            self.volume_allotment_protocol_type = volume_allotment_protocol_type
        if volume_name is not None:
            self.volume_name = volume_name
        if volume_total_size is not None:
            self.volume_total_size = volume_total_size
        if volume_size is not None:
            self.volume_size = volume_size
        if volume_use_size is not None:
            self.volume_use_size = volume_use_size
        if volume_use_ratio is not None:
            self.volume_use_ratio = volume_use_ratio
        if snapshot_volume_configuration_ratio is not None:
            self.snapshot_volume_configuration_ratio = snapshot_volume_configuration_ratio
        if snapshot_volume_config_period_type is not None:
            self.snapshot_volume_config_period_type = snapshot_volume_config_period_type
        if snapshot_volume_config_time is not None:
            self.snapshot_volume_config_time = snapshot_volume_config_time
        if snapshot_volume_size is not None:
            self.snapshot_volume_size = snapshot_volume_size
        if snapshot_volume_use_size is not None:
            self.snapshot_volume_use_size = snapshot_volume_use_size
        if snapshot_volume_use_ratio is not None:
            self.snapshot_volume_use_ratio = snapshot_volume_use_ratio
        if is_snapshot_configuration is not None:
            self.is_snapshot_configuration = is_snapshot_configuration
        if is_event_configuration is not None:
            self.is_event_configuration = is_event_configuration
        if region_code is not None:
            self.region_code = region_code
        if zone_code is not None:
            self.zone_code = zone_code
        if init_script_no is not None:
            self.init_script_no = init_script_no
        if nas_volume_server_instance_no_list is not None:
            self.nas_volume_server_instance_no_list = nas_volume_server_instance_no_list
        if is_encrypted_volume is not None:
            self.is_encrypted_volume = is_encrypted_volume

    @property
    def nas_volume_instance_no(self):
        """Gets the nas_volume_instance_no of this NasVolumeInstance.  # noqa: E501

        NAS볼륨인스턴스번호  # noqa: E501

        :return: The nas_volume_instance_no of this NasVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._nas_volume_instance_no

    @nas_volume_instance_no.setter
    def nas_volume_instance_no(self, nas_volume_instance_no):
        """Sets the nas_volume_instance_no of this NasVolumeInstance.

        NAS볼륨인스턴스번호  # noqa: E501

        :param nas_volume_instance_no: The nas_volume_instance_no of this NasVolumeInstance.  # noqa: E501
        :type: str
        """

        self._nas_volume_instance_no = nas_volume_instance_no

    @property
    def nas_volume_instance_status(self):
        """Gets the nas_volume_instance_status of this NasVolumeInstance.  # noqa: E501

        NAS볼륨인스턴스상태  # noqa: E501

        :return: The nas_volume_instance_status of this NasVolumeInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._nas_volume_instance_status

    @nas_volume_instance_status.setter
    def nas_volume_instance_status(self, nas_volume_instance_status):
        """Sets the nas_volume_instance_status of this NasVolumeInstance.

        NAS볼륨인스턴스상태  # noqa: E501

        :param nas_volume_instance_status: The nas_volume_instance_status of this NasVolumeInstance.  # noqa: E501
        :type: CommonCode
        """

        self._nas_volume_instance_status = nas_volume_instance_status

    @property
    def nas_volume_instance_operation(self):
        """Gets the nas_volume_instance_operation of this NasVolumeInstance.  # noqa: E501

        서버설명  # noqa: E501

        :return: The nas_volume_instance_operation of this NasVolumeInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._nas_volume_instance_operation

    @nas_volume_instance_operation.setter
    def nas_volume_instance_operation(self, nas_volume_instance_operation):
        """Sets the nas_volume_instance_operation of this NasVolumeInstance.

        서버설명  # noqa: E501

        :param nas_volume_instance_operation: The nas_volume_instance_operation of this NasVolumeInstance.  # noqa: E501
        :type: CommonCode
        """

        self._nas_volume_instance_operation = nas_volume_instance_operation

    @property
    def nas_volume_instance_status_name(self):
        """Gets the nas_volume_instance_status_name of this NasVolumeInstance.  # noqa: E501

        NAS볼륨인스턴스상태이름  # noqa: E501

        :return: The nas_volume_instance_status_name of this NasVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._nas_volume_instance_status_name

    @nas_volume_instance_status_name.setter
    def nas_volume_instance_status_name(self, nas_volume_instance_status_name):
        """Sets the nas_volume_instance_status_name of this NasVolumeInstance.

        NAS볼륨인스턴스상태이름  # noqa: E501

        :param nas_volume_instance_status_name: The nas_volume_instance_status_name of this NasVolumeInstance.  # noqa: E501
        :type: str
        """

        self._nas_volume_instance_status_name = nas_volume_instance_status_name

    @property
    def create_date(self):
        """Gets the create_date of this NasVolumeInstance.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this NasVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this NasVolumeInstance.

        생성일시  # noqa: E501

        :param create_date: The create_date of this NasVolumeInstance.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def nas_volume_description(self):
        """Gets the nas_volume_description of this NasVolumeInstance.  # noqa: E501

        NAS볼륨설명  # noqa: E501

        :return: The nas_volume_description of this NasVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._nas_volume_description

    @nas_volume_description.setter
    def nas_volume_description(self, nas_volume_description):
        """Sets the nas_volume_description of this NasVolumeInstance.

        NAS볼륨설명  # noqa: E501

        :param nas_volume_description: The nas_volume_description of this NasVolumeInstance.  # noqa: E501
        :type: str
        """

        self._nas_volume_description = nas_volume_description

    @property
    def mount_information(self):
        """Gets the mount_information of this NasVolumeInstance.  # noqa: E501

        마운트정보  # noqa: E501

        :return: The mount_information of this NasVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._mount_information

    @mount_information.setter
    def mount_information(self, mount_information):
        """Sets the mount_information of this NasVolumeInstance.

        마운트정보  # noqa: E501

        :param mount_information: The mount_information of this NasVolumeInstance.  # noqa: E501
        :type: str
        """

        self._mount_information = mount_information

    @property
    def volume_allotment_protocol_type(self):
        """Gets the volume_allotment_protocol_type of this NasVolumeInstance.  # noqa: E501

        볼륨할당프로토콜유형  # noqa: E501

        :return: The volume_allotment_protocol_type of this NasVolumeInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._volume_allotment_protocol_type

    @volume_allotment_protocol_type.setter
    def volume_allotment_protocol_type(self, volume_allotment_protocol_type):
        """Sets the volume_allotment_protocol_type of this NasVolumeInstance.

        볼륨할당프로토콜유형  # noqa: E501

        :param volume_allotment_protocol_type: The volume_allotment_protocol_type of this NasVolumeInstance.  # noqa: E501
        :type: CommonCode
        """

        self._volume_allotment_protocol_type = volume_allotment_protocol_type

    @property
    def volume_name(self):
        """Gets the volume_name of this NasVolumeInstance.  # noqa: E501

        볼륨이름  # noqa: E501

        :return: The volume_name of this NasVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this NasVolumeInstance.

        볼륨이름  # noqa: E501

        :param volume_name: The volume_name of this NasVolumeInstance.  # noqa: E501
        :type: str
        """

        self._volume_name = volume_name

    @property
    def volume_total_size(self):
        """Gets the volume_total_size of this NasVolumeInstance.  # noqa: E501

        볼륨총사이즈  # noqa: E501

        :return: The volume_total_size of this NasVolumeInstance.  # noqa: E501
        :rtype: int
        """
        return self._volume_total_size

    @volume_total_size.setter
    def volume_total_size(self, volume_total_size):
        """Sets the volume_total_size of this NasVolumeInstance.

        볼륨총사이즈  # noqa: E501

        :param volume_total_size: The volume_total_size of this NasVolumeInstance.  # noqa: E501
        :type: int
        """

        self._volume_total_size = volume_total_size

    @property
    def volume_size(self):
        """Gets the volume_size of this NasVolumeInstance.  # noqa: E501

        볼륨사이즈  # noqa: E501

        :return: The volume_size of this NasVolumeInstance.  # noqa: E501
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        """Sets the volume_size of this NasVolumeInstance.

        볼륨사이즈  # noqa: E501

        :param volume_size: The volume_size of this NasVolumeInstance.  # noqa: E501
        :type: int
        """

        self._volume_size = volume_size

    @property
    def volume_use_size(self):
        """Gets the volume_use_size of this NasVolumeInstance.  # noqa: E501

        볼륨사용사이즈  # noqa: E501

        :return: The volume_use_size of this NasVolumeInstance.  # noqa: E501
        :rtype: int
        """
        return self._volume_use_size

    @volume_use_size.setter
    def volume_use_size(self, volume_use_size):
        """Sets the volume_use_size of this NasVolumeInstance.

        볼륨사용사이즈  # noqa: E501

        :param volume_use_size: The volume_use_size of this NasVolumeInstance.  # noqa: E501
        :type: int
        """

        self._volume_use_size = volume_use_size

    @property
    def volume_use_ratio(self):
        """Gets the volume_use_ratio of this NasVolumeInstance.  # noqa: E501

        볼륨사용사이즈비율  # noqa: E501

        :return: The volume_use_ratio of this NasVolumeInstance.  # noqa: E501
        :rtype: float
        """
        return self._volume_use_ratio

    @volume_use_ratio.setter
    def volume_use_ratio(self, volume_use_ratio):
        """Sets the volume_use_ratio of this NasVolumeInstance.

        볼륨사용사이즈비율  # noqa: E501

        :param volume_use_ratio: The volume_use_ratio of this NasVolumeInstance.  # noqa: E501
        :type: float
        """

        self._volume_use_ratio = volume_use_ratio

    @property
    def snapshot_volume_configuration_ratio(self):
        """Gets the snapshot_volume_configuration_ratio of this NasVolumeInstance.  # noqa: E501

        스냅샷볼륨설정비율  # noqa: E501

        :return: The snapshot_volume_configuration_ratio of this NasVolumeInstance.  # noqa: E501
        :rtype: float
        """
        return self._snapshot_volume_configuration_ratio

    @snapshot_volume_configuration_ratio.setter
    def snapshot_volume_configuration_ratio(self, snapshot_volume_configuration_ratio):
        """Sets the snapshot_volume_configuration_ratio of this NasVolumeInstance.

        스냅샷볼륨설정비율  # noqa: E501

        :param snapshot_volume_configuration_ratio: The snapshot_volume_configuration_ratio of this NasVolumeInstance.  # noqa: E501
        :type: float
        """

        self._snapshot_volume_configuration_ratio = snapshot_volume_configuration_ratio

    @property
    def snapshot_volume_config_period_type(self):
        """Gets the snapshot_volume_config_period_type of this NasVolumeInstance.  # noqa: E501

        스냅샷볼륨설정기간유형  # noqa: E501

        :return: The snapshot_volume_config_period_type of this NasVolumeInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._snapshot_volume_config_period_type

    @snapshot_volume_config_period_type.setter
    def snapshot_volume_config_period_type(self, snapshot_volume_config_period_type):
        """Sets the snapshot_volume_config_period_type of this NasVolumeInstance.

        스냅샷볼륨설정기간유형  # noqa: E501

        :param snapshot_volume_config_period_type: The snapshot_volume_config_period_type of this NasVolumeInstance.  # noqa: E501
        :type: CommonCode
        """

        self._snapshot_volume_config_period_type = snapshot_volume_config_period_type

    @property
    def snapshot_volume_config_time(self):
        """Gets the snapshot_volume_config_time of this NasVolumeInstance.  # noqa: E501

        스냅샷볼륨설정시간  # noqa: E501

        :return: The snapshot_volume_config_time of this NasVolumeInstance.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_volume_config_time

    @snapshot_volume_config_time.setter
    def snapshot_volume_config_time(self, snapshot_volume_config_time):
        """Sets the snapshot_volume_config_time of this NasVolumeInstance.

        스냅샷볼륨설정시간  # noqa: E501

        :param snapshot_volume_config_time: The snapshot_volume_config_time of this NasVolumeInstance.  # noqa: E501
        :type: int
        """

        self._snapshot_volume_config_time = snapshot_volume_config_time

    @property
    def snapshot_volume_size(self):
        """Gets the snapshot_volume_size of this NasVolumeInstance.  # noqa: E501

        스냅샷볼륨사이즈  # noqa: E501

        :return: The snapshot_volume_size of this NasVolumeInstance.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_volume_size

    @snapshot_volume_size.setter
    def snapshot_volume_size(self, snapshot_volume_size):
        """Sets the snapshot_volume_size of this NasVolumeInstance.

        스냅샷볼륨사이즈  # noqa: E501

        :param snapshot_volume_size: The snapshot_volume_size of this NasVolumeInstance.  # noqa: E501
        :type: int
        """

        self._snapshot_volume_size = snapshot_volume_size

    @property
    def snapshot_volume_use_size(self):
        """Gets the snapshot_volume_use_size of this NasVolumeInstance.  # noqa: E501

        스냅샷볼륨사용사이즈  # noqa: E501

        :return: The snapshot_volume_use_size of this NasVolumeInstance.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_volume_use_size

    @snapshot_volume_use_size.setter
    def snapshot_volume_use_size(self, snapshot_volume_use_size):
        """Sets the snapshot_volume_use_size of this NasVolumeInstance.

        스냅샷볼륨사용사이즈  # noqa: E501

        :param snapshot_volume_use_size: The snapshot_volume_use_size of this NasVolumeInstance.  # noqa: E501
        :type: int
        """

        self._snapshot_volume_use_size = snapshot_volume_use_size

    @property
    def snapshot_volume_use_ratio(self):
        """Gets the snapshot_volume_use_ratio of this NasVolumeInstance.  # noqa: E501

        스냅샷볼륨사용비율  # noqa: E501

        :return: The snapshot_volume_use_ratio of this NasVolumeInstance.  # noqa: E501
        :rtype: float
        """
        return self._snapshot_volume_use_ratio

    @snapshot_volume_use_ratio.setter
    def snapshot_volume_use_ratio(self, snapshot_volume_use_ratio):
        """Sets the snapshot_volume_use_ratio of this NasVolumeInstance.

        스냅샷볼륨사용비율  # noqa: E501

        :param snapshot_volume_use_ratio: The snapshot_volume_use_ratio of this NasVolumeInstance.  # noqa: E501
        :type: float
        """

        self._snapshot_volume_use_ratio = snapshot_volume_use_ratio

    @property
    def is_snapshot_configuration(self):
        """Gets the is_snapshot_configuration of this NasVolumeInstance.  # noqa: E501

        스냅샷설정여부  # noqa: E501

        :return: The is_snapshot_configuration of this NasVolumeInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_snapshot_configuration

    @is_snapshot_configuration.setter
    def is_snapshot_configuration(self, is_snapshot_configuration):
        """Sets the is_snapshot_configuration of this NasVolumeInstance.

        스냅샷설정여부  # noqa: E501

        :param is_snapshot_configuration: The is_snapshot_configuration of this NasVolumeInstance.  # noqa: E501
        :type: bool
        """

        self._is_snapshot_configuration = is_snapshot_configuration

    @property
    def is_event_configuration(self):
        """Gets the is_event_configuration of this NasVolumeInstance.  # noqa: E501

        이벤트설정여부  # noqa: E501

        :return: The is_event_configuration of this NasVolumeInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_event_configuration

    @is_event_configuration.setter
    def is_event_configuration(self, is_event_configuration):
        """Sets the is_event_configuration of this NasVolumeInstance.

        이벤트설정여부  # noqa: E501

        :param is_event_configuration: The is_event_configuration of this NasVolumeInstance.  # noqa: E501
        :type: bool
        """

        self._is_event_configuration = is_event_configuration

    @property
    def region_code(self):
        """Gets the region_code of this NasVolumeInstance.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this NasVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this NasVolumeInstance.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this NasVolumeInstance.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def zone_code(self):
        """Gets the zone_code of this NasVolumeInstance.  # noqa: E501

        ZONE코드  # noqa: E501

        :return: The zone_code of this NasVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._zone_code

    @zone_code.setter
    def zone_code(self, zone_code):
        """Sets the zone_code of this NasVolumeInstance.

        ZONE코드  # noqa: E501

        :param zone_code: The zone_code of this NasVolumeInstance.  # noqa: E501
        :type: str
        """

        self._zone_code = zone_code

    @property
    def init_script_no(self):
        """Gets the init_script_no of this NasVolumeInstance.  # noqa: E501

        초기화스크립트번호  # noqa: E501

        :return: The init_script_no of this NasVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._init_script_no

    @init_script_no.setter
    def init_script_no(self, init_script_no):
        """Sets the init_script_no of this NasVolumeInstance.

        초기화스크립트번호  # noqa: E501

        :param init_script_no: The init_script_no of this NasVolumeInstance.  # noqa: E501
        :type: str
        """

        self._init_script_no = init_script_no

    @property
    def nas_volume_server_instance_no_list(self):
        """Gets the nas_volume_server_instance_no_list of this NasVolumeInstance.  # noqa: E501

        NAS볼륨서버인스턴스번호리스트  # noqa: E501

        :return: The nas_volume_server_instance_no_list of this NasVolumeInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._nas_volume_server_instance_no_list

    @nas_volume_server_instance_no_list.setter
    def nas_volume_server_instance_no_list(self, nas_volume_server_instance_no_list):
        """Sets the nas_volume_server_instance_no_list of this NasVolumeInstance.

        NAS볼륨서버인스턴스번호리스트  # noqa: E501

        :param nas_volume_server_instance_no_list: The nas_volume_server_instance_no_list of this NasVolumeInstance.  # noqa: E501
        :type: list[str]
        """

        self._nas_volume_server_instance_no_list = nas_volume_server_instance_no_list

    @property
    def is_encrypted_volume(self):
        """Gets the is_encrypted_volume of this NasVolumeInstance.  # noqa: E501

        볼륨암호화여부  # noqa: E501

        :return: The is_encrypted_volume of this NasVolumeInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_encrypted_volume

    @is_encrypted_volume.setter
    def is_encrypted_volume(self, is_encrypted_volume):
        """Sets the is_encrypted_volume of this NasVolumeInstance.

        볼륨암호화여부  # noqa: E501

        :param is_encrypted_volume: The is_encrypted_volume of this NasVolumeInstance.  # noqa: E501
        :type: bool
        """

        self._is_encrypted_volume = is_encrypted_volume

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
        if not isinstance(other, NasVolumeInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
