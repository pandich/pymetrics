from threading import Thread, Event
from pymetrics.unit.duration import Duration
from pymetrics.unit.timeunit import seconds
from time import sleep

class Reporter(object):
    default_interval = Duration(seconds, 1)

    class ReporterThread(Thread):
        def __init__(self, reporter, refresh_interval):
            Thread.__init__(self, name='metrics-reporter', verbose=True)
            self.daemon = True
            self._stop = Event()
            self._reporter = reporter
            self._refresh_interval = refresh_interval.seconds
            return

        def run(self):
            while not self.stopped():
                self._reporter.report()
                sleep(self._refresh_interval)
            return

        def stop(self):
            self._stop.set()
            return

        def stopped(self):
            return self._stop.isSet()

    def __init__(self, registry, refresh_interval=default_interval):
        self._thread = Reporter.ReporterThread(self, refresh_interval)
        self._registry = registry
        return

    def push(self, dump):
        raise NotImplementedError

    def report(self):
        report_body = {}
        for name, metric in self._registry.metrics.iteritems():
            report_body[name] = metric.dump()

        self.push(report_body)
        return

    def start(self):
        self._thread.start()
        return

    def stop(self):
        self._thread.stop()
        return
