from typing import Any, Generic, Optional, Type, TypeVar

T = TypeVar("T")

class customProperty(property, Generic[T]):
    def __get__(self, obj: Any, owner: Optional[Type] = None) -> T:
        return super().__get__(obj, owner)

class C:
    @customProperty
    def prop(self) -> int:
        return 1

reveal_type(C().prop)
