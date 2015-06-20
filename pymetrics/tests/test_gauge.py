import unittest
from pymetrics.registry import registry
from pymetrics.gauge import Gauge, gauged

class SomeClass:
    def __init__(self):
        self.name = 'example'

@gauged
def some_method():
    return 'hello'


class TestGauge(unittest.TestCase):
    def test_decorator(self):
        gauge = registry.get('gauge.some_method')
        self.assertIsNotNone(gauge)
        self.assertEqual(gauge.value, 'hello')
        return

    def test_get_value(self):
        a = SomeClass()

        def name():
            return a.name

        gauge = Gauge('class_name', name)
        self.assertEqual('example', gauge.value)

        a.name = 'bob'
        self.assertEqual('bob', gauge.value)


###

if __name__ == '__main__':
    unittest.main()
