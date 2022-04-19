from typing import Union, List

class A: pass
class B: pass

class Base:
    variable1 : List[Union[A, B]] = []
    variable2 : List[Union[A, B]] = []

class Derived(Base):
    variable1 = [A()]
    variable2 = variable1
