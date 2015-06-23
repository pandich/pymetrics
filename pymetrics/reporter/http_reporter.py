import json
from threading import Thread
from reporter import Reporter
from flask import Flask
from flask_classy import FlaskView, route

class HttpReporter(Reporter):

    def __init__(self, registry, host='0.0.0.0', port=9091):
        Reporter.__init__(self, registry)
        self._host = host
        self._port = port
        self.snapshot = {}

        reporter = self

        class ReporterView(FlaskView):

            route_base = '/'

            def __init__(self):
                FlaskView.__init__(self)
                return

            @route('/')
            def snapshot(self):
                return HttpReporter.generate_output(reporter.snapshot)

        def start_app():
            app = Flask(__name__)
            ReporterView.register(app)
            app.run(host=self._host, port=self._port, debug=True)

        self._http_thread = Thread(name='metrics_web_server', target=start_app, verbose=True)
        return

    def start(self):
        super(HttpReporter, self).start()
        self._http_thread.start()
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
