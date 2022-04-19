from typing import TypeVar

T = TypeVar("T")

def default(value: T | None, value_if_none: T) -> T:
    return value_if_none if value is None else value


foo: list[str] | None = []

bar = default(foo, [])

# expected: list[str]
# actual: Revealed type is "builtins.object*"
reveal_type(bar) 
