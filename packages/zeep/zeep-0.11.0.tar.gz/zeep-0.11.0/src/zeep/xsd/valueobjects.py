from collections import OrderedDict

import six

from zeep.xsd.indicators import Indicator
from zeep.xsd.printer import PrettyPrinter

__all__ = ['AnyObject', 'CompoundValue']


class AnyObject(object):
    def __init__(self, xsd_type, value):
        self.xsd_type = xsd_type
        self.value = value

    def __repr__(self):
        return '<%s(type=%r, value=%r)>' % (
            self.__class__.__name__, self.xsd_type, self.value)


class CompoundValue(object):

    def __init__(self, *args, **kwargs):
        self.__ordered_dict__ = OrderedDict()

        # Set default values
        for container_name, container in self._xsd_type.elements_nested:
            values = container.default_value
            if isinstance(container, Indicator):
                self.__ordered_dict__.update(values)
            else:
                self.__ordered_dict__[container_name] = values

        for attribute_name, attribute in self._xsd_type.attributes:
            self.__ordered_dict__[attribute_name] = attribute.default_value

        items = _process_signature(self._xsd_type, args, kwargs)
        for key, value in items.items():
            self.__ordered_dict__[key] = value

    def __contains__(self, key):
        return self.__ordered_dict__.__contains__(key)

    def __iter__(self):
        return self.__ordered_dict__.__iter__()

    def __repr__(self):
        return PrettyPrinter().pformat(self.__ordered_dict__)

    def __getitem__(self, key):
        return self.__ordered_dict__[key]

    def __setitem__(self, key, value):
        self.__ordered_dict__[key] = value

    def __setattr__(self, key, value):
        if key.startswith('__'):
            return super(CompoundValue, self).__setattr__(key, value)
        self.__ordered_dict__[key] = value

    def __getattribute__(self, key):
        if key.startswith('__') or key in ('_xsd_type',):
            return super(CompoundValue, self).__getattribute__(key)
        try:
            return self.__ordered_dict__[key]
        except KeyError:
            raise AttributeError(
                "%s instance has no attribute '%s'" % (
                    self.__class__.__name__, key))


def _process_signature(xsd_type, args, kwargs):
    """Return a dict with the args/kwargs mapped to the field name.

    Special handling is done for Choice elements since we need to record which
    element the user intends to use.

    :param fields: List of tuples (name, element)
    :type fields: list
    :param args: arg tuples
    :type args: tuple
    :param kwargs: kwargs
    :type kwargs: dict


    """
    result = OrderedDict()
    args = list(args)
    num_args = len(args)

    # Process the positional arguments
    for element_name, element in xsd_type.elements_nested:
        values, args = element.parse_args(args)
        if not values:
            break
        result.update(values)

    if args:
        for attribute in xsd_type.attributes:
            result[attribute.name] = args.pop(0)

    if args:
        raise TypeError(
            "__init__() takes at most %s positional arguments (%s given)" % (
                len(result), num_args))

    # Process the named arguments (sequence/group/all/choice)
    for element_name, element in xsd_type.elements_nested:
        if element.accepts_multiple:
            values, kwargs = element.parse_kwargs(kwargs, element_name)
        else:
            values, kwargs = element.parse_kwargs(kwargs, None)
        if values is not None:
            for key, value in values.items():
                if key not in result:
                    result[key] = value
    # Process the named arguments for attributes
    for attribute_name, attribute in xsd_type.attributes:
        if attribute_name in kwargs:
            result[attribute_name] = kwargs.pop(attribute_name)

    if kwargs:
        raise TypeError(
            (
                "__init__() got an unexpected keyword argument %r. " +
                "Signature: (%s)"
            ) % (
                next(six.iterkeys(kwargs)), xsd_type.signature()
            ))
    return result
