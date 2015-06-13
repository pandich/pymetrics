import util
from timeunit import *

class Duration:
    def __init__(self, unit, value):
        if not util.issubclass_recursive(unit, TimeUnit):
            raise TypeError('unit must be a time unit')

        if value is None:
            raise ValueError('value must not be None')

        self._nanoseconds = unit.from_unit(unit, value)
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
    def hundredth_second(self):
        return nanosecond.to_unit(
            hundredth_second,
            self._nanoseconds,
        )

    @property
    def tenth_second(self):
        return nanosecond.to_unit(
            tenth_second,
            self._nanoseconds,
        )

    @property
    def second(self):
        return nanosecond.to_unit(
            second,
            self._nanoseconds,
        )

    @property
    def minute(self):
        return nanosecond.to_unit(
            minute,
            self._nanoseconds,
        )

    @property
    def hour(self):
        return nanosecond.to_unit(
            hour,
            self._nanoseconds,
        )

    @property
    def day(self):
        return nanosecond.to_unit(
            day,
            self._nanoseconds,
        )
