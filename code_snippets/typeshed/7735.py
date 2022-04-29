V = t.TypeVar("V")

def sync_do_sum(
    environment: "Environment",
    iterable: "t.Iterable[V]",
    attribute: t.Optional[t.Union[str, int]] = None,
    start: V = 0,  # type: ignore
) -> V:
    if attribute is not None:
        iterable = map(make_attrgetter(environment, attribute), iterable)

    return sum(iterable, start)  # type: ignore[no-any-return, call-overload]
