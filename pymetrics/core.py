from util import issubclass_recursive
from util import coalesce


class MetricError(Exception):
    def __init__(self):
        return


class MetricTypeError(TypeError, MetricError):
    def __init__(self, o):
        Exception.__init__(self,
                           'class {class_name:s} is not a supported metric '
                           'type'.format(
                               class_name=o.__class__.__name__
                           ))
        return


class MetricValueError(ValueError, MetricError):
    def __init__(self, name, value):
        Exception.__init__(self,
                           '{name:s} has an invalid value: {value:s}'.format(
                               name=name,
                               value=value,
                           ))
        return


class Metric:
    def __init__(self, name):
        self.data = {
            'metric': self.__class__.__name__.lower(),
            'name': name,
        }
        return

    @property
    def name(self):
        return self.data['name']

    @property
    def metric(self):
        return self.data['metric']

    def snapshot(self):
        return {k: v for k, v in self.data.items()}

    def __str__(self):
        output = 'Metric: [name:"{value:s}"]'.format(
            value=self.data['name']
        )

        for name in sorted(self.data):
            if name is not 'name':
                output += ', [{name:s}:"{value:s}"]'.format(
                    name=name,
                    value=str(self.data[name]),
                )

        return output


class Registry:
    def __init__(self):
        self.registry = {}
        return

    def register(self, metric):
        if not metric:
            raise MetricValueError('metric', metric)

        if not issubclass_recursive(metric, Metric):
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


class Counter(Metric):
    def __init__(self, name, initial_count=0):
        Metric.__init__(self, name)
        self.data['count'] = coalesce(initial_count, 0)

    @property
    def count(self):
        return self.data['count']

    def inc(self, amount=1):
        self.data['count'] += coalesce(amount, 0)
        return

    def dec(self, amount=1):
        self.inc(-coalesce(amount, 0))
        return


class Meter(Counter):
    def __init__(self, name, initial_count=0):
        Counter.__init__(self, name)
        self.data['rate'] = initial_count

    def mark(self):
        self.inc()
        return
