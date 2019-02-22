# coding: utf-8

"""
    Quetzalcoatl API

    Quetzal (short for Quetzalcoatl): an API to manage data files and their associated metadata.  # General documentation  ...  ## Concepts  * File * Metadata   Versioning too * Families * Workspace   Description, workspace states, data_url, etc. * Workspace views * Queries  # Errors  Quetzal uses standard HTTP error codes to indicate success or failure of its operations. The body of the response follows [RFC-7807](https://tools.ietf.org/html/rfc7807) to provide details on an error. For example:  ``` {   \"type\": \"https://quetz.al/problems/some-name\",   \"title\": \"Bad request.\",   \"status\": 400,   \"detail\": \"Incorrect foo due to missing bar.\",   \"instance\": \"/some_path/some_id\" } ```  # Versioning  API version | Changes ------------|--------- 0.1.0       | [API changes](https://quetz.al/docs/changelog#v0-1-0)   # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: support@quetz.al
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import quetzal._auto_client
from quetzal._auto_client.api.data_api import DataApi  # noqa: E501
from quetzal._auto_client.rest import ApiException


class TestDataApi(unittest.TestCase):
    """DataApi unit test stubs"""

    def setUp(self):
        self.api = quetzal._auto_client.api.data_api.DataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_public_file_details(self):
        """Test case for public_file_details

        Fetch file.  # noqa: E501
        """
        pass

    def test_workspace_commit(self):
        """Test case for workspace_commit

        Commit workspace.  # noqa: E501
        """
        pass

    def test_workspace_create(self):
        """Test case for workspace_create

        Create workspace.  # noqa: E501
        """
        pass

    def test_workspace_delete(self):
        """Test case for workspace_delete

        Delete workspace.  # noqa: E501
        """
        pass

    def test_workspace_details(self):
        """Test case for workspace_details

        Workspace details.  # noqa: E501
        """
        pass

    def test_workspace_fetch(self):
        """Test case for workspace_fetch

        List workspaces.  # noqa: E501
        """
        pass

    def test_workspace_file_create(self):
        """Test case for workspace_file_create

        Upload file.  # noqa: E501
        """
        pass

    def test_workspace_file_details(self):
        """Test case for workspace_file_details

        Fetch file.  # noqa: E501
        """
        pass

    def test_workspace_file_fetch(self):
        """Test case for workspace_file_fetch

        List files.  # noqa: E501
        """
        pass

    def test_workspace_file_set_metadata(self):
        """Test case for workspace_file_set_metadata

        Rewrite metadata.  # noqa: E501
        """
        pass

    def test_workspace_file_update_metadata(self):
        """Test case for workspace_file_update_metadata

        Modify metadata.  # noqa: E501
        """
        pass

    def test_workspace_query_create(self):
        """Test case for workspace_query_create

        Prepare a query.  # noqa: E501
        """
        pass

    def test_workspace_query_details(self):
        """Test case for workspace_query_details

        Query details.  # noqa: E501
        """
        pass

    def test_workspace_query_fetch(self):
        """Test case for workspace_query_fetch

        List queries.  # noqa: E501
        """
        pass

    def test_workspace_scan(self):
        """Test case for workspace_scan

        Update views.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
