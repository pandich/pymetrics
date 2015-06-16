import json
from reporter import Reporter
from flask import Flask, app

class HttpReporter(Reporter):
    def __init__(self, registry, name='metrics', host='0.0.0.0', port=8080):
        Reporter.__init__(self, registry)
        self._name = name
        self._host = host
        self._port = port
        self._server = Flask(name)
        return

    def run(self):
        super(HttpReporter, self).run()
        self._server.run(host=self._host, port=self._port)
        return

    def generate_output(self, dump):
        return json.dumps(
            dump,
            indent=4,
            separators=(', ', ': '),
        )
