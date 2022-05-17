import datetime
from typing import Any

class MyDatetime(datetime.datetime):
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, datetime.datetime):
            delta = self - other  # error: No overload variant of "__sub__" of "datetime" matches argument type "datetime"  [operator]
            delta = other - self  # OK
            return True
        else:
            return NotImplemented

_D = TypeVar("_D", bound=date)

class datetime(date):
    if sys.version_info >= (3, 8):
        def __sub__(self: _D, __other: _D) -> timedelta: ...
    else:
        def __sub__(self, __other: datetime) -> timedelta: ...
