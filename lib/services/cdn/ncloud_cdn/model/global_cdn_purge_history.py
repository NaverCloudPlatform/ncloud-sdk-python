# coding: utf-8

"""
    cdn

    OpenAPI spec version: 2018-07-04T02:02:10Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_cdn.model.global_cdn_service_domain import GlobalCdnServiceDomain  # noqa: F401,E501


class GlobalCdnPurgeHistory(object):
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
        'purge_id': 'str',
        'is_whole_purge': 'bool',
        'is_whole_domain': 'bool',
        'global_cdn_service_domain_list': 'list[GlobalCdnServiceDomain]',
        'target_file_list': 'list[str]',
        'estimated_completion_date': 'str',
        'is_success': 'bool',
        'request_date': 'str'
    }

    attribute_map = {
        'cdn_instance_no': 'cdnInstanceNo',
        'purge_id': 'purgeId',
        'is_whole_purge': 'isWholePurge',
        'is_whole_domain': 'isWholeDomain',
        'global_cdn_service_domain_list': 'globalCdnServiceDomainList',
        'target_file_list': 'targetFileList',
        'estimated_completion_date': 'estimatedCompletionDate',
        'is_success': 'isSuccess',
        'request_date': 'requestDate'
    }

    def __init__(self, cdn_instance_no=None, purge_id=None, is_whole_purge=None, is_whole_domain=None, global_cdn_service_domain_list=None, target_file_list=None, estimated_completion_date=None, is_success=None, request_date=None):  # noqa: E501
        """GlobalCdnPurgeHistory - a model defined in Swagger"""  # noqa: E501

        self._cdn_instance_no = None
        self._purge_id = None
        self._is_whole_purge = None
        self._is_whole_domain = None
        self._global_cdn_service_domain_list = None
        self._target_file_list = None
        self._estimated_completion_date = None
        self._is_success = None
        self._request_date = None
        self.discriminator = None

        if cdn_instance_no is not None:
            self.cdn_instance_no = cdn_instance_no
        if purge_id is not None:
            self.purge_id = purge_id
        if is_whole_purge is not None:
            self.is_whole_purge = is_whole_purge
        if is_whole_domain is not None:
            self.is_whole_domain = is_whole_domain
        if global_cdn_service_domain_list is not None:
            self.global_cdn_service_domain_list = global_cdn_service_domain_list
        if target_file_list is not None:
            self.target_file_list = target_file_list
        if estimated_completion_date is not None:
            self.estimated_completion_date = estimated_completion_date
        if is_success is not None:
            self.is_success = is_success
        if request_date is not None:
            self.request_date = request_date

    @property
    def cdn_instance_no(self):
        """Gets the cdn_instance_no of this GlobalCdnPurgeHistory.  # noqa: E501

        CDN인스턴스번호  # noqa: E501

        :return: The cdn_instance_no of this GlobalCdnPurgeHistory.  # noqa: E501
        :rtype: str
        """
        return self._cdn_instance_no

    @cdn_instance_no.setter
    def cdn_instance_no(self, cdn_instance_no):
        """Sets the cdn_instance_no of this GlobalCdnPurgeHistory.

        CDN인스턴스번호  # noqa: E501

        :param cdn_instance_no: The cdn_instance_no of this GlobalCdnPurgeHistory.  # noqa: E501
        :type: str
        """

        self._cdn_instance_no = cdn_instance_no

    @property
    def purge_id(self):
        """Gets the purge_id of this GlobalCdnPurgeHistory.  # noqa: E501

        퍼지ID  # noqa: E501

        :return: The purge_id of this GlobalCdnPurgeHistory.  # noqa: E501
        :rtype: str
        """
        return self._purge_id

    @purge_id.setter
    def purge_id(self, purge_id):
        """Sets the purge_id of this GlobalCdnPurgeHistory.

        퍼지ID  # noqa: E501

        :param purge_id: The purge_id of this GlobalCdnPurgeHistory.  # noqa: E501
        :type: str
        """

        self._purge_id = purge_id

    @property
    def is_whole_purge(self):
        """Gets the is_whole_purge of this GlobalCdnPurgeHistory.  # noqa: E501

        전체퍼지여부  # noqa: E501

        :return: The is_whole_purge of this GlobalCdnPurgeHistory.  # noqa: E501
        :rtype: bool
        """
        return self._is_whole_purge

    @is_whole_purge.setter
    def is_whole_purge(self, is_whole_purge):
        """Sets the is_whole_purge of this GlobalCdnPurgeHistory.

        전체퍼지여부  # noqa: E501

        :param is_whole_purge: The is_whole_purge of this GlobalCdnPurgeHistory.  # noqa: E501
        :type: bool
        """

        self._is_whole_purge = is_whole_purge

    @property
    def is_whole_domain(self):
        """Gets the is_whole_domain of this GlobalCdnPurgeHistory.  # noqa: E501

        전체도메인퍼지여부  # noqa: E501

        :return: The is_whole_domain of this GlobalCdnPurgeHistory.  # noqa: E501
        :rtype: bool
        """
        return self._is_whole_domain

    @is_whole_domain.setter
    def is_whole_domain(self, is_whole_domain):
        """Sets the is_whole_domain of this GlobalCdnPurgeHistory.

        전체도메인퍼지여부  # noqa: E501

        :param is_whole_domain: The is_whole_domain of this GlobalCdnPurgeHistory.  # noqa: E501
        :type: bool
        """

        self._is_whole_domain = is_whole_domain

    @property
    def global_cdn_service_domain_list(self):
        """Gets the global_cdn_service_domain_list of this GlobalCdnPurgeHistory.  # noqa: E501

        Global CDN서비스도메인리스트  # noqa: E501

        :return: The global_cdn_service_domain_list of this GlobalCdnPurgeHistory.  # noqa: E501
        :rtype: list[GlobalCdnServiceDomain]
        """
        return self._global_cdn_service_domain_list

    @global_cdn_service_domain_list.setter
    def global_cdn_service_domain_list(self, global_cdn_service_domain_list):
        """Sets the global_cdn_service_domain_list of this GlobalCdnPurgeHistory.

        Global CDN서비스도메인리스트  # noqa: E501

        :param global_cdn_service_domain_list: The global_cdn_service_domain_list of this GlobalCdnPurgeHistory.  # noqa: E501
        :type: list[GlobalCdnServiceDomain]
        """

        self._global_cdn_service_domain_list = global_cdn_service_domain_list

    @property
    def target_file_list(self):
        """Gets the target_file_list of this GlobalCdnPurgeHistory.  # noqa: E501

        타겟파일리스트  # noqa: E501

        :return: The target_file_list of this GlobalCdnPurgeHistory.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_file_list

    @target_file_list.setter
    def target_file_list(self, target_file_list):
        """Sets the target_file_list of this GlobalCdnPurgeHistory.

        타겟파일리스트  # noqa: E501

        :param target_file_list: The target_file_list of this GlobalCdnPurgeHistory.  # noqa: E501
        :type: list[str]
        """

        self._target_file_list = target_file_list

    @property
    def estimated_completion_date(self):
        """Gets the estimated_completion_date of this GlobalCdnPurgeHistory.  # noqa: E501

        예상완료날짜  # noqa: E501

        :return: The estimated_completion_date of this GlobalCdnPurgeHistory.  # noqa: E501
        :rtype: str
        """
        return self._estimated_completion_date

    @estimated_completion_date.setter
    def estimated_completion_date(self, estimated_completion_date):
        """Sets the estimated_completion_date of this GlobalCdnPurgeHistory.

        예상완료날짜  # noqa: E501

        :param estimated_completion_date: The estimated_completion_date of this GlobalCdnPurgeHistory.  # noqa: E501
        :type: str
        """

        self._estimated_completion_date = estimated_completion_date

    @property
    def is_success(self):
        """Gets the is_success of this GlobalCdnPurgeHistory.  # noqa: E501

        성공여부  # noqa: E501

        :return: The is_success of this GlobalCdnPurgeHistory.  # noqa: E501
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this GlobalCdnPurgeHistory.

        성공여부  # noqa: E501

        :param is_success: The is_success of this GlobalCdnPurgeHistory.  # noqa: E501
        :type: bool
        """

        self._is_success = is_success

    @property
    def request_date(self):
        """Gets the request_date of this GlobalCdnPurgeHistory.  # noqa: E501

        요청날짜  # noqa: E501

        :return: The request_date of this GlobalCdnPurgeHistory.  # noqa: E501
        :rtype: str
        """
        return self._request_date

    @request_date.setter
    def request_date(self, request_date):
        """Sets the request_date of this GlobalCdnPurgeHistory.

        요청날짜  # noqa: E501

        :param request_date: The request_date of this GlobalCdnPurgeHistory.  # noqa: E501
        :type: str
        """

        self._request_date = request_date

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
        if not isinstance(other, GlobalCdnPurgeHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
