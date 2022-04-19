from typing import TypeVar, Callable
T = TypeVar('T')

def test1() -> Callable[[T], T]: ...
reveal_type(test1) # Revealed type is 'def () -> def [T] (T`-1) -> T`-1'
reveal_type(test1()) # Revealed type is 'def [T] (T`-1) -> T`-1'

F = Callable[[T], T]
def test2() -> F[T]: ...
reveal_type(test2) # Revealed type is 'def [T] () -> def (T`-1) -> T`-1'
reveal_type(test2()) # Revealed type is 'def (<nothing>) -> <nothing>'
