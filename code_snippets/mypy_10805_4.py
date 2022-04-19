from typing import Any, Protocol, TypeVar, Callable, cast

T = TypeVar('T', bound=Callable[..., Any])


class CountedFunction(Protocol[T]):
    __call__: T
    count: int


def counter(func: T) -> CountedFunction[T]:
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0  # type: ignore
    return cast(CountedFunction[T], wrapper)


# usage with a normal function
@counter
def greet(name: str) -> str:
    return f'hello, {name}'


print(greet('John'))  # OK
print(f'greet() called {greet.count} times')


# usage with a class function
class A:
    @counter
    def greet(self, name: str) -> str:
        return f'hello, {name}'


a = A()
print(a.greet('John'))  # error
print(f'greet() called {a.greet.count} times')
