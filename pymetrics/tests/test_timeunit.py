import unittest
from pymetrics.timeunit import *

class TestTimeUnit(unittest.TestCase):
    def test_minute_to_second(self):
        self.assertAlmostEqual(60, minute.to_unit(second, 1))

###

if __name__ == '__main__':
    unittest.main()
