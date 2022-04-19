from typing import Callable, List

def foo(factories: List[Callable[[], int]]):
    return sum(f() for f in factories)

names = ["0", "abc"]
# Inference works fine
assert foo([lambda: len(name) for name in names]) == 4
# Cannot infer type of lambda
assert foo([lambda name=name: len(name) for name in names]) == 4

def foo2(factories: List[Callable[[int], int]]):
    return sum(f(0) for f in factories)

# Inference works fine
assert foo2([lambda i: len(name) for name in names]) == 4
# Cannot infer type of lambda
assert foo2([lambda i, name=name: len(name) for name in names]) == 4
