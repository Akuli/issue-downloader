
S = TypeVar('S', bound='Spec')
from __future__ import annotations
from typing import TypeVar, Type, overload, Generic

S = TypeVar("S", bound='Spec')

class Spec:
    def __init__(self, name):
        self.name = name

    @overload
    def __get__(self: S, obj: None, typ: Type[Service[S]]) -> S: ...
    @overload
    def __get__(self: S, obj: Service[S], typ: Type[Service[S]]) -> Service[S]: ...

    def __get__(self, obj, typ):
        if obj is None:
            self
        else:
            service.push(S)
            return obj.service

class Int(Spec):
    pass

class String(Spec):
    pass

class Service(Generic[S]):
    def push(self, S):
        ...

class IntService(Service[Int]):
    a = Int('a')
    b = Int('b')
    c = String('c')  # offending descriptor: obj in __get__ will be a Service[Int], but Service[String] is expected for String

def usage(ints: IntService):
    ints.a
    ints.c  # only this line will cause a typing issue and it has no indication to the offending definition 4 lines abouve
