import util
from metric import *

class Registry:
    def __init__(self):
        self.registry = {}
        return

    def register(self, metric):
        if not metric:
            raise MetricValueError('metric', metric)

        if not util.issubclass_recursive(metric, Metric):
            raise MetricTypeError(metric)

        self.registry[metric.name] = metric

    def __str__(self):
        output = '[\n'

        for name in sorted(self.registry):
            metric = self.registry[name]
            output += '\t' + str(metric) + '\n'

        output += ']'
        return output

    def size(self):
        return len(self.registry)
