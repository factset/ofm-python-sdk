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


class GetAttributesGroupDto(object):


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
        'prod_type': 'str',
        'color': 'str',
        'type': 'str',
        'selection': 'str',
        'created': 'int',
        'updated': 'int',
        'attributes': 'list[GetAttributesGroupDtoAttributes]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'prod_type': 'prodType',
        'color': 'color',
        'type': 'type',
        'selection': 'selection',
        'created': 'created',
        'updated': 'updated',
        'attributes': 'attributes'
    }

    def __init__(self, id=None, name=None, prod_type=None, color=None, type=None, selection=None, created=None, updated=None, attributes=None):  # noqa: E501
        """GetAttributesGroupDto - a model defined in ofm"""  # noqa: E501

        self._id = None
        self._name = None
        self._prod_type = None
        self._color = None
        self._type = None
        self._selection = None
        self._created = None
        self._updated = None
        self._attributes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if prod_type is not None:
            self.prod_type = prod_type
        if color is not None:
            self.color = color
        if type is not None:
            self.type = type
        if selection is not None:
            self.selection = selection
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if attributes is not None:
            self.attributes = attributes

    @property
    def id(self):
        """Gets the id of this GetAttributesGroupDto.  # noqa: E501


        :return: The id of this GetAttributesGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAttributesGroupDto.


        :param id: The id of this GetAttributesGroupDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetAttributesGroupDto.  # noqa: E501


        :return: The name of this GetAttributesGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetAttributesGroupDto.


        :param name: The name of this GetAttributesGroupDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def prod_type(self):
        """Gets the prod_type of this GetAttributesGroupDto.  # noqa: E501


        :return: The prod_type of this GetAttributesGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._prod_type

    @prod_type.setter
    def prod_type(self, prod_type):
        """Sets the prod_type of this GetAttributesGroupDto.


        :param prod_type: The prod_type of this GetAttributesGroupDto.  # noqa: E501
        :type: str
        """

        self._prod_type = prod_type

    @property
    def color(self):
        """Gets the color of this GetAttributesGroupDto.  # noqa: E501


        :return: The color of this GetAttributesGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this GetAttributesGroupDto.


        :param color: The color of this GetAttributesGroupDto.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def type(self):
        """Gets the type of this GetAttributesGroupDto.  # noqa: E501


        :return: The type of this GetAttributesGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetAttributesGroupDto.


        :param type: The type of this GetAttributesGroupDto.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def selection(self):
        """Gets the selection of this GetAttributesGroupDto.  # noqa: E501


        :return: The selection of this GetAttributesGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._selection

    @selection.setter
    def selection(self, selection):
        """Sets the selection of this GetAttributesGroupDto.


        :param selection: The selection of this GetAttributesGroupDto.  # noqa: E501
        :type: str
        """

        self._selection = selection

    @property
    def created(self):
        """Gets the created of this GetAttributesGroupDto.  # noqa: E501


        :return: The created of this GetAttributesGroupDto.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetAttributesGroupDto.


        :param created: The created of this GetAttributesGroupDto.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this GetAttributesGroupDto.  # noqa: E501


        :return: The updated of this GetAttributesGroupDto.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this GetAttributesGroupDto.


        :param updated: The updated of this GetAttributesGroupDto.  # noqa: E501
        :type: int
        """

        self._updated = updated

    @property
    def attributes(self):
        """Gets the attributes of this GetAttributesGroupDto.  # noqa: E501


        :return: The attributes of this GetAttributesGroupDto.  # noqa: E501
        :rtype: list[GetAttributesGroupDtoAttributes]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this GetAttributesGroupDto.


        :param attributes: The attributes of this GetAttributesGroupDto.  # noqa: E501
        :type: list[GetAttributesGroupDtoAttributes]
        """

        self._attributes = attributes

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
        if issubclass(GetAttributesGroupDto, dict):
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
        if not isinstance(other, GetAttributesGroupDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
