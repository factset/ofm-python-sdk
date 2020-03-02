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


class GetResourceDto(object):


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
        'file_name': 'str',
        'description': 'str',
        'url': 'str',
        'order': 'int',
        'is_file': 'bool',
        'is_public': 'bool',
        'category_id': 'str',
        'created': 'int',
        'updated': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'file_name': 'fileName',
        'description': 'description',
        'url': 'url',
        'order': 'order',
        'is_file': 'isFile',
        'is_public': 'isPublic',
        'category_id': 'categoryId',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, name=None, file_name=None, description=None, url=None, order=None, is_file=None, is_public=None, category_id=None, created=None, updated=None):  # noqa: E501
        """GetResourceDto - a model defined in ofm"""  # noqa: E501

        self._id = None
        self._name = None
        self._file_name = None
        self._description = None
        self._url = None
        self._order = None
        self._is_file = None
        self._is_public = None
        self._category_id = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if file_name is not None:
            self.file_name = file_name
        if description is not None:
            self.description = description
        if url is not None:
            self.url = url
        if order is not None:
            self.order = order
        if is_file is not None:
            self.is_file = is_file
        if is_public is not None:
            self.is_public = is_public
        if category_id is not None:
            self.category_id = category_id
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        """Gets the id of this GetResourceDto.  # noqa: E501


        :return: The id of this GetResourceDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetResourceDto.


        :param id: The id of this GetResourceDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetResourceDto.  # noqa: E501


        :return: The name of this GetResourceDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetResourceDto.


        :param name: The name of this GetResourceDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def file_name(self):
        """Gets the file_name of this GetResourceDto.  # noqa: E501


        :return: The file_name of this GetResourceDto.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this GetResourceDto.


        :param file_name: The file_name of this GetResourceDto.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def description(self):
        """Gets the description of this GetResourceDto.  # noqa: E501


        :return: The description of this GetResourceDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetResourceDto.


        :param description: The description of this GetResourceDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def url(self):
        """Gets the url of this GetResourceDto.  # noqa: E501


        :return: The url of this GetResourceDto.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetResourceDto.


        :param url: The url of this GetResourceDto.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def order(self):
        """Gets the order of this GetResourceDto.  # noqa: E501


        :return: The order of this GetResourceDto.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this GetResourceDto.


        :param order: The order of this GetResourceDto.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def is_file(self):
        """Gets the is_file of this GetResourceDto.  # noqa: E501


        :return: The is_file of this GetResourceDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_file

    @is_file.setter
    def is_file(self, is_file):
        """Sets the is_file of this GetResourceDto.


        :param is_file: The is_file of this GetResourceDto.  # noqa: E501
        :type: bool
        """

        self._is_file = is_file

    @property
    def is_public(self):
        """Gets the is_public of this GetResourceDto.  # noqa: E501


        :return: The is_public of this GetResourceDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this GetResourceDto.


        :param is_public: The is_public of this GetResourceDto.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def category_id(self):
        """Gets the category_id of this GetResourceDto.  # noqa: E501


        :return: The category_id of this GetResourceDto.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this GetResourceDto.


        :param category_id: The category_id of this GetResourceDto.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def created(self):
        """Gets the created of this GetResourceDto.  # noqa: E501


        :return: The created of this GetResourceDto.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetResourceDto.


        :param created: The created of this GetResourceDto.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this GetResourceDto.  # noqa: E501


        :return: The updated of this GetResourceDto.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this GetResourceDto.


        :param updated: The updated of this GetResourceDto.  # noqa: E501
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
        if issubclass(GetResourceDto, dict):
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
        if not isinstance(other, GetResourceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
