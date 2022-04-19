from typing import Type

def f(x: Type[int]) -> None:
    if isinstance(x, Type):  # Argument 2 to "isinstance" has incompatible type "object"; 
                             # expected "Union[type, Tuple[Union[type, Tuple[Any, ...]], ...]]"
        pass
