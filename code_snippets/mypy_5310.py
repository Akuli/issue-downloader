from typing import Optional


def foo(bla: Optional[str] = None):
    bla_is_none = bla is None
    if bla_is_none:
        bla = "blabla"
    bla.lower()


from typing import Optional


def foo(bla: Optional[str] = None):
    if bla is None:
        bla = "blabla"
    bla.lower()


