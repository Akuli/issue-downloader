from __future__ import annotations

from typing import Protocol, TypeVar

_T0 = TypeVar("_T0")
_T0_co = TypeVar("_T0_co", covariant=True)

_T1 = TypeVar("_T1")
_T1_co = TypeVar("_T1_co", covariant=True)

#%%

class FP0(Protocol[_T0, _T1]):
    def __call__(self, arg0: _T0 | _T1, /) -> tuple[_T0, _T1]:
        ...

def return_fp0_float_float() -> FP0[float, float]:
    def f(x: float) -> tuple[float, float]:
        x += 1
        return (0, 0)

    return f

def return_fp0_object_object() -> FP0[object, object]:
    # Dangerous cast, reported.
    return return_fp0_float_float()

#%%

class FP0A(Protocol[_T0_co, _T1_co]):
    def __call__(self, arg0: _T0_co | _T1_co, /) -> tuple[_T0_co, _T1_co]:
        ...

def return_fp0a_float_float() -> FP0A[float, float]:
    def f(x: float) -> tuple[float, float]:
        x += 1
        return (0, 0)

    return f

def return_fp0a_object_object() -> FP0A[object, object]:
    # Dangerous cast, but not reported.
    return return_fp0a_float_float()

fp0a_object_object: FP0A[object, object] = return_fp0a_object_object()
_ = fp0a_object_object(object())
