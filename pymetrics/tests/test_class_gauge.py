import unittest
from pymetrics.class_gauge import ClassGauge

class SomeClass:
    def __init__(self):
        self._name = 'example'

    def name(self):
        return self._name


class TestClassGauge(unittest.TestCase):
    def test_get_value(self):
        a = SomeClass()
        gauge = ClassGauge('class_name', a, 'name')
        self.assertEqual('example', gauge.value())


###

if __name__ == '__main__':
    unittest.main()
