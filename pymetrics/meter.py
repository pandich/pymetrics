import numpy as np
from histogram import Histogram
from metric import metric_decorated
from statistical_metric import StatisticalMetric
from timeunit import now

class Meter(Histogram):
    def __init__(self, name):
        StatisticalMetric.__init__(
            self,
            name,
            np.array([])
        )
        return

    def mark(self):
        self.inc()
        self._series = np.append(self._series, now())
        return


def metered(target=None, **options):
    def before(record):
        record.meter.mark()
        return

    return metric_decorated(
        target,
        Meter,
        metered,
        before=before,
        **options
    )
