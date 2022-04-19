from typing import List, TypeVar, Union

It = Union[str, int]

T = TypeVar("T")
def foo(a: Union[T, bool], b: List[T]) -> None: ...
def bar(a: T, b: List[T]) -> None: ...

it: It
data: List[It]

foo(it, data)  # Cannot infer type argument 1 of "foo"
bar(it, data)
