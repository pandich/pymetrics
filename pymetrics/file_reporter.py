import sys
from reporter import Reporter

class FileReporter(Reporter):
    def __init__(self, registry, refresh_interval, filename=None):
        Reporter.__init__(self, registry, refresh_interval)
        self._filename = filename
        if filename:
            self._fh = open(filename, 'w')
        else:
            self._fh = sys.stdout
        return

    def __del__(self):
        self._fh.close()
        return

    @property
    def filename(self):
        return self._filename

    def push(self, dump):
        print >>self._fh, self.generate_output(dump)
        return

    def generate_output(self, dump):
        raise NotImplementedError
