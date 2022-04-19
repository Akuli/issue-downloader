from typing import Any, Callable, overload, TypeVar

T = TypeVar('T')
U = TypeVar('U')

@overload	
def tree_map(f: Callable[[U], U], tree: T) -> T:	
    ...	

@overload	
def tree_map(f: Callable[[T], U], tree: T) -> U:	
    ...	

@overload	
def tree_map(f: Callable[[Any], Any], tree: Any) -> Any:	
    ...	

def tree_map(f: Callable[[Any], Any], tree: Any) -> Any:
  pass
  

def bar(x: Any) -> str:
  return repr(x)

reveal_type(tree_map(bar, [2, 3, 4]))
