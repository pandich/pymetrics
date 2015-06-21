import unittest
from time import sleep
from pymetrics.registry import name
from pymetrics.timer import Timer

class TestTimer(unittest.TestCase):

    def test_with(self):
        timer = Timer(name('example'))
        with timer:
            sleep(2)

        print timer.mean()


###

if __name__ == '__main__':
    unittest.main()
