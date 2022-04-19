from typing import Optional, Iterable, TypeVar, Callable

T = TypeVar('T')


def is_even(n: int) -> bool:
    return n % 2 == 0


# equivalent to https://ruby-doc.org/core-2.5.0/Enumerable.html#method-i-detect
def detect(function: Callable[[T], bool],
           iterable: Iterable[T]) -> Optional[T]:
    for element in iterable:
        if function(element):
            return element
    return None


numbers = [1, 2, 3, 4, 5]

# using a lambda
print(detect(lambda n: n % 2 == 0, numbers))

# using a function
print(detect(is_even, numbers))

