def create_from_typeddict(d: Type[TypedDict]): ...


_TD = TypeVar("_TD", bound=TypedDict)
class Application(Generic[_TD]):
    state: _TD
