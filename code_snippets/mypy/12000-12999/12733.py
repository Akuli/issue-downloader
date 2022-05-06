@overload
def foo(cls: type[dict], mapping: SupportsKeysAndGetItem[K, V], /) -> dict[K, V]: ...
@overload
def foo(cls: type[dict], mapping: SupportsKeysAndGetItem[str, V], /, **kwargs: V) -> dict[str, V]: ...

class FrozendictBase(Generic[K, V]):
    @overload
    def __new__(
            cls,
            mapping: SupportsKeysAndGetItem[K, V],
            /,
            ) -> 'FrozendictBase[K, V]': ...

    @overload
    def __new__(
            cls,
            mapping: SupportsKeysAndGetItem[str, V],
            /,
            **kwargs: V,
            ) -> 'FrozendictBase[str, V]': ...
