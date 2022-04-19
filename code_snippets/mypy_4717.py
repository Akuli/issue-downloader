import abc
import typing

class FooObserver(metaclass=abc.ABCMeta):
    """Receives Foo events."""

    @abc.abstractmethod
    def on_foo(self, count: int) -> None:
        raise NotImplementedError()

class BarObserver(metaclass=abc.ABCMeta):
    """Receives Bar events."""

    @abc.abstractmethod
    def on_bar(self, status: str) -> None:
        raise NotImplementedError()

class Engine:
    def __init__(self, observers: typing.Sequence[typing.Any]) -> None:
        self.__all_observers = observers

    def do_bar(self, succeed: bool) -> None:
        status = 'ok' if succeed else 'problem'
        for bar_observer in self.__observers(BarObserver):
            bar_observer.on_bar(status)

    def do_foo(self, elements: typing.Sequence[typing.Any]) -> None:
        count = len(elements)
        for foo_observer in self.__observers(FooObserver):
            foo_observer.on_foo(count)

    __OBSERVER_TYPE = typing.TypeVar('__OBSERVER_TYPE')

    def __observers(
            self,
            observer_type: typing.Type['__OBSERVER_TYPE']
    ) -> typing.Sequence['__OBSERVER_TYPE']:
        return [observer for observer in self.__all_observers
                if isinstance(observer, observer_type)]
