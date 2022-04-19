from typing import Mapping


def f(x: Mapping[str, object]) -> int:
    d = {
        "foo": 3.14,
        **x,
    }
    return len(d)
