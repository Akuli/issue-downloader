from typing import Literal

foo: Literal["foo"] = "foo"

# error: Non-overlapping equality check (left operand type: "Literal['foo']", right operand type: "Literal['bar']")  [comparison-overlap]
foo == "bar"


bar: Literal[True]

# no error
bar == False
