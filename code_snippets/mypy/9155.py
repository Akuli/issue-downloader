from typing import TypeVar, Generic, List, Sequence

T = TypeVar('T')
I = TypeVar('I')

class B(Generic[T]):
  def __init__(self, t: T, a: Sequence[I], c: Sequence[I]):
    self.t = t
    self.b: Sequence[object] = [*a, *c]

c = B[int]     (15, ['a'], ['b', 'c']) # mypy rejects this
b = B[int, str](15, ['a'], ['b', 'c']) # and accepts this

d: B[int]      # mypy correctly accepts it here
e: B[int, str] # and rejects this
