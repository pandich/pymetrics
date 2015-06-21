import time


class TimeUnit(object):
    def __init__(self, multiplier):
        self.multiplier = multiplier
        return

    def from_unit(self, unit, value):
        if not value:
            return value

        ratio = self.multiplier / unit.multiplier
        return value * ratio

    def to_unit(self, unit, value):
        if not value:
            return value

        ratio = unit.multiplier / self.multiplier
        return value * ratio


class _Nanosecond(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self, 10.0**9)
        return


class _Microsecond(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self, 10.0**6)
        return


class _Millisecond(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self, 10.0**3)
        return


class _HundredthSecond(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self, 10.0**3)
        return


class _TenthSecond(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self, 10.0**1)
        return


class _Second(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self, 10.0**0)
        return


class _Minute(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self, 1.0/60.0)
        return


class _Hour(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self, 1.0/(60.0 * 60.0))
        return


class _Day(TimeUnit):
    def __init__(self):
        TimeUnit.__init__(self, 1.0/(60.0 * 60.0 * 24.0))
        return


nanoseconds = _Nanosecond()
microseconds = _Microsecond()
milliseconds = _Millisecond()
hundredth_seconds = _HundredthSecond()
tenth_seconds = _TenthSecond()
seconds = _Second()
minutes = _Minute()
hours = _Hour()
days = _Day()


def now():
    return nanoseconds.from_unit(microseconds, time.time())
