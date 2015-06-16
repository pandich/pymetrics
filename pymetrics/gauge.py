from metric import Metric


class Gauge(Metric):
    def __init__(self, name, fn):
        Metric.__init__(self, name)
        self._fn = fn
        return

    def value(self):
        return self._fn()

    def dump(self):
        return {
            self.name: self.value()
        }
