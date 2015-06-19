import util
from metric import *
from frozendict import frozendict
from string import join

class Registry(object):
    _id = 0
    _registries = dict()

    @staticmethod
    def registry(registry_name='default'):
        registries = Registry._registries
        if name in registries:
            return registry.get(registry_name)

        registries[registry_name] = Registry(registry_name)
        return registries[registry_name]

    def __init__(self, registry_name=None):
        self._metrics = {}
        self._id = self._id
        self._id += 1
        self._name = util.coalesce(registry_name,
                                   'registry-{id:02d}'.format(id=self._id))
        return

    @property
    def name(self):
        return self._name

    def register(self, metric):
        if not metric:
            raise MetricValueError('metric', metric)

        self._metrics[metric.name] = metric
        return metric

    @property
    def metrics(self):
        return frozendict(self._metrics)

    def __str__(self):
        output = '[\n'

        for metric_name in sorted(self._metrics):
            metric = self._metrics[metric_name]
            output += '\t' + str(metric) + '\n'

        output += ']'
        return output

    @property
    def count(self):
        return len(self._metrics)

    def __hash__(self):
        return self._id

def name(*args):
    names = [str(x) for x in args if x]
    if not names:
        raise ValueError('at least one name must be provided')

    return join(names, '.')

registry = Registry.registry('default')
