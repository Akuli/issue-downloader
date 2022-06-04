from __future__ import annotations
import typing as t

HeaderValue = str | list[str]
# HeaderValue = t.TypeVar("HeaderValue", str, list[str])
ResponseReturnType = tuple[str, dict[str, HeaderValue]]
ViewCallable = t.Callable[..., ResponseReturnType]
RouteCallable = t.TypeVar("RouteCallable", bound=ViewCallable)

def route() -> t.Callable[[RouteCallable], RouteCallable]:
    def wrapped(f: RouteCallable) -> RouteCallable:
        return f

    return wrapped

@route()
def view() -> tuple[str, dict[str, str]]:
    return "hello", {"content-type": "text/plain"}
