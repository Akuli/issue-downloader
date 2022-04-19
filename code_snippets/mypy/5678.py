import sys
from typing import Generator

def f() -> Generator[int, None, None]:
    if sys.platform == "darwin":
        yield 1
