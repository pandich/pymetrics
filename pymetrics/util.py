import time
import types
import collections
import numpy
from timeunit import *


class DynamicRecArray(object):
    def __init__(self, dtype):
        self.dtype = numpy.dtype(dtype)
        self.length = 0
        self.size = 10
        self._data = numpy.empty(self.size, dtype=self.dtype)

    def __len__(self):
        return self.length

    def append(self, rec):
        if self.length == self.size:
            self.size = int(1.5 * self.size)
            self._data = numpy.resize(self._data, self.size)
        self._data[self.length] = rec
        self.length += 1

    def extend(self, recs):
        for rec in recs:
            self.append(rec)

    @property
    def data(self):
        return self._data[:self.length]


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
    return nanoseconds.from_unit(microseconds, time.time())

def flatten(d, parent_key='', sep=','):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
