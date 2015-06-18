import json
from reporter import Reporter
from flask import Flask

app = Flask(__name__)

class HttpReporter(Reporter):
    def __init__(self, registry, host='0.0.0.0', port=9091):
        Reporter.__init__(self, registry)
        self._host = host
        self._port = port
        self.snapshot = {}
        return

    def run(self):
        app.run(host=self._host, port=self._port, debug=True)
        super(HttpReporter, self).run()
        return

    def push(self, dump):
        self.snapshot = dump
        return

    @staticmethod
    def generate_output(dump):
        return json.dumps(
            dump,
            indent=4,
            separators=(', ', ': '),
        )

    @app.route('/', methods=['GET'])
    def snapshot(self):
        return self.snapshot
