import six

from ..utils.is_base_type import is_base_type
from .abstracttype import AbstractTypeMeta
from .options import Options
from .utils import (get_fields_in_type, merge_fields_in_attrs,
                    yank_fields_from_attrs)


class InterfaceMeta(AbstractTypeMeta):

    def __new__(cls, name, bases, attrs):
        # Also ensure initialization is only performed for subclasses of
        # Interface
        if not is_base_type(bases, InterfaceMeta):
            return type.__new__(cls, name, bases, attrs)

        options = Options(
            attrs.pop('Meta', None),
            name=name,
            description=attrs.get('__doc__'),
            fields=None,
        )

        attrs = merge_fields_in_attrs(bases, attrs)
        if not options.fields:
            options.fields = get_fields_in_type(Interface, attrs)
            yank_fields_from_attrs(attrs, options.fields)

        return type.__new__(cls, name, bases, dict(attrs, _meta=options))

    def __str__(cls):  # noqa: N802
        return cls._meta.name


class Interface(six.with_metaclass(InterfaceMeta)):
    resolve_type = None

    def __init__(self, *args, **kwargs):
        raise Exception("An Interface cannot be intitialized")

    @classmethod
    def implements(cls, objecttype):
        pass
