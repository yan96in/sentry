from __future__ import absolute_import

from rest_framework.exceptions import APIException, PermissionDenied


class ResourceDoesNotExist(APIException):
    status_code = 404


class InvalidRepository(Exception):
    pass


class NeedSuperuserUpgrade(PermissionDenied):
    default_detail = 'You need to re-authenticate for superuser.'
