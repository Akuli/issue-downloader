from typing import Union
 
class Foo:
    def __mod__(self, other: Union[Foo, str]) -> int: ...   
    def __rmod__(self, other: str) -> int: ...   
