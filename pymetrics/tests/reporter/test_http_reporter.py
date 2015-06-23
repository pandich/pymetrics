import unittest
from time import sleep

from pymetrics.counter import Counter
from pymetrics.timer import Timer
from pymetrics.registry import registry, name
from pymetrics.reporter.http_reporter import HttpReporter


class TestHttpReporter(unittest.TestCase):
    def test_a(self):
        c = Counter(name('some', 'example', 1))
        registry.register(c)
        t = Timer('time')
        registry.register(t)
        reporter = HttpReporter(
            registry,
        )
        reporter.start()

        with t.time():
            sleep(2)

        for x in range(1, 20):
            sleep(1)
            c.inc()

        reporter.stop()


###

if __name__ == '__main__':
    unittest.main()
