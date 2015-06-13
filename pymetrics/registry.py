import util
from metric import *
from frozendict import frozendict

_registries = dict()


class Registry:
    _id = 0

    def __init__(self, name = None):
        self._metrics = {}
        self._id = self._id
        self._id += 1
        self._name = util.coalesce(name,
                                   'registry-{id:02d}'.format(id=self._id))
        return

    @property
    def name(self):
        return self._name;

    def register(self, metric):
        if not metric:
            raise MetricValueError('metric', metric)

        if not util.issubclass_recursive(metric, Metric):
            raise MetricTypeError(metric)

        self._metrics[metric.name] = metric

    @property
    def metrics(self):
        return frozendict(self._metrics)

    def __str__(self):
        output = '[\n'

        for name in sorted(self._metrics):
            metric = self._metrics[name]
            output += '\t' + str(metric) + '\n'

        output += ']'
        return output

    def size(self):
        return len(self._metrics)

    def __hash__(self):
        return self._id

default = Registry('default')
_registries[default.name] = default

def registry(name=None):
    if name in _registries:
        return _registries.get(name)

    _registries[name] = Registry(name)
    return _registries[name]
