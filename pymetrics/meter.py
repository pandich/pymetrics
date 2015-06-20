import numpy as np
from histogram import Histogram
from metric import metric_decorator_registry, metric_decorator_name, metric_decorated
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
    def before(meter):
        meter.mark()
        return

    return metric_decorated(
        cls=Meter,
        handler=metered,
        before=before,
        target=target,
        **options
    )
