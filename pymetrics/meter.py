import numpy as np
from histogram import Histogram
from metric import metric_decorator_registry, metric_decorator_name
from statistical_metric import StatisticalMetric
from timeunit import now

class Meter(StatisticalMetric):
    def __init__(self, name):
        StatisticalMetric.__init__(
            self,
            name,
            np.array([], Histogram.record_type)
        )
        return

    def mark(self):
        self.inc()
        self._series = np.append(self._series, now())
        return


def metered(target=None, **options):
    if not target:
        def inner(inner_target):
            return metered(inner_target, **options)

        return inner

    target_registry = metric_decorator_registry(**options)
    metric_name = metric_decorator_name(Meter, target, **options)
    meter = target_registry.register(Meter(metric_name))

    def decorator(func):
        names = getattr(func, '_names', None)

        def decorated(*args, **kwargs):
            meter.mark()
            return func(*args, **kwargs)

        decorated._names = names
        return decorated

    return decorator
