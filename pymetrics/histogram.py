import util
import numpy
from statistical_metric import StatisticalMetric

class Histogram(StatisticalMetric):

    context_data_type = numpy.dtype([
        ('time', float),
        ('value', float),
    ])

    def __init__(self, name):
        StatisticalMetric.__init__(
            self,
            name,
            numpy.array([], Histogram.context_data_type),
        )
        return

    def update(self, event_time=util.now(), value=None):
        if value is None:
            return

        self.inc()
        self._series = numpy.append(
            self._series,
            numpy.array([
                (
                    event_time,
                    value,
                ),
            ], dtype=Histogram.context_data_type)
        )
        return

    def values(self):
        return self.series['value']

    def values_by_time(self, threshold):
        filtered = numpy.where(self.series['time'] >= threshold)
        return self.series[filtered]['value']
