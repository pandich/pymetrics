import unittest
from pymetrics.meter import Meter, metered
from pymetrics.registry import registry



@metered
def example():
    return

#
# COUNTER
#

METER_EXAMPLE = 'meter.example'
class TestMeter(unittest.TestCase):
    def test_name_and_metric(self):
        metric = Meter('example')
        self.assertEqual('meter', metric.metric)
        self.assertEqual('example', metric.name)

    def test_mark(self):
        meter = Meter('example')
        meter.mark()

    def test_metered_decorator(self):
        meter = registry.get(METER_EXAMPLE)
        self.assertEqual(meter.count, 0)
        example()
        self.assertEqual(meter.count, 1)
        example()
        self.assertEqual(meter.count, 2)

###

if __name__ == '__main__':
    unittest.main()
