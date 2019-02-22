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


class QueryApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def workspace_query_create(self, wid, inline_object4, **kwargs):  # noqa: E501
        """Prepare a query.  # noqa: E501

        Queries in Quetzal are saved as a resource associated to a workspace. This endpoint creates one and responds with a _see other_ status referencing the query details endpoint.  Since the query details contains the query results as a paginated list, this endpoint also accepts the normal pagination parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workspace_query_create(wid, inline_object4, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int wid: Workspace identifier (required)
        :param InlineObject4 inline_object4: (required)
        :param int page: The page of a collection to return.
        :param int per_page: Number of items to return per page.
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workspace_query_create_with_http_info(wid, inline_object4, **kwargs)  # noqa: E501
        else:
            (data) = self.workspace_query_create_with_http_info(wid, inline_object4, **kwargs)  # noqa: E501
            return data

    def workspace_query_create_with_http_info(self, wid, inline_object4, **kwargs):  # noqa: E501
        """Prepare a query.  # noqa: E501

        Queries in Quetzal are saved as a resource associated to a workspace. This endpoint creates one and responds with a _see other_ status referencing the query details endpoint.  Since the query details contains the query results as a paginated list, this endpoint also accepts the normal pagination parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workspace_query_create_with_http_info(wid, inline_object4, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int wid: Workspace identifier (required)
        :param InlineObject4 inline_object4: (required)
        :param int page: The page of a collection to return.
        :param int per_page: Number of items to return per page.
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['wid', 'inline_object4', 'page', 'per_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workspace_query_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'wid' is set
        if ('wid' not in local_var_params or
                local_var_params['wid'] is None):
            raise ValueError("Missing the required parameter `wid` when calling `workspace_query_create`")  # noqa: E501
        # verify the required parameter 'inline_object4' is set
        if ('inline_object4' not in local_var_params or
                local_var_params['inline_object4'] is None):
            raise ValueError("Missing the required parameter `inline_object4` when calling `workspace_query_create`")  # noqa: E501

        if 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `workspace_query_create`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] > 100000:  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `workspace_query_create`, must be a value less than or equal to `100000`")  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `workspace_query_create`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'wid' in local_var_params:
            path_params['wid'] = local_var_params['wid']  # noqa: E501

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_object4' in local_var_params:
            body_params = local_var_params['inline_object4']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/data/workspaces/{wid}/queries/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse201',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workspace_query_details(self, wid, qid, **kwargs):  # noqa: E501
        """Query details.  # noqa: E501

        The details of a query, which contains the query itself and a paginated list of its results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workspace_query_details(wid, qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int wid: Workspace identifier (required)
        :param int qid: Query identifier (required)
        :param int page: The page of a collection to return.
        :param int per_page: Number of items to return per page.
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workspace_query_details_with_http_info(wid, qid, **kwargs)  # noqa: E501
        else:
            (data) = self.workspace_query_details_with_http_info(wid, qid, **kwargs)  # noqa: E501
            return data

    def workspace_query_details_with_http_info(self, wid, qid, **kwargs):  # noqa: E501
        """Query details.  # noqa: E501

        The details of a query, which contains the query itself and a paginated list of its results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workspace_query_details_with_http_info(wid, qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int wid: Workspace identifier (required)
        :param int qid: Query identifier (required)
        :param int page: The page of a collection to return.
        :param int per_page: Number of items to return per page.
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['wid', 'qid', 'page', 'per_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workspace_query_details" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'wid' is set
        if ('wid' not in local_var_params or
                local_var_params['wid'] is None):
            raise ValueError("Missing the required parameter `wid` when calling `workspace_query_details`")  # noqa: E501
        # verify the required parameter 'qid' is set
        if ('qid' not in local_var_params or
                local_var_params['qid'] is None):
            raise ValueError("Missing the required parameter `qid` when calling `workspace_query_details`")  # noqa: E501

        if 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `workspace_query_details`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] > 100000:  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `workspace_query_details`, must be a value less than or equal to `100000`")  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `workspace_query_details`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'wid' in local_var_params:
            path_params['wid'] = local_var_params['wid']  # noqa: E501
        if 'qid' in local_var_params:
            path_params['qid'] = local_var_params['qid']  # noqa: E501

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501

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
            '/data/workspaces/{wid}/queries/{qid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse201',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workspace_query_fetch(self, wid, **kwargs):  # noqa: E501
        """List queries.  # noqa: E501

        List all the queries that are associated with a workspace. Note that each query listed here is shown _without_ its results, for brevity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workspace_query_fetch(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int wid: Workspace identifier (required)
        :param int page: The page of a collection to return.
        :param int per_page: Number of items to return per page.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workspace_query_fetch_with_http_info(wid, **kwargs)  # noqa: E501
        else:
            (data) = self.workspace_query_fetch_with_http_info(wid, **kwargs)  # noqa: E501
            return data

    def workspace_query_fetch_with_http_info(self, wid, **kwargs):  # noqa: E501
        """List queries.  # noqa: E501

        List all the queries that are associated with a workspace. Note that each query listed here is shown _without_ its results, for brevity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workspace_query_fetch_with_http_info(wid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int wid: Workspace identifier (required)
        :param int page: The page of a collection to return.
        :param int per_page: Number of items to return per page.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['wid', 'page', 'per_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workspace_query_fetch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'wid' is set
        if ('wid' not in local_var_params or
                local_var_params['wid'] is None):
            raise ValueError("Missing the required parameter `wid` when calling `workspace_query_fetch`")  # noqa: E501

        if 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `workspace_query_fetch`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] > 100000:  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `workspace_query_fetch`, must be a value less than or equal to `100000`")  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `workspace_query_fetch`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'wid' in local_var_params:
            path_params['wid'] = local_var_params['wid']  # noqa: E501

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))  # noqa: E501

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
            '/data/workspaces/{wid}/queries/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
