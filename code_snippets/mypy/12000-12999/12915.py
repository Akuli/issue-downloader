import random


def foo() -> tuple[int, None] | tuple[int, str]:
    if random.choice((True, False)):
        return 0, None
    return 5, "thing"


res = None

status, res = foo()
reveal_type(res)  # builtins.str
