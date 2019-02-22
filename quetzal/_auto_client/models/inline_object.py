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


class InlineObject(object):
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
        'status': 'str',
        'creation_date': 'datetime',
        'owner': 'str',
        'data_url': 'str',
        'name': 'str',
        'description': 'str',
        'families': 'object',
        'temporary': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'creation_date': 'creation_date',
        'owner': 'owner',
        'data_url': 'data_url',
        'name': 'name',
        'description': 'description',
        'families': 'families',
        'temporary': 'temporary'
    }

    def __init__(self, id=None, status=None, creation_date=None, owner=None, data_url=None, name=None, description=None, families=None, temporary=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._status = None
        self._creation_date = None
        self._owner = None
        self._data_url = None
        self._name = None
        self._description = None
        self._families = None
        self._temporary = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if creation_date is not None:
            self.creation_date = creation_date
        if owner is not None:
            self.owner = owner
        self.data_url = data_url
        self.name = name
        self.description = description
        self.families = families
        if temporary is not None:
            self.temporary = temporary

    @property
    def id(self):
        """Gets the id of this InlineObject.  # noqa: E501

        Workspace ID  # noqa: E501

        :return: The id of this InlineObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineObject.

        Workspace ID  # noqa: E501

        :param id: The id of this InlineObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this InlineObject.  # noqa: E501

        Workspace status  # noqa: E501

        :return: The status of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineObject.

        Workspace status  # noqa: E501

        :param status: The status of this InlineObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["INITIALIZING", "READY", "SCANNING", "UPDATING", "COMMITTING", "DELETING", "INVALID", "CONFLICT", "DELETED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def creation_date(self):
        """Gets the creation_date of this InlineObject.  # noqa: E501

        Date when the workspace was created  # noqa: E501

        :return: The creation_date of this InlineObject.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this InlineObject.

        Date when the workspace was created  # noqa: E501

        :param creation_date: The creation_date of this InlineObject.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def owner(self):
        """Gets the owner of this InlineObject.  # noqa: E501

        User who owns this workpace  # noqa: E501

        :return: The owner of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this InlineObject.

        User who owns this workpace  # noqa: E501

        :param owner: The owner of this InlineObject.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def data_url(self):
        """Gets the data_url of this InlineObject.  # noqa: E501

        URL of a remote storage location for files used in this workspace  # noqa: E501

        :return: The data_url of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._data_url

    @data_url.setter
    def data_url(self, data_url):
        """Sets the data_url of this InlineObject.

        URL of a remote storage location for files used in this workspace  # noqa: E501

        :param data_url: The data_url of this InlineObject.  # noqa: E501
        :type: str
        """

        self._data_url = data_url

    @property
    def name(self):
        """Gets the name of this InlineObject.  # noqa: E501

        Name of the workspace  # noqa: E501

        :return: The name of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject.

        Name of the workspace  # noqa: E501

        :param name: The name of this InlineObject.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this InlineObject.  # noqa: E501

        Descriptive text of the purpose of this workspace  # noqa: E501

        :return: The description of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject.

        Descriptive text of the purpose of this workspace  # noqa: E501

        :param description: The description of this InlineObject.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def families(self):
        """Gets the families of this InlineObject.  # noqa: E501

        Families and corresponding versions used in this workspace. This property is a object whose keys are family names and values are integers.  # noqa: E501

        :return: The families of this InlineObject.  # noqa: E501
        :rtype: object
        """
        return self._families

    @families.setter
    def families(self, families):
        """Sets the families of this InlineObject.

        Families and corresponding versions used in this workspace. This property is a object whose keys are family names and values are integers.  # noqa: E501

        :param families: The families of this InlineObject.  # noqa: E501
        :type: object
        """
        if families is None:
            raise ValueError("Invalid value for `families`, must not be `None`")  # noqa: E501

        self._families = families

    @property
    def temporary(self):
        """Gets the temporary of this InlineObject.  # noqa: E501

        Whether this workspace is temporary or not. Temporary workspaces are automatically deleted after some time.  # noqa: E501

        :return: The temporary of this InlineObject.  # noqa: E501
        :rtype: bool
        """
        return self._temporary

    @temporary.setter
    def temporary(self, temporary):
        """Sets the temporary of this InlineObject.

        Whether this workspace is temporary or not. Temporary workspaces are automatically deleted after some time.  # noqa: E501

        :param temporary: The temporary of this InlineObject.  # noqa: E501
        :type: bool
        """

        self._temporary = temporary

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
        if not isinstance(other, InlineObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
