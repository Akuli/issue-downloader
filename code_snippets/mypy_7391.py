from contextlib import AbstractContextManager
from typing import TYPE_CHECKING, Optional, Type
from types import TracebackType

if TYPE_CHECKING:
    _Base = AbstractContextManager['A']  # problematic "line 6"
else:
    _Base = AbstractContextManager

class A(_Base):
    def __enter__(self) -> 'A':
        return self

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType],
                 ) -> Optional[bool]:
        return None

a = A()
