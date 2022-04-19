from typing import TypeVar, Type, Generic, ClassVar, Any

T = TypeVar("T", bound="Base[Any]")

class Base(Generic[T]):
    instance_list: ClassVar[list[T]]
    @classmethod
    def init(cls: Type[T]) -> None:
        cls.instance_list = []

class Derived(Base["Derived"]):
    pass

Derived.init()
print(Derived.instance_list)
