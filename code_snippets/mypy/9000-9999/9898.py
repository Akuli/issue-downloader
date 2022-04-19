import typing as t

T = t.TypeVar('T', covariant=True)
Y = t.TypeVar('Y')


class Nothing(t.Generic[T]):
    def chain_none(self: 'Nothing[t.Optional[Y]]') -> 'Nothing[Y]':
        return self  # type: ignore


class Just(t.Generic[T]):
    def __init__(self, val: T) -> None:
        self._value = val

    def chain_none(
            self: 'Just[t.Optional[Y]]') -> t.Union[Nothing[Y], 'Just[Y]']:
        if self._value is None:
            return Nothing()
        return Just(self._value)


val: t.Union[Nothing[t.Union[None, int, str]], Just[t.Union[None, int, str]]]
reveal_type(val.chain_none())
