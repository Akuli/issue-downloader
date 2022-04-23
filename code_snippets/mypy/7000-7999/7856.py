from typing import Any, Union, Optional
from typing_extensions import Literal
from mypy_extensions import TypedDict


class Test(TypedDict):
    a: str
    b: int
    c: int


TestKeys = Literal["a", "b", "c"]  # QUESTION: is there a Test.KEYS or something equivalent?
TestValue = Union[str, int]  # QUESTION: is there a Test.VALUE_TYPES or something equivalent?


class Foo:
    def __init__(self):
        self._foo: Optional[Test] = None

    def _set(self) -> None:
        self._foo = {"a": "a", "b": 0, "c": 1}

    def __getitem__(self, key: TestKeys) -> Any:
        self._set()
        assert self._foo is not None
        return self._foo[key]

    def a(self) -> str:
        return self["a"]

    def b(self) -> int:
        return self["b"]


class Bar:
    def __init__(self):
        self._bar: Optional[Test] = None

    def _set(self) -> None:
        self._bar = {"a": "a", "b": 0, "c": 1}

    def __getitem__(self, key: TestKeys) -> TestValue:
        self._set()
        assert self._bar is not None
        return self._bar[key]

    def a(self) -> str:
        return self["a"]  # WRONG: Incompatible return value type (got "Union[str, int]", expected "str")

    def b(self) -> int:
        return self["b"]  # WRONG: Incompatible return value type (got "Union[str, int]", expected "int")


a = Foo().a()
a.find("a")

b = Foo().b()
b.find("a")  # CORRECT: "int" has no attribute "find"

c = Foo()["a"]
c.find("a")

d = Foo()["b"]
d.find("a")  # MISSING: no error reported here (if self._foo is not lazily initialized the error gets correctly reported)

e = Bar().a()
e.find("a")

f = Bar().b()
f.find("a")  # CORRECT: "int" has no attribute "find"

g = Bar()["a"]
g.find("a")  # WRONG: Item "int" of "Union[str, int]" has no attribute "find"

h = Bar()["b"]
h.find("a")  # WRONG: Item "int" of "Union[str, int]" has no attribute "find" (should be "int" has no attribute "find")

KT = TypeVar("KT", bound=TestKeys)  # or better Test.KEYS

def __getitem__(self, key: KT) -> Test[KT]:
    ...
