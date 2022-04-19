from typing import Optional


def foo(bla: Optional[str] = None):
    if bla is None:
        bla = "blabla"
    bla.lower()

