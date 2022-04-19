from typing import Callable, TypeVar, Any, List

T = TypeVar('T')
T1 = TypeVar('T1')
T2 = TypeVar('T2')


def chain(f1: Callable[[Any],T1], f2: Callable[[T1], T2]) -> Callable[[Any], T2]:
    def chained(x: Any) -> T2:
        return f2(f1(x))

    return chained


# Two toy functions
def identity(x: T) -> T: 
    return x


def to_str(x: Any) -> str:
    return str(x)


# (mypy: "Cannot infer type argument 1 of chain")
chained = chain(to_str, identity)
str_var: str = chained(123)
print(str_var)
