import util
from metric import MetricError
from histogram import Histogram

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
            self.time = util.now()
            self.duration = None
            self.stopped = False
            return

        def stop(self):
            if self.stopped:
                raise TimerAlreadyStoppedError(self._timer.name)
            self.stopped = True
            self.duration = util.now() - self.time
            self._timer.submit(self)
            return

    def __init__(self, name):
        Histogram.__init__(
            self,
            name,
        )
        return

    def submit(self, context):
        self.update(event_time=context.time, value=context.duration)
        return

    def time(self):
        self.inc()
        return Timer.Context(self)
