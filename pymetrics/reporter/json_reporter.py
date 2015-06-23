import json
from file_reporter import FileReporter


class JsonReporter(FileReporter):
    def __init__(self, registry, refresh_interval, filename=None):
        FileReporter.__init__(self, registry, refresh_interval, filename)
        return

    def generate_output(self, dump):
        return json.dumps(
            dump,
            indent=4,
            separators=(', ', ': '),
        )
