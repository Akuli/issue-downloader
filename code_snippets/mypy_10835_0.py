from typing import TypeVar

# context:
T = TypeVar('T')
class A: pass
class B: pass


def function1(obj: T) -> T:  # expected behaviour:
    if isinstance(obj, A):
        pass
    elif isinstance(obj, B):
        pass
    return obj  # no problem here

def function2(obj: T) -> T:  # unexpected behaviour:
    if isinstance(obj, (A, B)):
        pass
    return obj  # mypy has forgotten that obj is of type T
