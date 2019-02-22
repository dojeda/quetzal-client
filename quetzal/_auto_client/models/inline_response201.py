# coding: utf-8

"""
    Quetzalcoatl API

    Quetzal (short for Quetzalcoatl): an API to manage data files and their associated metadata.  # General documentation  ...  ## Concepts  * File * Metadata   Versioning too * Families * Workspace   Description, workspace states, data_url, etc. * Workspace views * Queries  # Errors  Quetzal uses standard HTTP error codes to indicate success or failure of its operations. The body of the response follows [RFC-7807](https://tools.ietf.org/html/rfc7807) to provide details on an error. For example:  ``` {   \"type\": \"https://quetz.al/problems/some-name\",   \"title\": \"Bad request.\",   \"status\": 400,   \"detail\": \"Incorrect foo due to missing bar.\",   \"instance\": \"/some_path/some_id\" } ```  # Versioning  API version | Changes ------------|--------- 0.1.0       | [API changes](https://quetz.al/docs/changelog#v0-1-0)   # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: support@quetz.al
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse201(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'workspace_id': 'int',
        'dialect': 'str',
        'query': 'str',
        'page': 'int',
        'pages': 'int',
        'total': 'int',
        'results': 'list[object]'
    }

    attribute_map = {
        'id': 'id',
        'workspace_id': 'workspace_id',
        'dialect': 'dialect',
        'query': 'query',
        'page': 'page',
        'pages': 'pages',
        'total': 'total',
        'results': 'results'
    }

    def __init__(self, id=None, workspace_id=None, dialect=None, query=None, page=None, pages=None, total=None, results=None):  # noqa: E501
        """InlineResponse201 - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._workspace_id = None
        self._dialect = None
        self._query = None
        self._page = None
        self._pages = None
        self._total = None
        self._results = None
        self.discriminator = None

        self.id = id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        self.dialect = dialect
        self.query = query
        if page is not None:
            self.page = page
        if pages is not None:
            self.pages = pages
        if total is not None:
            self.total = total
        if results is not None:
            self.results = results

    @property
    def id(self):
        """Gets the id of this InlineResponse201.  # noqa: E501

        Query identifier  # noqa: E501

        :return: The id of this InlineResponse201.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse201.

        Query identifier  # noqa: E501

        :param id: The id of this InlineResponse201.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this InlineResponse201.  # noqa: E501

        Workspace identifier where the query operates  # noqa: E501

        :return: The workspace_id of this InlineResponse201.  # noqa: E501
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this InlineResponse201.

        Workspace identifier where the query operates  # noqa: E501

        :param workspace_id: The workspace_id of this InlineResponse201.  # noqa: E501
        :type: int
        """

        self._workspace_id = workspace_id

    @property
    def dialect(self):
        """Gets the dialect of this InlineResponse201.  # noqa: E501

        Dialect of query  # noqa: E501

        :return: The dialect of this InlineResponse201.  # noqa: E501
        :rtype: str
        """
        return self._dialect

    @dialect.setter
    def dialect(self, dialect):
        """Sets the dialect of this InlineResponse201.

        Dialect of query  # noqa: E501

        :param dialect: The dialect of this InlineResponse201.  # noqa: E501
        :type: str
        """
        if dialect is None:
            raise ValueError("Invalid value for `dialect`, must not be `None`")  # noqa: E501
        allowed_values = ["postgresql"]  # noqa: E501
        if dialect not in allowed_values:
            raise ValueError(
                "Invalid value for `dialect` ({0}), must be one of {1}"  # noqa: E501
                .format(dialect, allowed_values)
            )

        self._dialect = dialect

    @property
    def query(self):
        """Gets the query of this InlineResponse201.  # noqa: E501

        Query in code as needed by the dialect  # noqa: E501

        :return: The query of this InlineResponse201.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this InlineResponse201.

        Query in code as needed by the dialect  # noqa: E501

        :param query: The query of this InlineResponse201.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def page(self):
        """Gets the page of this InlineResponse201.  # noqa: E501

        Current page number  # noqa: E501

        :return: The page of this InlineResponse201.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this InlineResponse201.

        Current page number  # noqa: E501

        :param page: The page of this InlineResponse201.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def pages(self):
        """Gets the pages of this InlineResponse201.  # noqa: E501

        Number of pages available in the collection  # noqa: E501

        :return: The pages of this InlineResponse201.  # noqa: E501
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this InlineResponse201.

        Number of pages available in the collection  # noqa: E501

        :param pages: The pages of this InlineResponse201.  # noqa: E501
        :type: int
        """

        self._pages = pages

    @property
    def total(self):
        """Gets the total of this InlineResponse201.  # noqa: E501

        Total number of items in the collection  # noqa: E501

        :return: The total of this InlineResponse201.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InlineResponse201.

        Total number of items in the collection  # noqa: E501

        :param total: The total of this InlineResponse201.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def results(self):
        """Gets the results of this InlineResponse201.  # noqa: E501


        :return: The results of this InlineResponse201.  # noqa: E501
        :rtype: list[object]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this InlineResponse201.


        :param results: The results of this InlineResponse201.  # noqa: E501
        :type: list[object]
        """

        self._results = results

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse201):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
