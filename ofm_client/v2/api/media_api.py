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


class MediaApi(object):
    

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def media_download_namespace_scope_guid_file_name_get(self, namespace, scope, guid, file_name, **kwargs):  # noqa: E501
        """Retrieve a specific media file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_download_namespace_scope_guid_file_name_get(namespace, scope, guid, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace of the media file (required)
        :param str scope: The scope of the media file (required)
        :param str guid: The GUID of the file being requested (required)
        :param str file_name: The name you want to show for this file in the uri. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.media_download_namespace_scope_guid_file_name_get_with_http_info(namespace, scope, guid, file_name, **kwargs)  # noqa: E501
        else:
            (data) = self.media_download_namespace_scope_guid_file_name_get_with_http_info(namespace, scope, guid, file_name, **kwargs)  # noqa: E501
            return data

    def media_download_namespace_scope_guid_file_name_get_with_http_info(self, namespace, scope, guid, file_name, **kwargs):  # noqa: E501
        """Retrieve a specific media file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_download_namespace_scope_guid_file_name_get_with_http_info(namespace, scope, guid, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace of the media file (required)
        :param str scope: The scope of the media file (required)
        :param str guid: The GUID of the file being requested (required)
        :param str file_name: The name you want to show for this file in the uri. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'scope', 'guid', 'file_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_download_namespace_scope_guid_file_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `media_download_namespace_scope_guid_file_name_get`")  # noqa: E501
        # verify the required parameter 'scope' is set
        if ('scope' not in params or
                params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `media_download_namespace_scope_guid_file_name_get`")  # noqa: E501
        # verify the required parameter 'guid' is set
        if ('guid' not in params or
                params['guid'] is None):
            raise ValueError("Missing the required parameter `guid` when calling `media_download_namespace_scope_guid_file_name_get`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if ('file_name' not in params or
                params['file_name'] is None):
            raise ValueError("Missing the required parameter `file_name` when calling `media_download_namespace_scope_guid_file_name_get`")  # noqa: E501

        if 'namespace' in params and not re.search(r'(partners|products|resources)', params['namespace']):  # noqa: E501
            raise ValueError("Invalid value for parameter `namespace` when calling `media_download_namespace_scope_guid_file_name_get`, must conform to the pattern `/(partners|products|resources)/`")  # noqa: E501
        if 'scope' in params and not re.search(r'(logo|avatar|documents)', params['scope']):  # noqa: E501
            raise ValueError("Invalid value for parameter `scope` when calling `media_download_namespace_scope_guid_file_name_get`, must conform to the pattern `/(logo|avatar|documents)/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'scope' in params:
            path_params['scope'] = params['scope']  # noqa: E501
        if 'guid' in params:
            path_params['guid'] = params['guid']  # noqa: E501
        if 'file_name' in params:
            path_params['fileName'] = params['file_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Basic']  # noqa: E501

        return self.api_client.call_api(
            '/media/download/{namespace}/{scope}/{guid}/{fileName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def media_download_namespace_scope_guid_file_name_head(self, namespace, scope, guid, file_name, **kwargs):  # noqa: E501
        """Check the existence and retrieve the headers of a spefic media file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_download_namespace_scope_guid_file_name_head(namespace, scope, guid, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace of the media file (required)
        :param str scope: The scope of the media file (required)
        :param str guid: The GUID of the file being requested (required)
        :param str file_name: The name you want to show for this file in the uri. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.media_download_namespace_scope_guid_file_name_head_with_http_info(namespace, scope, guid, file_name, **kwargs)  # noqa: E501
        else:
            (data) = self.media_download_namespace_scope_guid_file_name_head_with_http_info(namespace, scope, guid, file_name, **kwargs)  # noqa: E501
            return data

    def media_download_namespace_scope_guid_file_name_head_with_http_info(self, namespace, scope, guid, file_name, **kwargs):  # noqa: E501
        """Check the existence and retrieve the headers of a spefic media file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_download_namespace_scope_guid_file_name_head_with_http_info(namespace, scope, guid, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace of the media file (required)
        :param str scope: The scope of the media file (required)
        :param str guid: The GUID of the file being requested (required)
        :param str file_name: The name you want to show for this file in the uri. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'scope', 'guid', 'file_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_download_namespace_scope_guid_file_name_head" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `media_download_namespace_scope_guid_file_name_head`")  # noqa: E501
        # verify the required parameter 'scope' is set
        if ('scope' not in params or
                params['scope'] is None):
            raise ValueError("Missing the required parameter `scope` when calling `media_download_namespace_scope_guid_file_name_head`")  # noqa: E501
        # verify the required parameter 'guid' is set
        if ('guid' not in params or
                params['guid'] is None):
            raise ValueError("Missing the required parameter `guid` when calling `media_download_namespace_scope_guid_file_name_head`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if ('file_name' not in params or
                params['file_name'] is None):
            raise ValueError("Missing the required parameter `file_name` when calling `media_download_namespace_scope_guid_file_name_head`")  # noqa: E501

        if 'namespace' in params and not re.search(r'(partners|products|resources)', params['namespace']):  # noqa: E501
            raise ValueError("Invalid value for parameter `namespace` when calling `media_download_namespace_scope_guid_file_name_head`, must conform to the pattern `/(partners|products|resources)/`")  # noqa: E501
        if 'scope' in params and not re.search(r'(logo|avatar|documents)', params['scope']):  # noqa: E501
            raise ValueError("Invalid value for parameter `scope` when calling `media_download_namespace_scope_guid_file_name_head`, must conform to the pattern `/(logo|avatar|documents)/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'scope' in params:
            path_params['scope'] = params['scope']  # noqa: E501
        if 'guid' in params:
            path_params['guid'] = params['guid']  # noqa: E501
        if 'file_name' in params:
            path_params['fileName'] = params['file_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Basic']  # noqa: E501

        return self.api_client.call_api(
            '/media/download/{namespace}/{scope}/{guid}/{fileName}', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
