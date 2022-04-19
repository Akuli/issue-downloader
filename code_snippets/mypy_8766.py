import contextlib
from typing import Iterator

@contextlib.contextmanager
def context_func() -> Iterator[None]:
    try:
        yield
    except Exception:
        pass

def foo() -> None:
    with context_func():
        raise Exception

    print("xxx")  # mypy: Statement is unreachable
