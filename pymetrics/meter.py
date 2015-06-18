import numpy as np
from statistical_metric import StatisticalMetric
from timeunit import now

class Meter(StatisticalMetric):
    def __init__(self, name):
        StatisticalMetric.__init__(self, name, np.array([]))
        return

    def mark(self):
        self.inc()
        self._series = np.append(self._series, now())
        return
