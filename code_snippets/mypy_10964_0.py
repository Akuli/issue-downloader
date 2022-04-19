from typing import Any, TYPE_CHECKING, overload

class _IntDescriptorMeta(type):
    def __get__(self, instance: Any, owner: Any) -> int:
        return 123

class IntDescriptorClass(metaclass=_IntDescriptorMeta):
    ...

class IntDescriptor:
    def __get__(self, instance: Any, owner: Any) -> int:
        return 123

class X:
    number_cls = IntDescriptorClass
    number = IntDescriptor()

print(X.number_cls)
print(X().number_cls)
print(X.number)
print(X().number)

if TYPE_CHECKING:
    reveal_type(X.number_cls)
    reveal_type(X().number_cls)
    reveal_type(X.number)
    reveal_type(X().number)
