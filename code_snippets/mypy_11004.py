from typing import Any, Callable, Generic, overload, Optional, TypeVar, Tuple, Union

Row = TypeVar("Row")

class Connection(Generic[Row]):
    @overload
    def connect(
        self, *, row_factory: Callable[[], Row], **kwargs: Union[None, int, str]
    ) -> "Connection[Row]":
        ...

    @overload
    def connect(
        self, **kwargs: Union[None, int, str],
    ) -> "Connection[Tuple[Any, ...]]":
        ...

    def connect(
        self, *, row_factory: Optional[Callable[[], Row]] = None, **kwargs: Any,
    ) -> "Connection[Any]":
        raise NotImplementedError
