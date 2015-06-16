from metric import Metric


class Gauge(Metric):
    def __init__(self, name, method):
        Metric.__init__(self, name)
        self._method_name = method
        return

    def value(self):
        raise NotImplementedError

    def dump(self):
        return {
            self.name: self.value()
        }
