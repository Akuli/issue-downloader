from typing_extensions import Literal
from typing import Union


HTTPMethodName = Union[
    Literal['GET'],
    Literal['POST'],
]


class A:
    method: HTTPMethodName


class B(A):
    # works if the subclass also annotates the property
    method: HTTPMethodName = 'POST' 


class C(A):
    # error: Incompatible types in assignment (expression has type "str", base class "A" defined the type as "Union[Literal['GET'], Literal['POST']]")
    method = 'POST'

[mypy]
ignore_missing_imports = True
strict_optional = True
no_implicit_optional = True
check_untyped_defs = True
disallow_incomplete_defs = True

