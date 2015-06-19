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


# TODO handle metric-specific arguments
def metric_decorated(
        cls=None,
        handler=None,
        before=None,
        after=None,
        target=None,
        **options
):
    if not target:
        def inner(inner_target):
            return handler(inner_target, **options)
        return inner

    target_registry = metric_decorator_registry(**options)
    metric_name = metric_decorator_name(cls, target, **options)
    metric = target_registry.register(cls(metric_name))

    def decorator(func):
        def decorated(*args, **kwargs):
            print '----------------------------------'
            before_result = before(metric) if before else None
            exception = None
            function_result = None
            try:
                function_result = func(*args, **kwargs)
            except BaseException as e:
                exception = e
            finally:
                if after:
                    after(metric, before_result, function_result, exception)
            if exception:
                raise exception

            return function_result

        decorated._names = getattr(func, '_names', None)
        return decorated

    return decorator
