from typing import Generic, TypeVar, TypedDict


class A(TypedDict):
    a: str


T = TypeVar("T", bound=A)


class G(Generic[T]):
    a: str

    def foo(self, t: T) -> None:
        t["a"] = "asd"
        self.a = t["a"]

    def bar(self) -> T:
        return {"a": self.a}
