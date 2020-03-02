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


class GetResourcesSectionDto(object):


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
        'order': 'int',
        'created': 'int',
        'updated': 'int',
        'documents': 'list[GetResourceDto]',
        'meta': 'list[GetResourcesSectionDtoMeta]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'order': 'order',
        'created': 'created',
        'updated': 'updated',
        'documents': 'documents',
        'meta': 'meta'
    }

    def __init__(self, id=None, name=None, order=None, created=None, updated=None, documents=None, meta=None):  # noqa: E501
        """GetResourcesSectionDto - a model defined in ofm"""  # noqa: E501

        self._id = None
        self._name = None
        self._order = None
        self._created = None
        self._updated = None
        self._documents = None
        self._meta = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if order is not None:
            self.order = order
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if documents is not None:
            self.documents = documents
        if meta is not None:
            self.meta = meta

    @property
    def id(self):
        """Gets the id of this GetResourcesSectionDto.  # noqa: E501


        :return: The id of this GetResourcesSectionDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetResourcesSectionDto.


        :param id: The id of this GetResourcesSectionDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetResourcesSectionDto.  # noqa: E501


        :return: The name of this GetResourcesSectionDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetResourcesSectionDto.


        :param name: The name of this GetResourcesSectionDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order(self):
        """Gets the order of this GetResourcesSectionDto.  # noqa: E501


        :return: The order of this GetResourcesSectionDto.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this GetResourcesSectionDto.


        :param order: The order of this GetResourcesSectionDto.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def created(self):
        """Gets the created of this GetResourcesSectionDto.  # noqa: E501


        :return: The created of this GetResourcesSectionDto.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetResourcesSectionDto.


        :param created: The created of this GetResourcesSectionDto.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this GetResourcesSectionDto.  # noqa: E501


        :return: The updated of this GetResourcesSectionDto.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this GetResourcesSectionDto.


        :param updated: The updated of this GetResourcesSectionDto.  # noqa: E501
        :type: int
        """

        self._updated = updated

    @property
    def documents(self):
        """Gets the documents of this GetResourcesSectionDto.  # noqa: E501


        :return: The documents of this GetResourcesSectionDto.  # noqa: E501
        :rtype: list[GetResourceDto]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this GetResourcesSectionDto.


        :param documents: The documents of this GetResourcesSectionDto.  # noqa: E501
        :type: list[GetResourceDto]
        """

        self._documents = documents

    @property
    def meta(self):
        """Gets the meta of this GetResourcesSectionDto.  # noqa: E501


        :return: The meta of this GetResourcesSectionDto.  # noqa: E501
        :rtype: list[GetResourcesSectionDtoMeta]
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this GetResourcesSectionDto.


        :param meta: The meta of this GetResourcesSectionDto.  # noqa: E501
        :type: list[GetResourcesSectionDtoMeta]
        """

        self._meta = meta

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
        if issubclass(GetResourcesSectionDto, dict):
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
        if not isinstance(other, GetResourcesSectionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
