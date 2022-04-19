from typing import Final, Optional, TypedDict

KEY_NAME: Final = "bar"


class Foo(TypedDict):
    bar: Optional[str]


foo = Foo(bar="hello")

if foo["bar"] is not None:
    # ok
    string1: str = foo["bar"]

    # (expression has type "Optional[str]", variable has type "str")
    string2: str = foo[KEY_NAME]

if foo[KEY_NAME] is not None:
    # (expression has type "Optional[str]", variable has type "str")
    string3: str = foo[KEY_NAME]

    # (expression has type "Optional[str]", variable has type "str")
    string4: str = foo["bar"]
