from typing import overload

@overload
def foo(a: int) -> int: ...
# this overload was just removed
# @overload
# def foo(a: None) -> str ...
@overload
def foo(a: str) -> str: ...
def foo(a: object) -> object: ...

a = foo(None)  # error: No overload variant of "foo" matches argument type "None"\
    # error: Expression has type "Any"

reveal_type(a)  # error: Expression has type "Any"\
  # note: Revealed type is "Any"
print(a) # error: Expression has type "Any"
bar(a) # error: Expression has type "Any"
a + "asdf" # error: Expression has type "Any"
