from gauge import Gauge


class ModuleGauge(Gauge):
    def __init__(self, name, module, method_name):
        Gauge.__init__(self, name, method_name)
        self._module = module
        return

    def value(self):
        print self._module
        print self._method_name
        attr = getattr(self._module, self._method_name)
        print attr
        return attr()
