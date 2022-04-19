@overload
def __sub__(self, other: Union[timedelta, relativedelta]) -> "Arrow":
    pass  # pragma: no cover

@overload
def __sub__(self, other: Union[dt_datetime, "Arrow"]) -> timedelta:
    pass  # pragma: no cover

def __sub__(self, other: Any) -> Union[timedelta, "Arrow"]:

    if isinstance(other, (timedelta, relativedelta)):
        return self.fromdatetime(self._datetime - other, self._datetime.tzinfo)

    elif isinstance(other, dt_datetime):
        return self._datetime - other

    elif isinstance(other, Arrow):
        return self._datetime - other._datetime

    return NotImplemented

import arrow

a1 = arrow.get()
a2 = arrow.get()

diff = a2 - a1
print(diff.total_seconds())

from datetime import timedelta
import arrow

a1 = arrow.get()
a2 = arrow.get()

diff: timedelta = a2 - a1
print(diff.total_seconds())
