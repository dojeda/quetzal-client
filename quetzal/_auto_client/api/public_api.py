# coding: utf-8

"""
    Quetzalcoatl API

    Quetzal (short for Quetzalcoatl): an API to manage data files and their associated metadata.  # General documentation  ...  ## Concepts  * File * Metadata   Versioning too * Families * Workspace   Description, workspace states, data_url, etc. * Workspace views * Queries  # Errors  Quetzal uses standard HTTP error codes to indicate success or failure of its operations. The body of the response follows [RFC-7807](https://tools.ietf.org/html/rfc7807) to provide details on an error. For example:  ``` {   \"type\": \"https://quetz.al/problems/some-name\",   \"title\": \"Bad request.\",   \"status\": 400,   \"detail\": \"Incorrect foo due to missing bar.\",   \"instance\": \"/some_path/some_id\" } ```  # Versioning  API version | Changes ------------|--------- 0.1.0       | [API changes](https://quetz.al/docs/changelog#v0-1-0)   # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: support@quetz.al
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from quetzal._auto_client.api_client import ApiClient


class PublicApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def public_file_details(self, uuid, **kwargs):  # noqa: E501
        """Fetch file.  # noqa: E501

        This endpoint can be used to fetch the file contents or its metadata. The type of response, data or metadata, depends on the `Accept` request header. In the case of metadata, this endpoint returns the most recent metadata that has been committed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_file_details(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: File identifier (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.public_file_details_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.public_file_details_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def public_file_details_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Fetch file.  # noqa: E501

        This endpoint can be used to fetch the file contents or its metadata. The type of response, data or metadata, depends on the `Accept` request header. In the case of metadata, this endpoint returns the most recent metadata that has been committed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_file_details_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: File identifier (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method public_file_details" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in local_var_params or
                local_var_params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `public_file_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in local_var_params:
            path_params['uuid'] = local_var_params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/octet-stream', 'application/problem+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/data/files/{uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workspace_create(self, inline_object, **kwargs):  # noqa: E501
        """Create workspace.  # noqa: E501

        Create a workspace, which initializes the basic resources and information associated with it, and then schedules some background tasks to initialize Cloud resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workspace_create(inline_object, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InlineObject inline_object: (required)
        :return: InlineResponse2001Results
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workspace_create_with_http_info(inline_object, **kwargs)  # noqa: E501
        else:
            (data) = self.workspace_create_with_http_info(inline_object, **kwargs)  # noqa: E501
            return data

    def workspace_create_with_http_info(self, inline_object, **kwargs):  # noqa: E501
        """Create workspace.  # noqa: E501

        Create a workspace, which initializes the basic resources and information associated with it, and then schedules some background tasks to initialize Cloud resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workspace_create_with_http_info(inline_object, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InlineObject inline_object: (required)
        :return: InlineResponse2001Results
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['inline_object']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workspace_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'inline_object' is set
        if ('inline_object' not in local_var_params or
                local_var_params['inline_object'] is None):
            raise ValueError("Missing the required parameter `inline_object` when calling `workspace_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_object' in local_var_params:
            body_params = local_var_params['inline_object']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/data/workspaces/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001Results',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workspace_fetch(self, **kwargs):  # noqa: E501
        """List workspaces.  # noqa: E501

        List workspace details. Optionally, filter workspaces according to their name, owner or whether they have been deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workspace_fetch(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of a collection to return.
        :param int per_page: Number of items to return per page.
        :param str name: Filter workspaces by name
        :param str owner: Filter workspaces by owner
        :param bool deleted: Include deleted workspaces
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workspace_fetch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.workspace_fetch_with_http_info(**kwargs)  # noqa: E501
            return data

    def workspace_fetch_with_http_info(self, **kwargs):  # noqa: E501
        """List workspaces.  # noqa: E501

        List workspace details. Optionally, filter workspaces according to their name, owner or whether they have been deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workspace_fetch_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page of a collection to return.
        :param int per_page: Number of items to return per page.
        :param str name: Filter workspaces by name
        :param str owner: Filter workspaces by owner
        :param bool deleted: Include deleted workspaces
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['page', 'per_page', 'name', 'owner', 'deleted']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workspace_fetch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `workspace_fetch`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] > 100000:  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `workspace_fetch`, must be a value less than or equal to `100000`")  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `workspace_fetch`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))  # noqa: E501
        if 'deleted' in local_var_params:
            query_params.append(('deleted', local_var_params['deleted']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/data/workspaces/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
