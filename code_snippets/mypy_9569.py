from typing import TypeVar, List, Type


TypeArgT = TypeVar("TypeArgT", Type, List[Type])

def type_a(*args: TypeArgT):
    ...
    
    
def type_b(*args: List[Type]):
    ...
    
type_a(int, str, float)             # test t1
type_a([str, float], [int])         # test t2   <-- this does not work

type_b([bool, bool], [str, bool])   # test t3

