import numpy
from duration import Duration
from counter import Counter
from timeunit import *

class Meter(Counter):
    def __init__(self, name):
        Counter.__init__(self, name)
        self._series = numpy.array([])
        return

    def mark(self):
        self.inc()
        self._series = numpy.append(self._series, util.now())
        return

    def mean(self, window=None):
        if window:
            if not util.issubclass_recursive(window, Duration):
                raise TypeError('window must be a duration')

            filtered = numpy.where(
                self._series > util.now - window.nanonseconds(),
                self._series,
            )
            return filtered.mean()
        else:
            return numpy.mean(self._series)

    def median(self):
        return numpy.median(self._series)

    def dump(self):
        return {
            'mean': {
                'all': self.mean(),
                '1 minute': self.mean(Duration(minute, 1)),
                '5 minutes': self.mean(Duration(minute, 5)),
                '15 minutes': self.mean(Duration(minute, 15)),
            },
            'median': self.median(),
        }
