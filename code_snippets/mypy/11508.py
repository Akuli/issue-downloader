from typing import Generic, Mapping, NoReturn, Sequence, TypeVar

T = TypeVar("T", contravariant=True)


class Foo(Generic[T]):
    ...


foo = Foo[int]()
bar = Foo[str]()

a1: Sequence[Foo[NoReturn]] = [foo]  # no error
a2: Sequence[Foo[NoReturn]] = [bar]  # no error

# error (this one seemed to be fixed around commit 32448b88370f8327c390f4e21666065c87ca95e2, then broken again)
a3: Sequence[Foo[NoReturn]] = [foo, bar]

a4: Sequence[Foo[NoReturn]] = [foo] or [bar]  # error

a5: Mapping[str, Sequence[Foo[NoReturn]]] = {  # error
    "foo": [foo],
    "bar": [],  # error goes away if you change this to [foo]
}

a6: Sequence[Sequence[Foo[NoReturn]]] = [[foo], []]  # error
