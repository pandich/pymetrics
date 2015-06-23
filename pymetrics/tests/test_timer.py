import unittest
from time import sleep

from pymetrics.registry import name
from pymetrics.timer import Timer
from pymetrics.unit.timeunit import milliseconds, seconds


class TestTimer(unittest.TestCase):
    def test_with(self):
        sleep_time = 1.0
        timer = Timer(name('example'))
        with timer.time():
            sleep(sleep_time)

        self.assertAlmostEqual(timer.mean(), milliseconds.from_unit(seconds, sleep_time), places=-1)


###

if __name__ == '__main__':
    unittest.main()
