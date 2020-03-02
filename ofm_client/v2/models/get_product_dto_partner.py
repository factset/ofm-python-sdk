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


class GetProductDtoPartner(object):


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
        'slug': 'str',
        'logo_url': 'str',
        'firm_info': 'str',
        'company_url': 'str',
        'social_media': 'GetProductDtoPartnerSocialMedia'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'logo_url': 'logoUrl',
        'firm_info': 'firmInfo',
        'company_url': 'companyUrl',
        'social_media': 'socialMedia'
    }

    def __init__(self, id=None, name=None, slug=None, logo_url=None, firm_info=None, company_url=None, social_media=None):  # noqa: E501
        """GetProductDtoPartner - a model defined in ofm"""  # noqa: E501

        self._id = None
        self._name = None
        self._slug = None
        self._logo_url = None
        self._firm_info = None
        self._company_url = None
        self._social_media = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if logo_url is not None:
            self.logo_url = logo_url
        if firm_info is not None:
            self.firm_info = firm_info
        if company_url is not None:
            self.company_url = company_url
        if social_media is not None:
            self.social_media = social_media

    @property
    def id(self):
        """Gets the id of this GetProductDtoPartner.  # noqa: E501


        :return: The id of this GetProductDtoPartner.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetProductDtoPartner.


        :param id: The id of this GetProductDtoPartner.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetProductDtoPartner.  # noqa: E501


        :return: The name of this GetProductDtoPartner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetProductDtoPartner.


        :param name: The name of this GetProductDtoPartner.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this GetProductDtoPartner.  # noqa: E501


        :return: The slug of this GetProductDtoPartner.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this GetProductDtoPartner.


        :param slug: The slug of this GetProductDtoPartner.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def logo_url(self):
        """Gets the logo_url of this GetProductDtoPartner.  # noqa: E501


        :return: The logo_url of this GetProductDtoPartner.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this GetProductDtoPartner.


        :param logo_url: The logo_url of this GetProductDtoPartner.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def firm_info(self):
        """Gets the firm_info of this GetProductDtoPartner.  # noqa: E501


        :return: The firm_info of this GetProductDtoPartner.  # noqa: E501
        :rtype: str
        """
        return self._firm_info

    @firm_info.setter
    def firm_info(self, firm_info):
        """Sets the firm_info of this GetProductDtoPartner.


        :param firm_info: The firm_info of this GetProductDtoPartner.  # noqa: E501
        :type: str
        """

        self._firm_info = firm_info

    @property
    def company_url(self):
        """Gets the company_url of this GetProductDtoPartner.  # noqa: E501


        :return: The company_url of this GetProductDtoPartner.  # noqa: E501
        :rtype: str
        """
        return self._company_url

    @company_url.setter
    def company_url(self, company_url):
        """Sets the company_url of this GetProductDtoPartner.


        :param company_url: The company_url of this GetProductDtoPartner.  # noqa: E501
        :type: str
        """

        self._company_url = company_url

    @property
    def social_media(self):
        """Gets the social_media of this GetProductDtoPartner.  # noqa: E501


        :return: The social_media of this GetProductDtoPartner.  # noqa: E501
        :rtype: GetProductDtoPartnerSocialMedia
        """
        return self._social_media

    @social_media.setter
    def social_media(self, social_media):
        """Sets the social_media of this GetProductDtoPartner.


        :param social_media: The social_media of this GetProductDtoPartner.  # noqa: E501
        :type: GetProductDtoPartnerSocialMedia
        """

        self._social_media = social_media

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
        if issubclass(GetProductDtoPartner, dict):
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
        if not isinstance(other, GetProductDtoPartner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
