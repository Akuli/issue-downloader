from typing import Any

class Foo:
    def foo(self, x:Any) -> bool:
        return isinstance(x, __class__)

if TYPE_CHECKING:
    __class__ : Type

