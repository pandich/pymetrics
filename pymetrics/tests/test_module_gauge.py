import unittest
import fake
from pymetrics.module_gauge import ModuleGauge

def name():
    return 'example'


class TestModuleGauge(unittest.TestCase):
    def test_get_value(self):
        gauge = ModuleGauge('name', fake, 'name')
        self.assertEqual('fake', gauge.value())


###

if __name__ == '__main__':
    unittest.main()
