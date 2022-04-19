from __future__ import annotations

from typing import Protocol, TypeVar

_T0 = TypeVar("_T0")
_T0_contra = TypeVar("_T0_contra", contravariant=True)

_T1 = TypeVar("_T1")
_T1_contra = TypeVar("_T1_contra", contravariant=True)

#%%

class FP1(Protocol[_T0, _T1]):
    def __call__(self, arg0: _T0, arg1: _T1, /) -> _T0 | _T1:
        ...

def return_fp1_object_object() -> FP1[object, object]:
    def f(a: object, b: object) -> object:
        return object()

    return f

def return_fp1_float_float() -> FP1[float, float]:
    # Dangerous cast, reported.
    return return_fp1_object_object()

#%%

class FP1A(Protocol[_T0_contra, _T1_contra]):
    def __call__(self, arg0: _T0_contra, arg1: _T1_contra, /) -> _T0_contra | _T1_contra:
        ...

def return_fp1a_object_object() -> FP1A[object, object]:
    def f(a: object, b: object) -> object:
        return object()

    return f

def return_fp1a_float_float() -> FP1A[float, float]:
    # Dangerous cast, but not reported.
    return return_fp1a_object_object()

fp1a_float_float: FP1A[float, float] = return_fp1a_float_float()
result: float = fp1a_float_float(1.0, 2.0)
result += 1
