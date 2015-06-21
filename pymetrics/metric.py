import registry
from util import coalesce


def metric_decorator_name(metric, target, **options):
    name = coalesce(options.get('metric_name'), target.__name__)
    prefix = coalesce(options.get('metric_prefix'), metric.__name__.lower())
    return registry.name(prefix, name)


def metric_decorator_registry(**options):
    return getattr(options, 'registry', registry.registry)


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

    def __enter__(self):
        return

    def __exit__(self, value_type, value, traceback):
        return

    def __str__(self):
        return '{metric:s}: name:"{value:s}"'.format(
            metric=self._metric,
            value=self.name,
        )


class BeforeDecoratorRecord(object):
    def __init__(self, metric):
        self._metric = metric
        return

    @property
    def metric(self):
        return self._metric

    @property
    def counter(self):
        return self._metric

    @property
    def gauge(self):
        return self._metric

    @property
    def health_check(self):
        return self._metric

    @property
    def histogram(self):
        return self._metric

    @property
    def meter(self):
        return self._metric

    @property
    def timer(self):
        return self._metric


class AfterDecoratedRecord(object):
    def __init__(self, metric, before, result, exception):
        self._metric = metric
        self._before = before
        self._result = result
        self._exception = exception

    @property
    def metric(self):
        return self._metric

    @property
    def counter(self):
        return self._metric

    @property
    def gauge(self):
        return self._metric

    @property
    def health_check(self):
        return self._metric

    @property
    def histogram(self):
        return self._metric

    @property
    def meter(self):
        return self._metric

    @property
    def timer(self):
        return self._metric

    @property
    def before(self):
        return self._before

    @property
    def result(self):
        return self._result

    @property
    def exception(self):
        return self._exception


# TODO handle metric-specific arguments
def metric_decorated(
        target,
        cls,
        handler,
        before=None,
        after=None,
        **options
):
    if not target:
        def inner(inner_target):
            return handler(inner_target, **options)
        return inner

    target_registry = metric_decorator_registry(**options)
    metric_name = metric_decorator_name(cls, target, **options)
    metric = target_registry.register(cls(metric_name))

    def decorated(*args, **kwargs):
        before_result = before(
            BeforeDecoratorRecord(metric)
        ) if before else None
        exception = None
        function_result = None
        try:
            function_result = target(*args, **kwargs)
        except BaseException as e:
            exception = e
        finally:
            if after:
                after(AfterDecoratedRecord(
                    metric,
                    before_result,
                    function_result,
                    exception
                ))

        if exception:
            raise exception

        return function_result

    decorated._names = getattr(target, '_names', None)
    return decorated
