import unittest
from pymetrics.counter import Counter

class TestCounter(unittest.TestCase):
    def test_name_and_metric(self):
        metric = Counter('example')
        self.assertEqual('counter', metric.metric)
        self.assertEqual('example', metric.name)

    def test_initial_value(self):
        counter = Counter('example', 10)
        self.assertEqual(10, counter.count)

    def test_initial_value_None(self):
        counter = Counter('example', None)
        self.assertEqual(0, counter.count)

    def test_value(self):
        counter = Counter('example')
        self.assertEqual(0, counter.count)

        counter.inc()
        self.assertEqual(1, counter.count)

        counter.dec()
        self.assertEqual(0, counter.count)

        counter.inc(5)
        self.assertEqual(5, counter.count)

        counter.dec(3)
        self.assertEqual(2, counter.count)

        counter.inc(None)
        self.assertEqual(2, counter.count)

        counter.dec(None)
        self.assertEqual(2, counter.count)


###

if __name__ == '__main__':
    unittest.main()
