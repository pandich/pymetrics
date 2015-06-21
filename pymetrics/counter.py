import util
import logging
from metric import Metric, metric_decorated


class Counter(Metric):

    logger = logging.getLogger(__name__)

    def __init__(self, name):
        Metric.__init__(self, name)
        self._count = 0
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

    def __enter__(self):
        self.inc()
        return

def counted(target=None, **options):
    def before(record):
        record.counter.inc()
        return

    return metric_decorated(
        target,
        Counter,
        counted,
        before=before,
        **options
    )
