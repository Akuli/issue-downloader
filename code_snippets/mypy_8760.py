from typing import Any
  
def foo(**kwargs: Any) -> None: ...

foo(bar=reveal_type([1])) # Revealed type is List[Any]
