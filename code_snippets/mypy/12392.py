from typing import Type, TypeAlias

A = type[int] | str  # error: Value of type "Type[type]" is not indexable
B = Type[int] | str  # error: Unsupported left operand type for | ("object")
C: TypeAlias = type[int] | str  # error: Value of type "Type[type]" is not indexable
D: TypeAlias = Type[int] | str  # error: Unsupported left operand type for | ("object")

E = str | type[int]  # error: Value of type "Type[type]" is not indexable
F: TypeAlias = str | type[int]  # error: Value of type "Type[type]" is not indexable

B = Type[int] | str  # error: Unsupported left operand type for | ("object")
D: TypeAlias = Type[int] | str  # error: Unsupported left operand type for | ("object")
G = str | Type[int]  # no error

E = list[type[int] | str]
F = type[int | str]

from typing import Union
G = Union[type[int], str]
