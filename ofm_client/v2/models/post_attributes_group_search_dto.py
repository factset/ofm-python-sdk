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


class PostAttributesGroupSearchDto(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'limit': 'int',
        'page': 'int',
        'sort': 'str',
        'fields': 'str',
        'search': 'str',
        'filter': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'page': 'page',
        'sort': 'sort',
        'fields': 'fields',
        'search': 'search',
        'filter': 'filter'
    }

    def __init__(self, limit=None, page=None, sort='name:asc', fields=None, search=None, filter=None):  # noqa: E501
        """PostAttributesGroupSearchDto - a model defined in ofm"""  # noqa: E501

        self._limit = None
        self._page = None
        self._sort = None
        self._fields = None
        self._search = None
        self._filter = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if page is not None:
            self.page = page
        if sort is not None:
            self.sort = sort
        if fields is not None:
            self.fields = fields
        if search is not None:
            self.search = search
        if filter is not None:
            self.filter = filter

    @property
    def limit(self):
        """Gets the limit of this PostAttributesGroupSearchDto.  # noqa: E501

        Limit the amount of records per page.  # noqa: E501

        :return: The limit of this PostAttributesGroupSearchDto.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PostAttributesGroupSearchDto.

        Limit the amount of records per page.  # noqa: E501

        :param limit: The limit of this PostAttributesGroupSearchDto.  # noqa: E501
        :type: int
        """
        if limit is not None and limit > 300:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value less than or equal to `300`")  # noqa: E501

        self._limit = limit

    @property
    def page(self):
        """Gets the page of this PostAttributesGroupSearchDto.  # noqa: E501

        Select which page to show.  # noqa: E501

        :return: The page of this PostAttributesGroupSearchDto.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PostAttributesGroupSearchDto.

        Select which page to show.  # noqa: E501

        :param page: The page of this PostAttributesGroupSearchDto.  # noqa: E501
        :type: int
        """
        if page is not None and page < 1:  # noqa: E501
            raise ValueError("Invalid value for `page`, must be a value greater than or equal to `1`")  # noqa: E501

        self._page = page

    @property
    def sort(self):
        """Gets the sort of this PostAttributesGroupSearchDto.  # noqa: E501

        Sort according to  specific field value.  # noqa: E501

        :return: The sort of this PostAttributesGroupSearchDto.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this PostAttributesGroupSearchDto.

        Sort according to  specific field value.  # noqa: E501

        :param sort: The sort of this PostAttributesGroupSearchDto.  # noqa: E501
        :type: str
        """

        self._sort = sort

    @property
    def fields(self):
        """Gets the fields of this PostAttributesGroupSearchDto.  # noqa: E501

        Fetch only specific fields. The fields' names separated by a comma.  # noqa: E501

        :return: The fields of this PostAttributesGroupSearchDto.  # noqa: E501
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this PostAttributesGroupSearchDto.

        Fetch only specific fields. The fields' names separated by a comma.  # noqa: E501

        :param fields: The fields of this PostAttributesGroupSearchDto.  # noqa: E501
        :type: str
        """

        self._fields = fields

    @property
    def search(self):
        """Gets the search of this PostAttributesGroupSearchDto.  # noqa: E501

        Search for terms in certain fields.  # noqa: E501

        :return: The search of this PostAttributesGroupSearchDto.  # noqa: E501
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this PostAttributesGroupSearchDto.

        Search for terms in certain fields.  # noqa: E501

        :param search: The search of this PostAttributesGroupSearchDto.  # noqa: E501
        :type: str
        """

        self._search = search

    @property
    def filter(self):
        """Gets the filter of this PostAttributesGroupSearchDto.  # noqa: E501

        Filter against specific field values.  # noqa: E501

        :return: The filter of this PostAttributesGroupSearchDto.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this PostAttributesGroupSearchDto.

        Filter against specific field values.  # noqa: E501

        :param filter: The filter of this PostAttributesGroupSearchDto.  # noqa: E501
        :type: str
        """

        self._filter = filter

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
        if issubclass(PostAttributesGroupSearchDto, dict):
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
        if not isinstance(other, PostAttributesGroupSearchDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
