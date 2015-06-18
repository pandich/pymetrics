import unittest
from pymetrics.gauge import Gauge

class SomeClass:
    def __init__(self):
        self.name = 'example'


class TestGauge(unittest.TestCase):
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
