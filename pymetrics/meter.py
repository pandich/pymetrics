from histogram import Histogram
from metric import metric_decorated


class Meter(Histogram):
    def __init__(self, name):
        Histogram.__init__(self, name)
        return

    def mark(self):
        self.update()
        return

    def __enter__(self):
        self.mark()
        return

    def __exit__(*unused):
        pass

def metered(target=None, **options):
    def before(record):
        record.meter.mark()
        return

    return metric_decorated(
        target,
        Meter,
        metered,
        before=before,
        **options
    )
