Type = type

class MyInt(int):
    pass

x_type: Type[int] = MyInt

from __future__ import annotations

if sys.version_info >= (3, 9):
    List = list
    Type = type
else:
    # Legacy generic type annotation classes
    # Deprecated in Python 3.9
    # Remove once we no longer support Python 3.8 or lower
    from typing import List
    from typing import Type

class MyCustomContext:
    data: List[int]

    def __init__(self):
        self.data = []

    def __enter__(self) -> MyCustomContext:
        return self

    def add(i: int) -> None:
        self.data.append(i)

    def __exit__(
        self,
        ex_type: Optional[Type[Exception]],
        ex_value: Optional[Exception],
        ex_traceback: Optional[TracebackType],
    ) -> None:
        if ex_value is None and len(self.data) > 100:
            raise ValueError('Too much data')

