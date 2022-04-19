class _SessionData(TypedDict):
    created: int
    session: Dict[str, Any]


class _EmptyDict(TypedDict):
    """Empty dict for typing."""


SessionData = Union[_SessionData, _EmptyDict]

data: SessionData

reveal_type(data)
a = data if data else None
reveal_type(a)
