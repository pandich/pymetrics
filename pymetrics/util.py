import time
import types
import timeunit
import sys
import contextlib
import collections


def issubclass_recursive(child, parent):
    if not child or not parent:
        return False

    child_class = child if isinstance(child,
                                      types.ClassType) else child.__class__
    parent_class = parent if isinstance(parent,
                                        types.ClassType) else parent.__class__

    if issubclass(child_class, parent_class):
        return True

    for base in child_class.__bases__:
        if issubclass_recursive(base, parent):
            return True

    return False


def coalesce(*args):
    if args:
        for arg in args:
            if arg is not None:
                return arg

    return None


def now():
    timeunit.microsecond.to_unit(timeunit.nanosecond, time.time())


@contextlib.contextmanager
def smart_open(filename=None):
    if filename:
        fh = open(filename, 'w')
    else:
        fh = sys.stdout

    try:
        yield fh
    finally:
        if fh is not sys.stdout:
            fh.close()

def flatten(d, parent_key='', sep=','):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
