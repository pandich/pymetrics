import timeunit
import util
from metric import Metric

class HealthCheck(Metric):

    class Result:
        def __init__(self, is_healthy, message=None):
            self._healthy = is_healthy
            self._message = message
            return

        @property
        def healthy(self):
            return self._healthy

        @property
        def message(self):
            return self._message

    def __init__(self, name):
        Metric.__init__(self, name)
        return

    @property
    def name(self):
        return self._name

    def check(self):
        raise NotImplementedError

    def dump(self):
        when = timeunit.now()
        health = self.check()

        return {
            self._name: {
                'result': {
                    'time': when,
                    'healthy': health.healthy,
                    'message': util.coalesce(health.message, ''),
                }
            }
        }

def healthy():
    return HealthCheck.Result(True)


def unhealthy(message=None):
    return HealthCheck.Result(False, message)
