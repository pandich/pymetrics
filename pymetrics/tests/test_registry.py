import unittest
from pymetrics.metric import Metric
from pymetrics.registry import Registry

class Nothing(Metric):
    def __init__(self):
        Metric.__init__(self, 'test')


class TestCoreRegistry(unittest.TestCase):
    def test_register_and_size(self):
        registry = Registry()
        self.assertEqual(0, registry.size())
        registry.register(Nothing())
        self.assertEqual(1, registry.size())

    def test_to_string(self):
        registry = Registry()
        registry.register(Nothing())
        self.assertGreater(str(registry).index('name:"test"'), 0)

###

if __name__ == '__main__':
    unittest.main()
