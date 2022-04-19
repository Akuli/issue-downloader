from typing import *

T1 = TypeVar('T1')
T2 = TypeVar('T2')

T_contra = TypeVar('T_contra', contravariant=True)
T_co = TypeVar('T_co', covariant=True)

class CallbackWithArgs(Protocol[T_contra, T_co]):
  def __call__(self, __element: T_contra, *args: Any) -> T_co:
    pass

def applyit_with_args(func: CallbackWithArgs[T1, T2], y: T1) -> T2:
    return func(y)

def callback_with_args(x: str, *args: Any) -> int:
    pass

applyit_with_args(callback_with_args, 'foo')  # OK!
