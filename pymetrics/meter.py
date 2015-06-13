import numpy
import util
from duration import Duration
from counter import Counter
from timeunit import *

class Meter(Counter):
    def __init__(self, name):
        Counter.__init__(self, name)
        self.series = numpy.array([])

    def mark(self):
        self.inc()
        self.series = numpy.append(self.series, util.now())

    def mean(self, when=util.now(), window=None):
        if window:
            if not util.issubclass_recursive(window, Duration):
                raise TypeError('window must be a duration')

            filtered = numpy.where(
                self.series > when - window.nanonseconds(),
                self.series,
            )
            return filtered.mean()
        else:
            return numpy.mean(self.series)

    def median(self):
        return numpy.median(self.series)

    def dump(self):
        now = util.now()
        return {
            'mean': {
                'all': self.mean(when=now),
                '1': self.mean(when=now, window=Duration(minute, 1)),
                '5': self.mean(when=now, window=Duration(minute, 5)),
                '15': self.mean(when=now, window=Duration(minute, 15)),
            },
            'median': self.median(),
        }
