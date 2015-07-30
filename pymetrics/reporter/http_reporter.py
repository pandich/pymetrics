import json
from threading import Thread
from reporter import Reporter
from flask import Flask, render_template
from flask_classy import FlaskView, route

class HttpReporter(Reporter):

    def __init__(self, registry, host='0.0.0.0', port=9091):
        Reporter.__init__(self, registry)
        self._snapshot = {}

        reporter = self

        class ReporterView(FlaskView):

            route_base = '/'

            def __init__(self):
                FlaskView.__init__(self)
                return

            @route(route_base)
            def index(self):
                return HttpReporter.generate_output(
                    reporter.snapshot
                )

            @route('/metrics/')
            def metrics(self):
                return HttpReporter.generate_output(
                    reporter.snapshot.get('metrics')
                )

            @route('/health/')
            def metrics(self):
                return HttpReporter.generate_output(
                    reporter.snapshot['health']
                )

        def start_app():
            app = Flask(__name__)
            ReporterView.register(app)
            app.run(host=host, port=port)
            return

        self._http_thread = Thread(
            name='metrics_web_server',
            target=start_app,
            verbose=True,
        )
        return

    def start(self):
        Reporter.start(self)
        self._http_thread.start()
        return

    def push(self, dump):
        self._snapshot = dump
        return

    @property
    def snapshot(self):
        return self._snapshot

    @staticmethod
    def generate_output(dump):
        return json.dumps(
            dump,
            indent=4,
            separators=(', ', ': '),
        )
