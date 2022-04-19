from enum import Enum
from typing import NamedTuple

class T(NamedTuple):
  class State(Enum):
    A =1
  state:State

print(T.State.A)
print(T(state=T.State.A))
