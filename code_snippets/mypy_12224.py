from typing import Union
class A:
    def __init__(self, a): ...
    
Test1 = str | A  # error
Test2 = Union[str, A]
