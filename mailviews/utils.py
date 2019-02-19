import textwrap
from collections import namedtuple

import django
from distutils.version import StrictVersion


Docstring = namedtuple('Docstring', ('summary', 'body'))


def split_docstring(value):
    """
    Splits the docstring of the given value into it's summary and body.

    :returns: a 2-tuple of the format ``(summary, body)``
    """
    docstring = textwrap.dedent(getattr(value, '__doc__', ''))
    if not docstring:
        return None

    pieces = docstring.strip().split('\n\n', 1)
    try:
        body = pieces[1]
    except IndexError:
        body = None

    return Docstring(pieces[0], body)


def unimplemented(*args, **kwargs):
    raise NotImplementedError


def is_django_version_greater(version):
    return StrictVersion(django.get_version()) > StrictVersion(version)


def is_django_version_greater_than_1_9():
    return is_django_version_greater('1.9')
