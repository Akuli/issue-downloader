
T = TypeVar("T")


class ClosedUnderFormat(Protocol[T]):
    def format(self: "ClosedUnderFormat"[T], other: "ClosedUnderFormat"[T]) -> "ClosedUnderFormat[T]":
        pass


class ClosedUnderAddition(Protocol[T]):
    def __add__(self: "ClosedUnderAddition"[T], other: "ClosedUnderAddition"[T]) -> "ClosedUnderAddition[T]":
        pass


class Bar(int):
    def format(self: int, other: int):
        return ""


def foofmt(x: ClosedUnderFormat[T], y: ClosedUnderFormat[T]) -> ClosedUnderFormat[T]:
    return x.format(y)


def fooadd(x: ClosedUnderAddition[T], y: ClosedUnderAddition[T]) -> ClosedUnderAddition[T]:
    return x.__add__(y)


def fooadd_operant(x: ClosedUnderAddition[T], y: ClosedUnderAddition[T]) -> ClosedUnderAddition[T]:
    return x + y


foofmt("foo", "foo") # ok
foofmt("foo", 10) # true positive - caught 
foofmt(Bar(10), Bar(11)) # true positive - caught

fooadd("foo", "foo") # False positive - caught but shouldn't
fooadd(10, 10) # False positive - caught but shouldn't
fooadd_operant(10, 10) # False positive - caught but shouldn't


