import unittest
from time import sleep
from pymetrics.counter import Counter
from pymetrics.timer import Timer
from pymetrics.registry import registry, name
from pymetrics.http_reporter import HttpReporter

class TestHttpReporter(unittest.TestCase):
    @unittest.skip('skip')
    def test_a(self):
        c = Counter(name('some', 'example', 1))
        registry.register(c)
        t = Timer('time')
        registry.register(t)
        reporter = HttpReporter(
            registry,
        )
        reporter.start()

        sleep(60)

        reporter.stop()


###

if __name__ == '__main__':
    unittest.main()
