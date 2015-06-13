import unittest
from pymetrics.meter import Meter



#
# COUNTER
#

class TestMeter(unittest.TestCase):
    def test_name_and_metric(self):
        metric = Meter('example')
        self.assertEqual('meter', metric.metric)
        self.assertEqual('example', metric.name)

    def test_mark(self):
        meter = Meter('example')
        meter.mark()


###

if __name__ == '__main__':
    unittest.main()
