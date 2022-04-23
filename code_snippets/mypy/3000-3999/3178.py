from typing import TypeVar, Callable

class Summable: ...
class MySummable(Summable): ...
T = TypeVar('T', bound=Summable)
def plus(a: T, b: T) -> T: ...

def plus_partial(t: T) -> Callable[[T], T]:
    def f(t1: T) -> T:
        return plus(t1, t)
    return f

my_s: MySummable
plus_my_s = plus_partial(my_s)

s: Summable
plus_my_s(s)  # E: Argument 1 has incompatible type "Summable"; expected "MySummable"

plus(my_s, s)  # ok
