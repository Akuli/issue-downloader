from typing import overload, Callable, Union, List, Set

@overload
def f(x: Callable[[str], str]) -> Set: ...

@overload
def f(x: Callable[..., str]) -> List: ...

def f(x: Callable[..., str]) -> Union[list, set]: ...  # E: Overloaded function signatures 1 and 2 overlap with incompatible return types
