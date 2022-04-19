from typing import Any, Dict, Optional, Sequence, Tuple

class BaseClass(object):
    def __init__(self, foo: str, *args: Sequence[Any], **kwargs: Dict[str, Any]) -> None:
        self.foo = foo
        super().__init__(*args, **kwargs)

class Mixin(object):
    def __init__(self, bar: str, baz: Optional[str]=None, *args: Sequence[Any], **kwargs: Dict[str, Any]) -> None:
        self.bar = bar
        self.baz = baz or 'baz2'
        super().__init__(*args, **kwargs)

class Derived(BaseClass, Mixin):
    def __init__(self, foo: str, bar: str, other: str, *args: Sequence[Any], **kwargs: Dict[str, Any]) -> None:
        self.other = other
        super().__init__(foo=foo, bar=bar, *args, **kwargs)

d = Derived('foo', 'bar', 'other')

print(d.foo)
print(d.bar)
print(d.other)
print(d.baz)
