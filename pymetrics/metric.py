import registry
from util import coalesce

class MetricError(Exception):
    def __init__(self):
        return


class MetricTypeError(TypeError, MetricError):
    def __init__(self, o):
        Exception.__init__(self,
                           'class {class_name:s} is not a supported metric '
                           'type'.format(
                               class_name=o.__class__.__name__
                           ))
        return


class MetricValueError(ValueError, MetricError):
    def __init__(self, name, value):
        Exception.__init__(self,
                           '{name:s} has an invalid value: {value:s}'.format(
                               name=name,
                               value=value,
                           ))
        return


class Metric(object):
    def __init__(self, name):
        self._name = name
        self._metric = self.__class__.__name__.lower()
        return

    @property
    def name(self):
        return self._name

    @property
    def metric(self):
        return self._metric

    def dump(self):
        raise NotImplementedError

    def __str__(self):
        return '{metric:s}: name:"{value:s}"'.format(
            metric = self._metric,
            value = self.name,
        )

def metric_decorator_name(metric, target, **options):
    name = coalesce(options.get('metric_name'), target.__name__)
    prefix = coalesce(options.get('metric_prefix'), metric.__name__.lower())
    return registry.name(prefix, name)

def metric_decorator_registry(**options):
    return getattr(options, 'registry', registry.registry)
