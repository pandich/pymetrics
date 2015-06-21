import unittest
from pymetrics.metric import Metric
from pymetrics.registry import Registry, name

class Nothing(Metric):
    def __init__(self):
        Metric.__init__(self, 'nothing')

    def dump(self):
        return {}


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
        print self.registry.metrics
        self.assertIsNone(self.registry.get('not_there'))
        self.assertIsNotNone(self.registry.get('nothing'))

    def test_name(self):
        self.assertEquals(name('a'), 'a')
        self.assertEquals(name('a', 'b'), 'a.b')
        self.assertEquals(name(Nothing, 'b'), 'test_registry.Nothing.b')

###

if __name__ == '__main__':
    unittest.main()
