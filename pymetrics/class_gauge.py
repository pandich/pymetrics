from gauge import Gauge


class ClassGauge(Gauge):
    def __init__(self, name, clazz, method_name):
        Gauge.__init__(self, name, method_name)
        self._clazz = clazz
        return

    def value(self):
        return getattr(self._clazz, self._method_name)()
