import util
from threading import Thread, Event
from duration import *
from timeunit import minute
from registry import Registry
from time import sleep

Duration.minutes
_default_interval = Duration(minute, 1)

class Reporter(Thread):

    def __init__(self, registry, refresh_interval=_default_interval):
        Thread.__init__(self, name='metrics-reporter')
        self.stopped = Event()

        if not util.issubclass_recursive(refresh_interval, Duration):
            raise ValueError('refresh interval must be a duration')

        if not util.issubclass_recursive(registry, Registry):
            raise ValueError('registry must be a registry')

        self._registry = registry
        self.refresh_seconds = refresh_interval.seconds
        self.daemon = True

    def push(self, dump):
        return

    def report(self):
        dump = {}
        for name, metric in self._registry.metrics.iteritems():
            dump[name] = metric.dump()

        self.push(dump)
        return

    def stop(self):
        self.stopped.set()
        return

    def run(self):
        while not self.stopped.isSet():
            self.report()
            sleep(self.refresh_seconds)
        return


class CsvReporter(Reporter):
    def __init__(self, registry, refresh_interval, filename=None):
        Reporter.__init__(self, registry, refresh_interval)
        self._filename = filename
        return

    def push(self, dump):
        flattened_dump = util.flatten(dump)
        with util.smart_open(self._filename) as fh:
            for name, value in flattened_dump.iteritems():
                line = name + ',' + str(value)
                print >>fh, line

        return
