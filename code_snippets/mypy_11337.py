from typing import Optional


def foo(s: str) -> None:
    pass


def bar(s: Optional[str] = None) -> None:
    if not s:
        return

    d: dict[str, str] = {}
    s = d.get(s, s)
    foo(s)  # Argument 1 to "foo" has incompatible type "Optional[str]"; expected "str"
