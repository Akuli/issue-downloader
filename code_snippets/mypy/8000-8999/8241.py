from typing import overload, Callable, Union, List, Set

@overload
def f(x: Callable[[str], str]) -> Set: ...

@overload
def f(x: Callable[..., str]) -> List: ...

def f(x: Callable[..., str]) -> Union[list, set]: ...  # E: Overloaded function signatures 1 and 2 overlap with incompatible return types

def g(a: str) -> str: ...

reveal_type(f(g))  # N: Revealed type is 'Set[Any]'

def h(a: str, b: int) -> str: ...

reveal_type(f(g))  # N: Revealed type is 'List[Any]'

def m(a: str, *b: int) -> str: ...

reveal_type(f(m))  # N: Revealed type is 'Set[Any]'

def n(a: str, **b: int) -> str: ...

reveal_type(f(n))  # N: Revealed type is 'Set[Any]'
