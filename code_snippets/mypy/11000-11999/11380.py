from typing import Any, cast

MYPY = False

def foo(p):
    # type: (Any) -> int
    doc = p
    if MYPY:
        return cast(int, doc)
    else:
        # needs to be in else for MYPY to believe this is reachable
        return doc

def bar(p):
    # type: (Any) -> int
    doc = p
    if MYPY:
        return cast(int, doc)
    return doc
