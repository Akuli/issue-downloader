from __future__ import annotations
import typing as t

# ErrorBound = t.TypeVar("ErrorBound", bound=t.Type[Exception])
# HandlerCallable = t.Callable[[ErrorBound], None]
HandlerCallable = t.Callable[[Exception], None]
HandlerDecorator = t.TypeVar("HandlerDecorator", bound=HandlerCallable)

def handler(code: t.Type[Exception]) -> t.Callable[[HandlerDecorator], HandlerDecorator]:
    def wrapper(f: HandlerDecorator) -> HandlerDecorator:
        return f

    return wrapper

# This is the basic use case. It should pass.
@handler(ValueError)
def one(e: ValueError) -> None:
    pass

# This should pass. It's not required to match the decorator
# argument to the decorated parameter, although that would b a nice bonus.
@handler(ValueError)
def two(e: Exception) -> None:
    pass

# This should also pass. It is possible to stack the decorator,
# and the user should be able to annotate that their function
# takes a union of Exceptions.
@handler(ValueError)
@handler(TypeError)
def three(e: ValueError | TypeError) -> None:
    pass

# This should fail, str is not a type of exception.
@handler(ValueError)
@handler(TypeError)
def four(e: str) -> None:
    pass
