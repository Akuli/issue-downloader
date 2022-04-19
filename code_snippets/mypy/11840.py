from typing import List, Sequence, TypedDict, Union

class TypeA(TypedDict):
    fieldB: str
    fieldC: bool

class _TypeB(TypedDict):
    fieldA: str
    fieldB: str

class TypeB(_TypeB, total=False):
    fieldC: bool

ComponentT = Union[TypeA, TypeB]
ComponentListT = List[ComponentT]  # Using List or Sequence causes an error.

def process(val: ComponentT) -> ComponentT:
    return val

def example(val: ComponentListT) -> ComponentListT:
    return [process(part) for part in val]
