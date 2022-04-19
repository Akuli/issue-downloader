from typing import Generic, TypeVar, List
  
T = TypeVar('T')

class B(Generic[T]):
    x: List[T] = []

class C1(B[int]):
    pass

class C2(B[str]):
    pass

C1().x.append(42)
C2().x.append('Hm...')
