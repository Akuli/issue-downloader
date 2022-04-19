from typing import TypeVar

T = TypeVar('T')

def function(arg: T) -> T:
    if isinstance(arg, type) and issubclass(arg, Exception):
        raise RuntimeError
    return arg  # error: Incompatible return value type (got "Union[T, Type[object]]", expected "T")  [return-value]
