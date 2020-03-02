# coding: utf-8

"""
    Open:FactSet Marketplace API

    Headless CMS API used by the Open:FactSet Marketplace.  # noqa: E501

    OpenAPI spec version: v2.1.5
    Contact: openfactset-frontend-engineering@factset.com
    
"""


import pprint
import re  # noqa: F401

import six


class GetAttributesGroupDtoAttributes(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'name': 'str',
        'group_id': 'str',
        'prod_type': 'str',
        'id': 'str',
        'created': 'int',
        'updated': 'int',
        'is_used': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'group_id': 'groupId',
        'prod_type': 'prodType',
        'id': 'id',
        'created': 'created',
        'updated': 'updated',
        'is_used': 'isUsed'
    }

    def __init__(self, name=None, group_id=None, prod_type=None, id=None, created=None, updated=None, is_used=None):  # noqa: E501
        """GetAttributesGroupDtoAttributes - a model defined in ofm"""  # noqa: E501

        self._name = None
        self._group_id = None
        self._prod_type = None
        self._id = None
        self._created = None
        self._updated = None
        self._is_used = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if group_id is not None:
            self.group_id = group_id
        if prod_type is not None:
            self.prod_type = prod_type
        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if is_used is not None:
            self.is_used = is_used

    @property
    def name(self):
        """Gets the name of this GetAttributesGroupDtoAttributes.  # noqa: E501


        :return: The name of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetAttributesGroupDtoAttributes.


        :param name: The name of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def group_id(self):
        """Gets the group_id of this GetAttributesGroupDtoAttributes.  # noqa: E501


        :return: The group_id of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GetAttributesGroupDtoAttributes.


        :param group_id: The group_id of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def prod_type(self):
        """Gets the prod_type of this GetAttributesGroupDtoAttributes.  # noqa: E501


        :return: The prod_type of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :rtype: str
        """
        return self._prod_type

    @prod_type.setter
    def prod_type(self, prod_type):
        """Sets the prod_type of this GetAttributesGroupDtoAttributes.


        :param prod_type: The prod_type of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :type: str
        """

        self._prod_type = prod_type

    @property
    def id(self):
        """Gets the id of this GetAttributesGroupDtoAttributes.  # noqa: E501


        :return: The id of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAttributesGroupDtoAttributes.


        :param id: The id of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this GetAttributesGroupDtoAttributes.  # noqa: E501


        :return: The created of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetAttributesGroupDtoAttributes.


        :param created: The created of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this GetAttributesGroupDtoAttributes.  # noqa: E501


        :return: The updated of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this GetAttributesGroupDtoAttributes.


        :param updated: The updated of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :type: int
        """

        self._updated = updated

    @property
    def is_used(self):
        """Gets the is_used of this GetAttributesGroupDtoAttributes.  # noqa: E501


        :return: The is_used of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._is_used

    @is_used.setter
    def is_used(self, is_used):
        """Sets the is_used of this GetAttributesGroupDtoAttributes.


        :param is_used: The is_used of this GetAttributesGroupDtoAttributes.  # noqa: E501
        :type: bool
        """

        self._is_used = is_used

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.ofm_types):
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
        if issubclass(GetAttributesGroupDtoAttributes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetAttributesGroupDtoAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
