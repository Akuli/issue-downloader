from typing import Generic, Optional, Tuple, TypeVar  

# Would like to write bound='TypedCons[T, V]' here, where T is self-referential
T = TypeVar('T', bound='TypedCons')
V = TypeVar('V')  


class TypedCons(Generic[T, V]):  
    def __init__(self, value: V, cdr: Optional[T]=None) -> None:  
        self.value = value  
        self.cdr = cdr  

    def first_two(self) -> Tuple[T, T]:  
        # Fails without cast with "Incompatible return value type: expected Tuple[T`1, T`1], got Tuple[example.TypedCons[T`1, V`2], T`1]"  
        return self, self.cdr  

class IntCons(TypedCons['IntCons', int]):  
    pass

# Recursive bound would reject this
class BadCons(TypedCons['IntCons', str]):  
    pass  
