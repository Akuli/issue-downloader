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
