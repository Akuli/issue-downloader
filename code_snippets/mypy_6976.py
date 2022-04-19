from typing import List


def foo() -> None:
    global bar
    bar = []  # type: List[str]  # Name 'bar' already defined (possibly by an import)
    bar  # Name 'bar' is not defined
