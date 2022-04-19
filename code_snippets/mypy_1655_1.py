from typing import Callable

def test_func(a, b, *, c, d):
    # type: (int, int, int, int) -> int
    return a + b + c + d

def check_func(method):
    # type: (Callable[[int, int, int, int], int]) -> int
    return method(1, 2, c=5, d=10)

print(check_func(test_func))
