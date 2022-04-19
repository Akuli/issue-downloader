from typing import TypeVar, Any, Callable, AnyStr

F = TypeVar('F', bound=Callable)

def on_exception_return(to_return):
    # type: (Any) -> Callable[[F], F]
    pass

@on_exception_return(False)
def is_on(feature_name):
    # type: (AnyStr) -> bool
    return True

class A: pass
class B: pass

X = TypeVar('X', A, B)

def f(x: X) -> None:
    is_on('')
