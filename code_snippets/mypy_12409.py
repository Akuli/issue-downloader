import sys


def foo() -> None:
    assert sys.platform == "AMONGUS"
    a # error, reachable ❌

cond: bool
if cond:
    assert sys.platform == "AMONGUS"
    a # error, reachable ❌

assert sys.platform == "AMONGUS"
a  # no error, silent unreachable ✅
