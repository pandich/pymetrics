import unittest

from pymetrics.unit.timeunit import *


class TestTimeUnit(unittest.TestCase):
    def test_minute_to_second(self):
        self.assertAlmostEqual(60, minutes.to_unit(seconds, 1))

###

if __name__ == '__main__':
    unittest.main()
