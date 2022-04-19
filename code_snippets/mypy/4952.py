from typing import *

class A(object):
    def method(self) -> str:
        return ''

R = TypeVar('R')

class B(object):
    def func(self, instance: A, instance_type: Type[R]) -> None:
        reveal_type(instance)
        if isinstance(instance, instance_type):
            reveal_type(instance)
            instance.method()
