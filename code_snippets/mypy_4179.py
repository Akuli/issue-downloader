import sys
from typing import List
from mypy_extensions import NoReturn

def never_returns() -> NoReturn:
    sys.exit(1)

def foo() -> None:
    x = never_returns()
