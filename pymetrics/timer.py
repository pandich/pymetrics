from metric import MetricError, metric_decorated
from histogram import Histogram
from pymetrics.unit.timeunit import now


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

        def __enter__(self):
            return

        # noinspection PyUnusedLocal
        def __exit__(self, *unused):
            self.stop()
            return

    def __init__(self, name):
        Histogram.__init__(self, name)
        return

    def submit(self, context):
        self.update(event_time=context.time, value=context.duration)
        return

    def time(self):
        self.inc()
        return Timer.Context(self)


def timed(target=None, **options):
    def before(record):
        return record.timer.time()

    def after(record):
        record.before.stop()
        return

    return metric_decorated(
        target,
        Timer,
        timed,
        before=before,
        after=after,
        **options
    )
