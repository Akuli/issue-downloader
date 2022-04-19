from typing import Generic, TypeVar

T = TypeVar("T", str, int)


class GenericSuperClass(Generic[T]):
    def __init__(self, value: T) -> None:
        # mypy complains if self.value is not annotated, for some reason
        self.value: T = value


class GenericSubClass(GenericSuperClass[T]):
    def __init__(self, value: T, flag: bool) -> None:
        super().__init__(value)
        self.flag = flag


instance = GenericSubClass("string", True)
reveal_type(instance.value)
