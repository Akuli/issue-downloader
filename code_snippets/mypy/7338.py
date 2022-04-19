from typing import overload, Optional, List
  
@overload
def f(x: int) -> List[int]: ...
@overload
def f(x: None) -> List[Optional[int]]: ...

def f(x: Optional[int]) -> List[Optional[int]]:
    return [x]
