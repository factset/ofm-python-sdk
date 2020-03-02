# coding: utf-8

"""
    Open:FactSet Marketplace API

    Headless CMS API used by the Open:FactSet Marketplace.  # noqa: E501

    OpenAPI spec version: v2.1.5
    Contact: openfactset-frontend-engineering@factset.com
    
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ofm_client.v2.api_client import ApiClient


class ProductsApi(object):
    

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def products_get(self, **kwargs):  # noqa: E501
        """Retrieve a collection of Product records.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Limit the amount of records per page
        :param int page: Select which page to show
        :return: list[GetProductDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.products_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.products_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def products_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a collection of Product records.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Limit the amount of records per page
        :param int page: Select which page to show
        :return: list[GetProductDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method products_get" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `products_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Basic']  # noqa: E501

        return self.api_client.call_api(
            '/products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetProductDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def products_id_get(self, id, **kwargs):  # noqa: E501
        """Retrieve a specific Product record.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Globally unique identifier (GUID) of a Product record (required)
        :return: GetProductDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.products_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.products_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def products_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve a specific Product record.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Globally unique identifier (GUID) of a Product record (required)
        :return: GetProductDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method products_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `products_id_get`")  # noqa: E501

        if 'id' in params and not re.search(r'\\{?[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}\\}?', params['id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `id` when calling `products_id_get`, must conform to the pattern `/\\{?[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}\\}?/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Basic']  # noqa: E501

        return self.api_client.call_api(
            '/products/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetProductDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def products_search_post(self, **kwargs):  # noqa: E501
        """Retrieve a collection of Product records.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_search_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostProductSearchDto body:
        :return: list[GetProductDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.products_search_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.products_search_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def products_search_post_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a collection of Product records.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_search_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostProductSearchDto body:
        :return: list[GetProductDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method products_search_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['Basic']  # noqa: E501

        return self.api_client.call_api(
            '/products/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetProductDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def products_types_get(self, **kwargs):  # noqa: E501
        """Retrieve a collection of the available Product Types along with the number of published products per type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_types_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[InlineResponse200]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.products_types_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.products_types_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def products_types_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a collection of the available Product Types along with the number of published products per type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.products_types_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[InlineResponse200]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method products_types_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Basic']  # noqa: E501

        return self.api_client.call_api(
            '/products/types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse200]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
