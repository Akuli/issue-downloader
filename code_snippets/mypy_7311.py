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

from typing import *

T1 = TypeVar('T1')
T2 = TypeVar('T2')

T_contra = TypeVar('T_contra', contravariant=True)
T_co = TypeVar('T_co', covariant=True)

class CallbackWithKwargs(Protocol[T_contra, T_co]):
  def __call__(self, __element: T_contra, **kwargs: Any) -> T_co:
    pass

def applyit_with_kwargs(func: CallbackWithKwargs[T1, T2], y: T1) -> T2:
    return func(y)

def callback_with_kwargs(x: str, **kwargs: Any) -> int:
    pass

# Argument 1 to "applyit_with_kwargs" has incompatible type "Callable[[str, KwArg(Any)], int]"; expected "CallbackWithKwargs[str, <nothing>]"
applyit_with_kwargs(callback_with_kwargs, 'foo')  # Error!
