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


class GetAttributeDto(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'id': 'str',
        'name': 'str',
        'group_id': 'str',
        'prod_type': 'str',
        'created': 'int',
        'updated': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'group_id': 'groupId',
        'prod_type': 'prodType',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, name=None, group_id=None, prod_type=None, created=None, updated=None):  # noqa: E501
        """GetAttributeDto - a model defined in ofm"""  # noqa: E501

        self._id = None
        self._name = None
        self._group_id = None
        self._prod_type = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if group_id is not None:
            self.group_id = group_id
        if prod_type is not None:
            self.prod_type = prod_type
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        """Gets the id of this GetAttributeDto.  # noqa: E501


        :return: The id of this GetAttributeDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAttributeDto.


        :param id: The id of this GetAttributeDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetAttributeDto.  # noqa: E501


        :return: The name of this GetAttributeDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetAttributeDto.


        :param name: The name of this GetAttributeDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def group_id(self):
        """Gets the group_id of this GetAttributeDto.  # noqa: E501


        :return: The group_id of this GetAttributeDto.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GetAttributeDto.


        :param group_id: The group_id of this GetAttributeDto.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def prod_type(self):
        """Gets the prod_type of this GetAttributeDto.  # noqa: E501


        :return: The prod_type of this GetAttributeDto.  # noqa: E501
        :rtype: str
        """
        return self._prod_type

    @prod_type.setter
    def prod_type(self, prod_type):
        """Sets the prod_type of this GetAttributeDto.


        :param prod_type: The prod_type of this GetAttributeDto.  # noqa: E501
        :type: str
        """

        self._prod_type = prod_type

    @property
    def created(self):
        """Gets the created of this GetAttributeDto.  # noqa: E501


        :return: The created of this GetAttributeDto.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetAttributeDto.


        :param created: The created of this GetAttributeDto.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this GetAttributeDto.  # noqa: E501


        :return: The updated of this GetAttributeDto.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this GetAttributeDto.


        :param updated: The updated of this GetAttributeDto.  # noqa: E501
        :type: int
        """

        self._updated = updated

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
        if issubclass(GetAttributeDto, dict):
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
        if not isinstance(other, GetAttributeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
