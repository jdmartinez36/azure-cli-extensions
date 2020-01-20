# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class DebugSendResponse(Resource):
    """Description of a NotificationHub Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param sku: The sku of the created namespace
    :type sku: ~azure.mgmt.notificationhubs.models.Sku
    :param success: successful send
    :type success: float
    :param failure: send failure
    :type failure: float
    :param results: actual failure description
    :type results: object
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'success': {'key': 'properties.success', 'type': 'float'},
        'failure': {'key': 'properties.failure', 'type': 'float'},
        'results': {'key': 'properties.results', 'type': 'object'},
    }

    def __init__(self, *, location: str=None, tags=None, sku=None, success: float=None, failure: float=None, results=None, **kwargs) -> None:
        super(DebugSendResponse, self).__init__(location=location, tags=tags, sku=sku, **kwargs)
        self.success = success
        self.failure = failure
        self.results = results