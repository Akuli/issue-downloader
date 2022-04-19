
from typing import Any, Generator


def foo() -> Generator[int, Any, None]:
    yield
    while True:
        yield 42
