import unittest
from pymetrics.metric import Metric
from pymetrics.registry import Registry

class Nothing(Metric):
    def __init__(self):
        Metric.__init__(self, 'test')


class TestCoreRegistry(unittest.TestCase):

    registry = None

    def setUp(self):
        super(TestCoreRegistry, self).setUp()
        self.registry = Registry()

    def test_register_and_size(self):
        self.assertEqual(0, self.registry.count)
        self.registry.register(Nothing())
        self.assertEqual(1, self.registry.count)

    def test_to_string(self):
        self.registry.register(Nothing())
        self.assertGreater(str(self.registry).index('name:"test"'), 0)

###

if __name__ == '__main__':
    unittest.main()
