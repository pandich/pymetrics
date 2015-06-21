import unittest
from pymetrics.metric import Metric

class Nothing(Metric):
    def dump(self):
        pass

    def __init__(self):
        Metric.__init__(self, 'test')

class TestMetric(unittest.TestCase):
    def test_name_and_metric(self):
        metric = Nothing()
        self.assertEqual('nothing', metric.metric)
        self.assertEqual('test', metric.name)

###

if __name__ == '__main__':
    unittest.main()
