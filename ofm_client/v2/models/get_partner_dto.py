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


class GetPartnerDto(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'id': 'str',
        'logo_url': 'str',
        'forum_tags': 'list[GetPartnerDtoForumTags]',
        'video_url': 'str',
        'firm_info': 'str',
        'social_media': 'GetPartnerDtoSocialMedia',
        'name': 'str',
        'firm_id': 'int',
        'company_url': 'str',
        'seo_meta': 'GetPartnerDtoSeoMeta',
        'published_date': 'int',
        'slug': 'str',
        'marking': 'Marking',
        'created': 'int',
        'updated': 'int',
        'version_schema': 'GetPartnerDtoVersionSchema'
    }

    attribute_map = {
        'id': 'id',
        'logo_url': 'logoUrl',
        'forum_tags': 'forumTags',
        'video_url': 'videoUrl',
        'firm_info': 'firmInfo',
        'social_media': 'socialMedia',
        'name': 'name',
        'firm_id': 'firmId',
        'company_url': 'companyUrl',
        'seo_meta': 'seoMeta',
        'published_date': 'publishedDate',
        'slug': 'slug',
        'marking': 'marking',
        'created': 'created',
        'updated': 'updated',
        'version_schema': 'versionSchema'
    }

    def __init__(self, id=None, logo_url=None, forum_tags=None, video_url=None, firm_info=None, social_media=None, name=None, firm_id=None, company_url=None, seo_meta=None, published_date=None, slug=None, marking=None, created=None, updated=None, version_schema=None):  # noqa: E501
        """GetPartnerDto - a model defined in ofm"""  # noqa: E501

        self._id = None
        self._logo_url = None
        self._forum_tags = None
        self._video_url = None
        self._firm_info = None
        self._social_media = None
        self._name = None
        self._firm_id = None
        self._company_url = None
        self._seo_meta = None
        self._published_date = None
        self._slug = None
        self._marking = None
        self._created = None
        self._updated = None
        self._version_schema = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if logo_url is not None:
            self.logo_url = logo_url
        if forum_tags is not None:
            self.forum_tags = forum_tags
        if video_url is not None:
            self.video_url = video_url
        if firm_info is not None:
            self.firm_info = firm_info
        if social_media is not None:
            self.social_media = social_media
        if name is not None:
            self.name = name
        if firm_id is not None:
            self.firm_id = firm_id
        if company_url is not None:
            self.company_url = company_url
        if seo_meta is not None:
            self.seo_meta = seo_meta
        if published_date is not None:
            self.published_date = published_date
        if slug is not None:
            self.slug = slug
        if marking is not None:
            self.marking = marking
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if version_schema is not None:
            self.version_schema = version_schema

    @property
    def id(self):
        """Gets the id of this GetPartnerDto.  # noqa: E501


        :return: The id of this GetPartnerDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetPartnerDto.


        :param id: The id of this GetPartnerDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def logo_url(self):
        """Gets the logo_url of this GetPartnerDto.  # noqa: E501


        :return: The logo_url of this GetPartnerDto.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this GetPartnerDto.


        :param logo_url: The logo_url of this GetPartnerDto.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def forum_tags(self):
        """Gets the forum_tags of this GetPartnerDto.  # noqa: E501


        :return: The forum_tags of this GetPartnerDto.  # noqa: E501
        :rtype: list[GetPartnerDtoForumTags]
        """
        return self._forum_tags

    @forum_tags.setter
    def forum_tags(self, forum_tags):
        """Sets the forum_tags of this GetPartnerDto.


        :param forum_tags: The forum_tags of this GetPartnerDto.  # noqa: E501
        :type: list[GetPartnerDtoForumTags]
        """

        self._forum_tags = forum_tags

    @property
    def video_url(self):
        """Gets the video_url of this GetPartnerDto.  # noqa: E501


        :return: The video_url of this GetPartnerDto.  # noqa: E501
        :rtype: str
        """
        return self._video_url

    @video_url.setter
    def video_url(self, video_url):
        """Sets the video_url of this GetPartnerDto.


        :param video_url: The video_url of this GetPartnerDto.  # noqa: E501
        :type: str
        """

        self._video_url = video_url

    @property
    def firm_info(self):
        """Gets the firm_info of this GetPartnerDto.  # noqa: E501


        :return: The firm_info of this GetPartnerDto.  # noqa: E501
        :rtype: str
        """
        return self._firm_info

    @firm_info.setter
    def firm_info(self, firm_info):
        """Sets the firm_info of this GetPartnerDto.


        :param firm_info: The firm_info of this GetPartnerDto.  # noqa: E501
        :type: str
        """

        self._firm_info = firm_info

    @property
    def social_media(self):
        """Gets the social_media of this GetPartnerDto.  # noqa: E501


        :return: The social_media of this GetPartnerDto.  # noqa: E501
        :rtype: GetPartnerDtoSocialMedia
        """
        return self._social_media

    @social_media.setter
    def social_media(self, social_media):
        """Sets the social_media of this GetPartnerDto.


        :param social_media: The social_media of this GetPartnerDto.  # noqa: E501
        :type: GetPartnerDtoSocialMedia
        """

        self._social_media = social_media

    @property
    def name(self):
        """Gets the name of this GetPartnerDto.  # noqa: E501


        :return: The name of this GetPartnerDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetPartnerDto.


        :param name: The name of this GetPartnerDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def firm_id(self):
        """Gets the firm_id of this GetPartnerDto.  # noqa: E501


        :return: The firm_id of this GetPartnerDto.  # noqa: E501
        :rtype: int
        """
        return self._firm_id

    @firm_id.setter
    def firm_id(self, firm_id):
        """Sets the firm_id of this GetPartnerDto.


        :param firm_id: The firm_id of this GetPartnerDto.  # noqa: E501
        :type: int
        """

        self._firm_id = firm_id

    @property
    def company_url(self):
        """Gets the company_url of this GetPartnerDto.  # noqa: E501


        :return: The company_url of this GetPartnerDto.  # noqa: E501
        :rtype: str
        """
        return self._company_url

    @company_url.setter
    def company_url(self, company_url):
        """Sets the company_url of this GetPartnerDto.


        :param company_url: The company_url of this GetPartnerDto.  # noqa: E501
        :type: str
        """

        self._company_url = company_url

    @property
    def seo_meta(self):
        """Gets the seo_meta of this GetPartnerDto.  # noqa: E501


        :return: The seo_meta of this GetPartnerDto.  # noqa: E501
        :rtype: GetPartnerDtoSeoMeta
        """
        return self._seo_meta

    @seo_meta.setter
    def seo_meta(self, seo_meta):
        """Sets the seo_meta of this GetPartnerDto.


        :param seo_meta: The seo_meta of this GetPartnerDto.  # noqa: E501
        :type: GetPartnerDtoSeoMeta
        """

        self._seo_meta = seo_meta

    @property
    def published_date(self):
        """Gets the published_date of this GetPartnerDto.  # noqa: E501


        :return: The published_date of this GetPartnerDto.  # noqa: E501
        :rtype: int
        """
        return self._published_date

    @published_date.setter
    def published_date(self, published_date):
        """Sets the published_date of this GetPartnerDto.


        :param published_date: The published_date of this GetPartnerDto.  # noqa: E501
        :type: int
        """

        self._published_date = published_date

    @property
    def slug(self):
        """Gets the slug of this GetPartnerDto.  # noqa: E501


        :return: The slug of this GetPartnerDto.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this GetPartnerDto.


        :param slug: The slug of this GetPartnerDto.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def marking(self):
        """Gets the marking of this GetPartnerDto.  # noqa: E501


        :return: The marking of this GetPartnerDto.  # noqa: E501
        :rtype: Marking
        """
        return self._marking

    @marking.setter
    def marking(self, marking):
        """Sets the marking of this GetPartnerDto.


        :param marking: The marking of this GetPartnerDto.  # noqa: E501
        :type: Marking
        """

        self._marking = marking

    @property
    def created(self):
        """Gets the created of this GetPartnerDto.  # noqa: E501


        :return: The created of this GetPartnerDto.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetPartnerDto.


        :param created: The created of this GetPartnerDto.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this GetPartnerDto.  # noqa: E501


        :return: The updated of this GetPartnerDto.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this GetPartnerDto.


        :param updated: The updated of this GetPartnerDto.  # noqa: E501
        :type: int
        """

        self._updated = updated

    @property
    def version_schema(self):
        """Gets the version_schema of this GetPartnerDto.  # noqa: E501


        :return: The version_schema of this GetPartnerDto.  # noqa: E501
        :rtype: GetPartnerDtoVersionSchema
        """
        return self._version_schema

    @version_schema.setter
    def version_schema(self, version_schema):
        """Sets the version_schema of this GetPartnerDto.


        :param version_schema: The version_schema of this GetPartnerDto.  # noqa: E501
        :type: GetPartnerDtoVersionSchema
        """

        self._version_schema = version_schema

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
        if issubclass(GetPartnerDto, dict):
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
        if not isinstance(other, GetPartnerDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
