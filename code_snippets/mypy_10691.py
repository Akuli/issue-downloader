from typing import Union, TypeVar, overload

class C1:...
class C2:...

T = TypeVar('T', bound=Union[C1, C2])

@overload
def update(elt: C1) -> C1:...

@overload
def update(elt:C2) -> C2:...

def update(elt: Union[C1, C2]) -> Union[C1, C2]:
  pass

def get_copy(elt: T) -> T:
  new_elt = update(elt)
  return new_elt
