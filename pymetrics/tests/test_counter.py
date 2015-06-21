import unittest
from pymetrics.counter import Counter

class TestCounter(unittest.TestCase):
    def test_name_and_metric(self):
        metric = Counter('example')
        self.assertEqual('counter', metric.metric)
        self.assertEqual('example', metric.name)

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

    def test_with(self):
        counter = Counter('example')
        self.assertEquals(counter.count, 0)
        with counter:
            pass
        self.assertEquals(counter.count, 1)


###

if __name__ == '__main__':
    unittest.main()
