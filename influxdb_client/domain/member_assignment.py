# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class MemberAssignment(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'member': 'MemberExpression',
        'init': 'Expression'
    }

    attribute_map = {
        'type': 'type',
        'member': 'member',
        'init': 'init'
    }

    def __init__(self, type=None, member=None, init=None):  # noqa: E501
        """MemberAssignment - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._member = None
        self._init = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if member is not None:
            self.member = member
        if init is not None:
            self.init = init

    @property
    def type(self):
        """Gets the type of this MemberAssignment.  # noqa: E501

        Type of AST node  # noqa: E501

        :return: The type of this MemberAssignment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MemberAssignment.

        Type of AST node  # noqa: E501

        :param type: The type of this MemberAssignment.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def member(self):
        """Gets the member of this MemberAssignment.  # noqa: E501


        :return: The member of this MemberAssignment.  # noqa: E501
        :rtype: MemberExpression
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this MemberAssignment.


        :param member: The member of this MemberAssignment.  # noqa: E501
        :type: MemberExpression
        """

        self._member = member

    @property
    def init(self):
        """Gets the init of this MemberAssignment.  # noqa: E501


        :return: The init of this MemberAssignment.  # noqa: E501
        :rtype: Expression
        """
        return self._init

    @init.setter
    def init(self, init):
        """Sets the init of this MemberAssignment.


        :param init: The init of this MemberAssignment.  # noqa: E501
        :type: Expression
        """

        self._init = init

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, MemberAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
