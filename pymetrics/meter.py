import util
import numpy
from statistical_metric import StatisticalMetric

class Meter(StatisticalMetric):
    def __init__(self, name):
        StatisticalMetric.__init__(self, name, numpy.array([]))
        return

    def mark(self):
        self.inc()
        self._series = numpy.append(self._series, util.now())
        return
