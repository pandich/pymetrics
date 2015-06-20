import numpy as np
from statistical_metric import StatisticalMetric
from timeunit import now

time_key = 'time'
value_key = 'value'

class Histogram(StatisticalMetric):

    record_type = np.dtype([
        (time_key, float),
        (value_key, float),
    ])

    def __init__(self, name, dtype=record_type):
        StatisticalMetric.__init__(self, name, series=np.array([], dtype=dtype))
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
            ], dtype=self._series.dtype)
        )
        return

    def values(self):
        return self._series[value_key]

    def values_by_time(self, threshold):
        filtered = np.where(self._series[time_key] >= threshold)
        return self._series[filtered][value_key]
