import numpy as np
from statistical_metric import StatisticalMetric
from timeunit import now

value_key = 'value'
time_key = 'time'

class Histogram(StatisticalMetric):

    record_type = np.dtype([
        (time_key, float),
        (value_key, float),
    ])

    def __init__(self, name):
        StatisticalMetric.__init__(
            self,
            name,
            np.array([], Histogram.record_type),
        )
        return

    def update(self, event_time=now(), value=None):
        if value is None:
            return

        self.inc()
        self._series = np.append(
            self._series,
            np.array([
                (
                    event_time,
                    value,
                ),
            ], dtype=Histogram.record_type)
        )
        return

    def values(self):
        return self.series[value_key]

    def values_by_time(self, threshold):
        filtered = np.where(self.series[time_key] >= threshold)
        return self.series[filtered][value_key]
