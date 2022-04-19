from typing import overload, Union

class A:
    def f(self, x: Union[int, str]) -> None: ...
    
class B(A):
    @overload
    def f(self, x: int) -> None: ...
    @overload
    def f(self, x: str) -> None: ...
    def f(self, x: Union[int, str]) -> None: ...

arg: Union[int, str]
B().f(arg)

