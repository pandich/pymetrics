from metric import Metric, metric_decorator_name, metric_decorator_registry


class Gauge(Metric):
    def __init__(self, name, fn):
        Metric.__init__(self, name)
        self._fn = fn
        return

    @property
    def value(self):
        return self._fn()

    def dump(self):
        return {
            self.name: self.value
        }

def gauged(
        target,
        **options
):
    if not target:
        def inner(inner_target):
            return gauged(inner_target, **options)

        return inner

    target_registry = metric_decorator_registry(**options)
    metric_name = metric_decorator_name(Gauge, target, **options)
    target_registry.register(Gauge(metric_name, target))

    return target
