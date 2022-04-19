from typing import *

class A:
    a = None  # type: List[str]
    b = None  # type: List[Union[str, int]]
    c = None  # type: List[Union[str, int]]
    d = None  # type: Sequence[Union[str, int]]

class B(A):
    a = ['foo']
    b = ['foo']
    c = ['foo', 1]
    d = ['foo', 1]

reveal_type(B.a)  # 'builtins.list[builtins.str*]'
reveal_type(B.b)  # 'builtins.list[builtins.str*]'
reveal_type(B.c)  # 'builtins.list[builtins.object*]'
reveal_type(B.d)  # 'builtins.list[builtins.object*]'
