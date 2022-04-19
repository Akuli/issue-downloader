# test_case.py
from typing import Protocol, overload, runtime_checkable
@runtime_checkable
class PowableProto(Protocol):
    @overload
    def __pow__(self, other: "PowableProto") -> "PowableProto":
        ...
    @overload
    def __pow__(self, other: "PowableProto", modulo: "PowableProto") -> "PowableProto":  # <- fine
        ...
    @overload
    def __rpow__(self, other: "PowableProto") -> "PowableProto":
        ...
    @overload
    def __rpow__(self, other: "PowableProto", modulo: "PowableProto") -> "PowableProto":  # <- this (of all things) breaks
        ...
    @overload
    def __rpOw__(self, other: "PowableProto") -> "PowableProto":
        ...
    @overload
    def __rpOw__(self, other: "PowableProto", modulo: "PowableProto") -> "PowableProto":  # <- fine
        ...
