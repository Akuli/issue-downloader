class Column:
    def mean(self) -> int:
        return 0


class GeoColumn(Column):
    def length(self) -> int:
        return 0


T = TypeVar("T", bound=Dict[str, Column])

K = TypeVar("K", bound=str)
V = TypeVar("V", bound=Column)


class Dataframe(Generic[T]):
    def __init__(self, cols: T):
        self.cols = cols

    def __getattr__(self: Dataframe[TypedDict({K: V})], name: K) -> V:
        return self.cols[name]


d = Dataframe({"name": Column(), "location": GeoColumn()})

d.name.mean()
d.location.length()

T = TypeVar("T", bound=Dict[str, Column])

K = TypeVar("K", bound=KeyOf[T])


class Dataframe(Generic[T]):
    def __init__(self, cols: T):
        self.cols = cols

    def __getattr__(self, name: K) -> GetItem[T, K]:
        return self.cols[name]
