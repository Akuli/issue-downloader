from typing import Any, Dict

class Foo(Any):
    pass

d: Dict[Foo, Foo]

def bar(x: Dict[str, str]) -> None:
    pass

bar(d)  # error: Argument 1 to "bar" has incompatible type "Dict[Foo, Foo]"; expected "Dict[str, str]"

from typing import Any, Dict

class Foo(Any):
    pass

foo: Foo

def bar(x: str) -> None:
    pass

bar(foo)
