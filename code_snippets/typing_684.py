import builtins
from typing import List, Union


def fun(x: Union[builtins.ellipsis, List], y: List):
    if x is not Ellipsis:
        y = x #  error: Incompatible types in assignment (expression has type "Union[ellipsis, List[Any]]", variable has type "List[Any]")

    return y

# another attempt:
def fun2(x: Union[Ellipsis, List], y: List): # error: Variable "builtins.Ellipsis" is not valid as a type
    if x is not Ellipsis:
        y = x

    return y

