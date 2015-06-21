import unittest
from pymetrics.meter import Meter, metered
from pymetrics.registry import registry, name

@metered
def example():
    return

class TestMeter(unittest.TestCase):
    def test_name_and_metric(self):
        metric = Meter('example')
        self.assertEqual('meter', metric.metric)
        self.assertEqual('example', metric.name)

    def test_mark(self):
        meter = Meter('example')
        meter.mark()

    def test_metered_decorator(self):
        meter = registry.get('meter.example')
        self.assertEqual(meter.count, 0)
        example()
        self.assertEqual(meter.count, 1)
        example()
        self.assertEqual(meter.count, 2)

    def test_with(self):
        meter = Meter(name('example'))
        self.assertEquals(meter.count, 0)
        with meter:
            pass
        self.assertEquals(meter.count, 1)

###

if __name__ == '__main__':
    unittest.main()
