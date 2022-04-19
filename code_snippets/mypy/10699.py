from __future__ import annotations

import abc
from typing import Literal, Mapping, overload


class AdapterBase(abc.ABC):
    @overload
    def get_map_or_value(self, *, as_dict: Literal[True]) -> Mapping[str, str]:
        ...

    @overload
    def get_map_or_value(self, *, as_dict: Literal[False] = ...) -> str:
        ...

    @overload
    def get_map_or_value(self, *, as_dict: bool = ...) -> Mapping[str, str] | str:
        ...

    @abc.abstractmethod
    def get_map_or_value(self, *, as_dict: bool = False) -> Mapping[str, str] | str:
        raise NotImplementedError


class ConcreteAdapter1(AdapterBase):
    # fails strict no-untyped-def checks
    def get_map_or_value(self, *, as_dict):
        if as_dict:
            return {"somekey": "somevalue"}
        return "somevalue"


class ConcreteAdapter2(AdapterBase):
    # Signature of "get_map_or_value" incompatible with supertype "AdapterBase" [override]
    def get_map_or_value(self, *, as_dict: bool = False) -> Mapping[str, str] | str:
        if as_dict:
            return {"someOtherKey": "someOtherValue"}
        return "someOtherValue"


class DoSomethingElse:
    def __init__(self, adapter: AdapterBase) -> None:
        # needs to know about function names, parameters, and return types
        self.adapter = adapter
