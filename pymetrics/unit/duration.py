from pymetrics.unit.timeunit import *


class Duration(object):

    @staticmethod
    def from_nanoseconds(t):
        return Duration(nanoseconds, t)

    @staticmethod
    def from_microseconds(t):
        return Duration(microseconds, t)

    @staticmethod
    def from_milliseconds(t):
        return Duration(milliseconds, t)

    @staticmethod
    def from_hundredth_seconds(t):
        return Duration(hundredth_seconds, t)

    @staticmethod
    def from_tenth_seconds(t):
        return Duration(tenth_seconds, t)

    @staticmethod
    def from_seconds(t):
        return Duration(seconds, t)

    @staticmethod
    def from_minutes(t):
        return Duration(minutes, t)

    @staticmethod
    def from_hours(t):
        return Duration(hours, t)

    @staticmethod
    def from_days(t):
        return Duration(days, t)

    def __init__(self, unit, value):
        if value is None:
            raise ValueError('value must not be None')

        self._nanoseconds = nanoseconds.from_unit(unit, value)
        return

    @property
    def nanoseconds(self):
        return self._nanoseconds

    @property
    def microseconds(self):
        return nanoseconds.to_unit(
            microseconds,
            self._nanoseconds,
        )

    @property
    def milliseconds(self):
        return nanoseconds.to_unit(
            milliseconds,
            self._nanoseconds,
        )

    @property
    def hundredth_seconds(self):
        return nanoseconds.to_unit(
            hundredth_seconds,
            self._nanoseconds,
        )

    @property
    def tenth_seconds(self):
        return nanoseconds.to_unit(
            tenth_seconds,
            self._nanoseconds,
        )

    @property
    def seconds(self):
        return nanoseconds.to_unit(
            seconds,
            self._nanoseconds,
        )

    @property
    def minutes(self):
        return nanoseconds.to_unit(
            minutes,
            self._nanoseconds,
        )

    @property
    def hours(self):
        return nanoseconds.to_unit(
            hours,
            self._nanoseconds,
        )

    @property
    def days(self):
        return nanoseconds.to_unit(
            days,
            self._nanoseconds,
        )
