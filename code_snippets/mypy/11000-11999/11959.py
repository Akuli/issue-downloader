from typing import Any

foo: Any #type:ignore[misc]

foo # no error

print(foo) # error: Expression has type "Any"
