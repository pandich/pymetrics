import numpy as np
from metric import MetricError, metric_decorator_name, metric_decorator_registry
from histogram import Histogram
from timeunit import now


class TimerAlreadyStoppedError(MetricError):
    def __init__(self, name):
        Exception.__init__(self,
                           '{name:s} timer context is already stopped'.format(
                               name=name,
                           ))
        return

class Timer(Histogram):

    class Context:
        def __init__(self, timer):
            self._timer = timer
            self.time = now()
            self.duration = None
            self.stopped = False
            return

        def stop(self):
            if self.stopped:
                raise TimerAlreadyStoppedError(self._timer.name)
            self.stopped = True
            self.duration = now() - self.time
            self._timer.submit(self)
            return

    def __init__(self, name):
        Histogram.__init__(
            self,
            name,
            np.array([], dtype=Histogram.record_type)
        )
        return

    def submit(self, context):
        self.update(event_time=context.time, value=context.duration)
        return

    def time(self):
        self.inc()
        return Timer.Context(self)

def timed(target=None, **options):
    if not target:
        def inner(inner_target):
            return timed(inner_target, **options)
        return inner

    target_registry = metric_decorator_registry(**options)
    metric_name = metric_decorator_name(Timer, target, **options)
    timer = target_registry.register(Timer(metric_name))

    def decorator(func):
        names = getattr(func, '_names', None)

        def decorated(*args, **kwargs):
            context = timer.time()
            try:
                return func(*args, **kwargs)
            finally:
                context.stop()

        decorated._names = names
        return decorated

    return decorator
