from typing import *

T1 = TypeVar('T1')
T2 = TypeVar('T2')

T_contra = TypeVar('T_contra', contravariant=True)
T_co = TypeVar('T_co', covariant=True)

class Callback(Protocol[T_contra, T_co]):
  def __call__(self, __element: T_contra) -> T_co:
    pass

def applyit(func: Callback[T1, T2], y: T1) -> T2:
    return func(y)

def callback(x: str) -> int:
    pass

applyit(callback, 'foo')  # OK!
