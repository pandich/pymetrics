import unittest
from pymetrics.health_check import HealthCheck, healthy, unhealthy

class FakeHealthCheck(HealthCheck):
    def __init__(self, name):
        HealthCheck.__init__(self)
        self.healthy = good
        return

    def check(self):
        return healthy() if self.healthy else unhealthy('woops')


class TestHealthCheck(unittest.TestCase):
    def test_simple_healthy(self):
        hc = FakeHealthCheck()
        self.assertTrue(hc.check().healthy)
        return

    def test_simple_unhealthy(self):
        hc = FakeHealthCheck(False)
        self.assertTrue(not hc.check().healthy)
        self.assertEqual(hc.check().message, 'woops')
        return

###

if __name__ == '__main__':
    unittest.main()
