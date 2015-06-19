import unittest
import random
from time import sleep
from pymetrics.counter import Counter
from pymetrics.timer import Timer, timed
from pymetrics.meter import metered
from pymetrics.registry import registry, name
from pymetrics.json_reporter import JsonReporter
from pymetrics.duration import Duration


class TestJsonReporter(unittest.TestCase):

    @timed
    def bob(self):
        sleep(random.random())
        return 'hi'

    @timed(metric_prefix='hey')
    @metered
    def joe(self):
        sleep(random.random())
        return 'hi'

    def test_a(self):
        reporter = JsonReporter(
            registry,
            refresh_interval=Duration.from_seconds(2),
        )
        reporter.start()

        for x in range(1, 10):
            self.joe()
            self.bob()
            sleep(1)

        reporter.stop()

###

if __name__ == '__main__':
    unittest.main()
