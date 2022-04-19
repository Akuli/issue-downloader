from typing import TypeVar, Protocol, Any, Callable
import functools

F = TypeVar('F', bound=Callable[..., Any])

def implements(method: Any) -> Callable[[F], F]:
    """
    Meant to be used as

    class B:
        @implements(IExpectedProtocol.method)
        def method(self):
            pass

    Useful for knowing whether a name still exists in the interface and document
    what's being implemented.

    In runtime validates that the name passed is the same name implemented.
    """
    @functools.wraps(method)
    def wrapper(func):
        if func.__name__ != method.__name__:
            msg = "Wrong @implements: %r expected, but implementing %r."
            msg = msg % (func.__name__, method.__name__)
            raise AssertionError(msg)

        return func

    return wrapper

T = TypeVar("T")

def check_implements(x: T) -> T:
    """
    This is to be used in the constructor of a class which is expected to
    implement some protocol. It can be used as:

    def __init__(self):
        _: IExpectedProtocol = check_implements(self)

    Mypy should complain if `self` is not implementing the IExpectedProtocol.
    """
    return x

class IFoo(Protocol):

    def some_method(self) -> bool:
        pass

class Foo(object):

    def __init__(self) -> None:  # give type
        _: IFoo = check_implements(self)  # Issue: Mypy does not report error here

    @implements(IFoo.some_method)  # Note: if this implements is removed it reports the error at the __init__!
    def some_method(self) -> str:  # Note: return value does not match protocol!
        pass

_: IFoo = check_implements(Foo())  # Mypy properly reports error here (with or without the implements decorator).
