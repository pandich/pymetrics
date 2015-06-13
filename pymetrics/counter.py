import util
from metric import Metric


class Counter(Metric):
    def __init__(self, name, initial_count=0):
        Metric.__init__(self, name)
        self.data['count'] = util.coalesce(initial_count, 0)

    @property
    def count(self):
        return self.data['count']

    def inc(self, amount=1):
        self.data['count'] += util.coalesce(amount, 0)
        return

    def dec(self, amount=1):
        self.inc(-util.coalesce(amount, 0))
        return

    def dump(self):
        return {
            'count': self.count,
        }
