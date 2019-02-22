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
from quetzal._auto_client.models.inline_response2001 import InlineResponse2001  # noqa: E501
from quetzal._auto_client.rest import ApiException


class TestInlineResponse2001(unittest.TestCase):
    """InlineResponse2001 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineResponse2001(self):
        """Test InlineResponse2001"""
        # FIXME: construct object with mandatory attributes with example values
        # model = quetzal._auto_client.models.inline_response2001.InlineResponse2001()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
