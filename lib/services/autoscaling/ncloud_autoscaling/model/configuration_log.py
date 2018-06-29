# coding: utf-8

"""
    autoscaling

    OpenAPI spec version: 2018-06-21T02:22:22Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ConfigurationLog(object):
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
        'configuration_no': 'str',
        'configuration_action_name': 'str',
        'parameters': 'str',
        'launch_configuration_name': 'str',
        'auto_scaling_group_name': 'str',
        'scheduled_action_name': 'str',
        'setting_time': 'str'
    }

    attribute_map = {
        'configuration_no': 'configurationNo',
        'configuration_action_name': 'configurationActionName',
        'parameters': 'parameters',
        'launch_configuration_name': 'launchConfigurationName',
        'auto_scaling_group_name': 'autoScalingGroupName',
        'scheduled_action_name': 'scheduledActionName',
        'setting_time': 'settingTime'
    }

    def __init__(self, configuration_no=None, configuration_action_name=None, parameters=None, launch_configuration_name=None, auto_scaling_group_name=None, scheduled_action_name=None, setting_time=None):  # noqa: E501
        """ConfigurationLog - a model defined in Swagger"""  # noqa: E501

        self._configuration_no = None
        self._configuration_action_name = None
        self._parameters = None
        self._launch_configuration_name = None
        self._auto_scaling_group_name = None
        self._scheduled_action_name = None
        self._setting_time = None
        self.discriminator = None

        if configuration_no is not None:
            self.configuration_no = configuration_no
        if configuration_action_name is not None:
            self.configuration_action_name = configuration_action_name
        if parameters is not None:
            self.parameters = parameters
        if launch_configuration_name is not None:
            self.launch_configuration_name = launch_configuration_name
        if auto_scaling_group_name is not None:
            self.auto_scaling_group_name = auto_scaling_group_name
        if scheduled_action_name is not None:
            self.scheduled_action_name = scheduled_action_name
        if setting_time is not None:
            self.setting_time = setting_time

    @property
    def configuration_no(self):
        """Gets the configuration_no of this ConfigurationLog.  # noqa: E501

        설정번호  # noqa: E501

        :return: The configuration_no of this ConfigurationLog.  # noqa: E501
        :rtype: str
        """
        return self._configuration_no

    @configuration_no.setter
    def configuration_no(self, configuration_no):
        """Sets the configuration_no of this ConfigurationLog.

        설정번호  # noqa: E501

        :param configuration_no: The configuration_no of this ConfigurationLog.  # noqa: E501
        :type: str
        """

        self._configuration_no = configuration_no

    @property
    def configuration_action_name(self):
        """Gets the configuration_action_name of this ConfigurationLog.  # noqa: E501

        설정액션명  # noqa: E501

        :return: The configuration_action_name of this ConfigurationLog.  # noqa: E501
        :rtype: str
        """
        return self._configuration_action_name

    @configuration_action_name.setter
    def configuration_action_name(self, configuration_action_name):
        """Sets the configuration_action_name of this ConfigurationLog.

        설정액션명  # noqa: E501

        :param configuration_action_name: The configuration_action_name of this ConfigurationLog.  # noqa: E501
        :type: str
        """

        self._configuration_action_name = configuration_action_name

    @property
    def parameters(self):
        """Gets the parameters of this ConfigurationLog.  # noqa: E501

        파라미터  # noqa: E501

        :return: The parameters of this ConfigurationLog.  # noqa: E501
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ConfigurationLog.

        파라미터  # noqa: E501

        :param parameters: The parameters of this ConfigurationLog.  # noqa: E501
        :type: str
        """

        self._parameters = parameters

    @property
    def launch_configuration_name(self):
        """Gets the launch_configuration_name of this ConfigurationLog.  # noqa: E501

        론치설절명  # noqa: E501

        :return: The launch_configuration_name of this ConfigurationLog.  # noqa: E501
        :rtype: str
        """
        return self._launch_configuration_name

    @launch_configuration_name.setter
    def launch_configuration_name(self, launch_configuration_name):
        """Sets the launch_configuration_name of this ConfigurationLog.

        론치설절명  # noqa: E501

        :param launch_configuration_name: The launch_configuration_name of this ConfigurationLog.  # noqa: E501
        :type: str
        """

        self._launch_configuration_name = launch_configuration_name

    @property
    def auto_scaling_group_name(self):
        """Gets the auto_scaling_group_name of this ConfigurationLog.  # noqa: E501

        오토스케일링그룹명  # noqa: E501

        :return: The auto_scaling_group_name of this ConfigurationLog.  # noqa: E501
        :rtype: str
        """
        return self._auto_scaling_group_name

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, auto_scaling_group_name):
        """Sets the auto_scaling_group_name of this ConfigurationLog.

        오토스케일링그룹명  # noqa: E501

        :param auto_scaling_group_name: The auto_scaling_group_name of this ConfigurationLog.  # noqa: E501
        :type: str
        """

        self._auto_scaling_group_name = auto_scaling_group_name

    @property
    def scheduled_action_name(self):
        """Gets the scheduled_action_name of this ConfigurationLog.  # noqa: E501

        스케쥴액션명  # noqa: E501

        :return: The scheduled_action_name of this ConfigurationLog.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_action_name

    @scheduled_action_name.setter
    def scheduled_action_name(self, scheduled_action_name):
        """Sets the scheduled_action_name of this ConfigurationLog.

        스케쥴액션명  # noqa: E501

        :param scheduled_action_name: The scheduled_action_name of this ConfigurationLog.  # noqa: E501
        :type: str
        """

        self._scheduled_action_name = scheduled_action_name

    @property
    def setting_time(self):
        """Gets the setting_time of this ConfigurationLog.  # noqa: E501

        설정일시  # noqa: E501

        :return: The setting_time of this ConfigurationLog.  # noqa: E501
        :rtype: str
        """
        return self._setting_time

    @setting_time.setter
    def setting_time(self, setting_time):
        """Sets the setting_time of this ConfigurationLog.

        설정일시  # noqa: E501

        :param setting_time: The setting_time of this ConfigurationLog.  # noqa: E501
        :type: str
        """

        self._setting_time = setting_time

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
        if not isinstance(other, ConfigurationLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other