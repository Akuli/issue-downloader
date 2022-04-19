T = TypeVar("T")
A_no_T = TypeVar(
    "A_no_T",
    bound="A[None]",
)


class A(
    Generic[T],
):

    @overload
    def method(
        self: A_no_T,
    ) -> None:
        pass

    @overload
    def method(
        self,
        t: T,
    ) -> None:
        pass

    def method(
        self,
        t: Optional[T] = None,
    ) -> None:
        return


class B(A[int]):

    def method(
        self,
        t: int,
    ) -> None:
        pass
