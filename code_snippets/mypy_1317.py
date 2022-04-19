from typing import *
from contextlib import *

T = TypeVar("T")

@contextmanager
def foo(x):
  # type: (T) -> Iterator[T]
  yield x

y = 1
with foo(2) as f:
  y = f
