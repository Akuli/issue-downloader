class Foo:
    def __init__(self) -> None:
        self._d = {'a': 1}

    def __setattr__(self, name: str, value: Any) -> None:
        if hasattr(self, '_d'):
            self._d[name] = value
        else:
            super(self.__class__, self).__setattr__(name, value)

    @property
    def a(self) -> int:
        return self._d['a']

f = Foo()
f.a = 2
