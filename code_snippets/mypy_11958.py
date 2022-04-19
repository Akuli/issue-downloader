from typing import cast

foo: str

a = cast(int, foo)

a = cast(int, cast(object, foo))

