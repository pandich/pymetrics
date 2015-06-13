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

