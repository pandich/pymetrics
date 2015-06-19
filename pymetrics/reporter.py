from threading import Thread, Event
from duration import *
from timeunit import seconds
from registry import Registry
from time import sleep
import util


class Reporter(Thread):
    default_interval = Duration(seconds, 30)

    def __init__(self, registry, refresh_interval=default_interval):
        Thread.__init__(self, name='metrics-reporter')
        self.stopped = Event()
        self._registry = registry
        self.refresh_seconds = refresh_interval.seconds
        self.daemon = True
        return

    def push(self, dump):
        raise NotImplementedError

    def report(self):
        report_body = {}
        for name, metric in self._registry.metrics.iteritems():
            report_body[name] = metric.dump()

        self.push(report_body)
        return

    def stop(self):
        self.stopped.set()
        return

    def run(self):
        while not self.stopped.isSet():
            self.report()
            sleep(self.refresh_seconds)
        return
