import numpy as np
from metric import metric_decorated
from statistical_metric import StatisticalMetric
from timeunit import now


time_key = 'time'
value_key = 'value'


class Histogram(StatisticalMetric):

    time_series_dtype = np.dtype([
        (time_key, float),
        (value_key, float),
    ])

    def __init__(self, name, dtype=time_series_dtype):
        StatisticalMetric.__init__(self, name, dtype)
        return

    def update(self, event_time=None, value=None):
        self.append((event_time or now(), value or 1))
        return

    def values(self):
        return self._series[value_key]

    def values_by_time(self, threshold):
        filtered = np.where(self._series[time_key] >= threshold)
        return self._series[filtered][value_key]

    def __exit__(self, value_type, value, traceback):
        self.update(value)
        return


def histogrammed(target=None, **options):
    def after(record):
        record.histogram.update(record.result)
        return

    return metric_decorated(
        target,
        Histogram,
        histogrammed,
        after=after,
        **options
    )
