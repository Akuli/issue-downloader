def doit(constructor: Callable[..., T]) -> List[T]:
    ...

from typing import Callable, List, Protocol, TypeVar

_T = TypeVar("_T")

# error: Incompatible default for argument "constructor" (default has type "Type[str]", argument has type "Callable[[int], _T]")
def generate(n: int, constructor: Callable[[int], _T] = str) -> List[_T]:
    return [constructor(i) for i in range(n)]

# error: Need type annotation for "res" (hint: "res: List[<type>] = ...")
res = generate(5)  # res should be of type List[str]
assert res == ["0", "1", "2", "3", "4"]
assert generate(5, float) == [0.0, 1.0, 2.0, 3.0, 4.0]

_T_co = TypeVar("_T_co", covariant=True)

class Constructor(Protocol[_T_co]):
    def __call__(self, n: int) -> _T_co:
        ...

def generate2(n: int, constructor: Constructor[_T] = str) -> List[_T]:
    return [constructor(i) for i in range(n)]

# error: Need type annotation for "res2" (hint: "res2: List[<type>] = ...")
res2 = generate2(5, float)  # res2 should be of type List[float]
assert res2 == [0.0, 1.0, 2.0, 3.0, 4.0]

