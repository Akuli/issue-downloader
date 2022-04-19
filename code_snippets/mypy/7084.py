from typing import TypeVar, Dict
  
T = TypeVar('T')
Alias = Dict[str, T]

x: Alias[T]
reveal_type(x)  # Revealed type is 'builtins.dict[builtins.str, T?]'
