import util
import logging
from metric import Metric


class Counter(Metric):

    logger = logging.getLogger(__name__)

    def __init__(self, name, initial_count=0):
        Metric.__init__(self, name)
        self._count = util.coalesce(initial_count, 0)
        return

    @property
    def count(self):
        return self._count

    def inc(self, amount=1):
        self._count += util.coalesce(amount, 0)
        return

    def dec(self, amount=1):
        self.inc(-util.coalesce(amount, 0))
        return

    def dump(self):
        return {
            'count': self.count,
        }
