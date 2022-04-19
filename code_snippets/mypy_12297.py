# test_case.py
from typing import Callable, Optional, TypeVar, Union, overload

class Foo: pass

class Bar: pass

ReturnsFooOrBarT = Callable[..., Union[Foo, Bar]]
TermT = TypeVar("TermT", bound=ReturnsFooOrBarT)

def returns_foo() -> Foo:
    return Foo()

def returns_bar() -> Bar:
    return Bar()

@overload
def do_something_or_something_else(
    *,
    something_else: Union[int, TermT] = 0,
) -> None:
    ...

@overload
def do_something_or_something_else(
    something: TermT,
    *,
    something_else: Union[int, TermT] = 0,
) -> None:
    ...

def do_something_or_something_else(
    something: Optional[TermT] = None,
    *,
    something_else: Union[int, TermT] = 0,
) -> None:
    pass

do_something_or_something_else(something_else=1)
do_something_or_something_else(something_else=returns_bar)
do_something_or_something_else(something_else=returns_foo)

do_something_or_something_else(returns_foo, something_else=1)
do_something_or_something_else(returns_foo, something_else=returns_foo)

do_something_or_something_else(returns_bar, something_else=1)
do_something_or_something_else(returns_bar, something_else=returns_bar)

returns_foo_or_bar: ReturnsFooOrBarT

# These should all validate, no?
returns_foo_or_bar = returns_foo
do_something_or_something_else(returns_foo_or_bar, something_else=1)
do_something_or_something_else(returns_foo_or_bar, something_else=returns_bar)  # <-- false negative?
do_something_or_something_else(returns_foo, something_else=returns_bar)  # <-- false negative?

# These should all validate, no?
returns_foo_or_bar = returns_bar
do_something_or_something_else(returns_foo_or_bar, something_else=1)
do_something_or_something_else(returns_foo_or_bar, something_else=returns_foo)  # <-- false negative?
do_something_or_something_else(returns_bar, something_else=returns_foo)  # <-- false negative?
