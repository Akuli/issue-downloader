class Foo:
    @classmethod
    @property
    def bar(cls) -> str:
        return cls.__name__ 


def foo_bar(msg: str) -> None:
    print(msg)

foo_bar(Foo.bar)
