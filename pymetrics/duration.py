import util
from timeunit import *

class Duration:
    def __init__(self, unit, value):
        if not util.issubclass_recursive(unit, TimeUnit):
            raise TypeError('unit must be a time unit')

        if value is None:
            raise ValueError('value must not be None')

        self._nanoseconds = nanosecond.from_unit(unit, value)
        return

    @property
    def nanoseconds(self):
        return self._nanoseconds

    @property
    def microseconds(self):
        return nanosecond.to_unit(
            microsecond,
            self._nanoseconds,
        )

    @property
    def milliseconds(self):
        return nanosecond.to_unit(
            millisecond,
            self._nanoseconds,
        )

    @property
    def hundredth_seconds(self):
        return nanosecond.to_unit(
            hundredth_second,
            self._nanoseconds,
        )

    @property
    def tenth_seconds(self):
        return nanosecond.to_unit(
            tenth_second,
            self._nanoseconds,
        )

    @property
    def seconds(self):
        return nanosecond.to_unit(
            second,
            self._nanoseconds,
        )

    @property
    def minutes(self):
        return nanosecond.to_unit(
            minute,
            self._nanoseconds,
        )

    @property
    def hours(self):
        return nanosecond.to_unit(
            hour,
            self._nanoseconds,
        )

    @property
    def days(self):
        return nanosecond.to_unit(
            day,
            self._nanoseconds,
        )
