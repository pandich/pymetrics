import numpy as np
from counter import Counter
from duration import Duration
from timeunit import now


class StatisticalMetric(Counter):
    def __init__(self, name, series):
        Counter.__init__(self, name)
        self._series = series
        return

    @property
    def series(self):
        return self._series

    def mean(self, window=None):
        if not self._series.size:
            return 0

        threshold = now() - window.nanoseconds if window else 0

        return self.values_by_time(threshold).mean()

    def values(self):
        return self._series

    def values_by_time(self, threshold):
        return np.where(self._series >= threshold)

    def median(self):
        if not self._series.size:
            return 0

        return np.median(self.values())

    def percentile(self, q):
        if not self._series.size:
            return 0

        return np.percentile(self.values(), q)

    def dump(self):
        return {
            'mean': {
                'all': self.mean(),
                '1 minute': self.mean(Duration.from_minutes(1)),
                '5 minutes': self.mean(Duration.from_minutes(5)),
                '15 minutes': self.mean(Duration.from_minutes(15)),
            },
            'percentile': {
                '90%': self.percentile(0.9),
                '95%': self.percentile(0.95),
                '99%': self.percentile(0.99),
                '99.9%': self.percentile(0.999),
            },
            'median': self.median(),
        }
