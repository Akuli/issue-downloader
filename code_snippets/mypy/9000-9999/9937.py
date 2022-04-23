from typing import (ClassVar, Generic, NamedTuple, Optional, Type, TypeVar,
                    Union, overload)

BoundsInt = NamedTuple("BoundsInt", [
    ("begin", int), ("end", int)])

BoundsStr = NamedTuple("BoundsStr", [
    ("begin", str), ("end", str)])

_T = TypeVar("_T", int, str)


class MyContainerBase(Generic[_T]):
    BOUND_TYPE = None  # type: ClassVar[Optional[Type[Union[BoundsInt, BoundsStr]]]]  # noqa

    def __init__(self, begin: _T, end: _T) -> None:
        assert self.BOUND_TYPE is not None
        if isinstance(begin, int) and isinstance(end, int):
            self._bounds = BoundsInt(begin, end)  # type: Union[BoundsInt, BoundsStr]  # noqa

        assert isinstance(begin, str) and isinstance(end, str)
        self._bounds = BoundsStr(begin, end)

    @overload  # type: ignore
    @property
    def bounds(
            self: 'MyContainerBase[int]'
    ) -> BoundsInt:
        ...

    @overload  # type: ignore
    @property
    def bounds(
            self: 'MyContainerBase[str]'
    ) -> BoundsStr:
        ...

    @property
    def bounds(self) -> Union[BoundsInt, BoundsStr]:
        """Return the recurrence period's bounds."""
        return self._bounds

    @overload
    def get_bounds(
            self: 'MyContainerBase[int]'
    ) -> BoundsInt:
        ...

    @overload
    def get_bounds(
            self: 'MyContainerBase[str]'
    ) -> BoundsStr:
        ...

    def get_bounds(self) -> Union[BoundsInt, BoundsStr]:
        """Return the recurrence period's bounds."""
        return self._bounds


class MyContainerInt(MyContainerBase[int]):
    BOUND_TYPE = BoundsInt


class MyContainerStr(MyContainerBase[str]):
    BOUND_TYPE = BoundsStr


def test() -> None:
    def check_to_int_bounds(bounds: BoundsInt) -> None:
        pass

    def check_to_str_bounds(bounds: BoundsStr) -> None:
        pass

    # Typechecks as expected:
    check_to_int_bounds(MyContainerInt(1, 1).bounds)
    # As expected, if uncommented, fails with:
    #   Argument 1 to "check_to_str_bounds" has incompatible type "BoundsInt";
    #   expected "BoundsStr"
    # check_to_str_bounds(MyContainerInt(1, 1).bounds)

    # Unexpectedly, if uncommented both of those fail with:
    #   Invalid self argument "MyContainerStr" to attribute
    #   function "bounds" with type "Callable[[MyContainerBase[int]],
    #   BoundsInt]"
    check_to_str_bounds(MyContainerStr("a", "b").bounds)
    # check_to_int_bounds(MyContainerStr(1.0, 1.0).bounds)

    # We do not have the above issue with the `get_bounds` method:

    # Typechecks as expected:
    check_to_int_bounds(MyContainerInt(1, 1).get_bounds())
    # As expected, if uncommented, fails.
    # check_to_str_bounds(MyContainerInt(1, 1).get_bounds())

    # Typechecks as expected:
    check_to_str_bounds(MyContainerStr("a", "b").get_bounds())
    # As expected, if uncommented, fails.
    # check_to_int_bounds(MyContainerStr(1.0, 1.0).get_bounds())
