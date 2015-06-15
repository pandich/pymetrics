import util
import numpy
from metric import MetricError
from statistical_metric import StatisticalMetric

class TimerAlreadyStoppedError(MetricError):
    def __init__(self, name):
        Exception.__init__(self,
                           '{name:s} timer context is already stopped'.format(
                               name=name,
                           ))
        return

class Timer(StatisticalMetric):

    context_data_type = numpy.dtype([
        ('time', float),
        ('duration', float),
    ])

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
        StatisticalMetric.__init__(
            self,
            name,
            numpy.array([], Timer.context_data_type),
        )
        return

    def submit(self, context):
        self.inc()
        self._series = numpy.append(
            self._series,
            numpy.array([
                    (
                        numpy.float_(context.time),
                        numpy.float_(context.duration)
                    )
            ],
                dtype=Timer.context_data_type
            ),
        )
        return

    def time(self):
        self.inc()
        return Timer.Context(self)

    def values(self):
        return self.series['duration']

    def values_by_time(self, threshold):
        filtered = numpy.where(self.series['time'] >= threshold)
        return self.series[filtered]['duration']
