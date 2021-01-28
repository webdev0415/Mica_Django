import os

from django.core.exceptions import ImproperlyConfigured
from django.template.base import TemplateSyntaxError


def get_env_variable(var_name, default=None):
    """
    return environment variable otherwise throws
    `django.core.exceptions.ImproperlyConfigured` error
    """
    value = os.getenv(var_name, default)

    if value:
        return value

    error_msg = "Set the %s environment variable" % var_name
    raise ImproperlyConfigured(error_msg)


class InvalidTemplateVariable(str):
    def __mod__(self, other):
        raise TemplateSyntaxError("Invalid variable : '%s'" % other)
