import unittest
from time import sleep
from pymetrics.counter import Counter
from pymetrics.timer import Timer
from pymetrics.registry import registry, name
from pymetrics.json_reporter import JsonReporter
from pymetrics.duration import Duration


class TestJsonReporter(unittest.TestCase):
    def test_a(self):
        c = Counter(name('some', 'example', 1))
        registry.register(c)
        t = Timer('time')
        registry.register(t)
        reporter = JsonReporter(
            registry,
            refresh_interval=Duration.from_seconds(2),
        )
        reporter.start()

        for x in range(1, 10):
            context = t.time()
            try:
                sleep(1)
                c.inc(x)
            finally:
                context.stop()

        reporter.stop()


###

if __name__ == '__main__':
    unittest.main()
