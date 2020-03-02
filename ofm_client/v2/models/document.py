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


class Document(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'name': 'str',
        'description': 'str',
        'file_name': 'str',
        'url': 'str',
        'is_file': 'bool',
        'is_public': 'bool',
        'order': 'int',
        'section': 'list[DocumentSection]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'file_name': 'fileName',
        'url': 'url',
        'is_file': 'isFile',
        'is_public': 'isPublic',
        'order': 'order',
        'section': 'section'
    }

    def __init__(self, name=None, description=None, file_name=None, url=None, is_file=None, is_public=None, order=None, section=None):  # noqa: E501
        """Document - a model defined in ofm"""  # noqa: E501

        self._name = None
        self._description = None
        self._file_name = None
        self._url = None
        self._is_file = None
        self._is_public = None
        self._order = None
        self._section = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if file_name is not None:
            self.file_name = file_name
        if url is not None:
            self.url = url
        if is_file is not None:
            self.is_file = is_file
        if is_public is not None:
            self.is_public = is_public
        if order is not None:
            self.order = order
        if section is not None:
            self.section = section

    @property
    def name(self):
        """Gets the name of this Document.  # noqa: E501


        :return: The name of this Document.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Document.


        :param name: The name of this Document.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Document.  # noqa: E501


        :return: The description of this Document.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Document.


        :param description: The description of this Document.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file_name(self):
        """Gets the file_name of this Document.  # noqa: E501


        :return: The file_name of this Document.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Document.


        :param file_name: The file_name of this Document.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def url(self):
        """Gets the url of this Document.  # noqa: E501


        :return: The url of this Document.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Document.


        :param url: The url of this Document.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def is_file(self):
        """Gets the is_file of this Document.  # noqa: E501


        :return: The is_file of this Document.  # noqa: E501
        :rtype: bool
        """
        return self._is_file

    @is_file.setter
    def is_file(self, is_file):
        """Sets the is_file of this Document.


        :param is_file: The is_file of this Document.  # noqa: E501
        :type: bool
        """

        self._is_file = is_file

    @property
    def is_public(self):
        """Gets the is_public of this Document.  # noqa: E501


        :return: The is_public of this Document.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this Document.


        :param is_public: The is_public of this Document.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def order(self):
        """Gets the order of this Document.  # noqa: E501


        :return: The order of this Document.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Document.


        :param order: The order of this Document.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def section(self):
        """Gets the section of this Document.  # noqa: E501


        :return: The section of this Document.  # noqa: E501
        :rtype: list[DocumentSection]
        """
        return self._section

    @section.setter
    def section(self, section):
        """Sets the section of this Document.


        :param section: The section of this Document.  # noqa: E501
        :type: list[DocumentSection]
        """

        self._section = section

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
        if issubclass(Document, dict):
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
        if not isinstance(other, Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
