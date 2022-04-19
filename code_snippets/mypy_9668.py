from typing import Any, Awaitable, Callable, Protocol, Union, TypeVar, Generic


class IRequest:
    pass


KleinSynchronousRenderable = Union[str, bytes]
KleinRenderable = Union[
    KleinSynchronousRenderable, Awaitable[KleinSynchronousRenderable]
]


T_co = TypeVar('T_co', contravariant=True)

class KleinRoute(Protocol[T_co]):
    def __call__(v, /, self: T_co, request: IRequest) -> KleinRenderable:
        """
        Function that, when decorated by L{Klein.route}, handles a Klein
        request.
        """


class Klein(Generic[T_co]):
    def route(self, url: str, *args: Any, **kwargs: Any) -> Callable[[KleinRoute[T_co]], KleinRoute[T_co]]:
        """
        Decorator for endpoint routing.
        """


class Application:
    klein: Klein[Application] = Klein()

    @klein.route("/foo")
    def foo(self, resource: IRequest) -> KleinRenderable:
        pass
