Thing1 = TypeVar("Thing1", bound=Base1, covariant=True)
Thing2 = TypeVar("Thing2", bound=Base2, covariant=True)
Thing3 = TypeVar("Thing3", bound=Base3, covariant=True)


class ThingWithLotsOfGenerics(Generic[Thing1, Thing2, Thing3]):
    ...


def foo(value: ThingWithLotsOfGenerics[..., ..., ...]) -> None:
    ...
