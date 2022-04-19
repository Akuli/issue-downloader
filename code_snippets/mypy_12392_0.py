from typing import Type, TypeAlias

A = type[int] | str  # error: Value of type "Type[type]" is not indexable
B = Type[int] | str  # error: Unsupported left operand type for | ("object")
C: TypeAlias = type[int] | str  # error: Value of type "Type[type]" is not indexable
D: TypeAlias = Type[int] | str  # error: Unsupported left operand type for | ("object")
