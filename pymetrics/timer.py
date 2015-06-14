import util
import numpy
from metric import MetricError
from counter import Counter
from duration import Duration
from timeunit import *

class TimerAlreadyStoppedError(MetricError):
    def __init__(self, name):
        Exception.__init__(self,
                           '{name:s} timer context is already stopped'.format(
                               name=name,
                           ))
        return

class Timer(Counter):

    context_data_type = numpy.dtype([
        ('start', float),
        ('duration', float),
    ])

    class Context:
        def __init__(self, timer):
            self._timer = timer
            self._start = util.now()
            self._stop = None
            self._duration = None
            return

        def stop(self):
            if self._stop:
                raise TimerAlreadyStoppedError(self._timer.name)
            self._stop = util.now()
            self._duration = self._stop - self._start
            self._timer.submit(self)
            return

        @property
        def start(self):
            return self._start

        @property
        def stop(self):
            return self._stop

        @property
        def duration(self):
            return self._duration

        @property
        def is_stopped(self):
            return self._stop is not None

    def __init__(self, name):
        Counter.__init__(self, name)
        self._series = numpy.recarray([], Timer.context_data_type)
        return

    def submit(self, context):
        self.inc()
        self._series = numpy.append(self._series, context)
        return

    def time(self):
        self.inc()
        return Timer.Context(self)

    def mean(self, window=None):
        if window:
            if not util.issubclass_recursive(window, Duration):
                raise TypeError('window must be a duration')

            window_start = numpy.searchsorted(
                self._series.field('start'),
                util.now() - window.nanoseconds, side='right'
            )

            filtered = self._series.field('duration')[window_start, -1]
            return filtered.mean()
        else:
            return numpy.mean(self._series)

    def median(self):
        return numpy.median(self._series.field('duration'))

    def dump(self):
        now = util.now()
        return {
            'mean': {
                'all': self.mean(),
                '1 minute': self.mean(Duration(minute, 1)),
                '5 minutes': self.mean(Duration(minute, 5)),
                '15 minutes': self.mean(Duration(minute, 15)),
            },
            'median': self.median(),
        }
