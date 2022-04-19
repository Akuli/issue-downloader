from typing import AnyStr, Union
def g(a: AnyStr) -> AnyStr:
    pass
def f(a: Union[str, bytes]):
    g(a)
