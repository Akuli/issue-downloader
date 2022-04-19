from typing import Generic, TypeVar

T = TypeVar("T")


class A(Generic[T]):
    class_attr: T

    @classmethod
    def set_attr(cls, arg: T) -> None:
        cls.class_attr = arg  # no error?


B = A[str]
B.set_attr("1")
B.class_attr = "1"  # error: Access to generic instance variables via class is ambiguous

C = A[int]
C.set_attr(1)
C.class_attr = 1  # error: Access to generic instance variables via class is ambiguous

value = B().class_attr

reveal_type(value)  # revealed: str, actual value: int
