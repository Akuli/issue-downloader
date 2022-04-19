import typing as tp


T = tp.TypeVar("T")


@tp.overload
def gf1(i: int, j: tp.Any) -> str:
    ...


@tp.overload
def gf1(i: tp.Iterable[T], j: bool) -> tp.Dict[T, T]:
    ...


def gf1(i: tp.Union[int, tp.Iterable[T]], j: tp.Any) -> tp.Union[str, tp.Dict[T, T]]:
    pass


gf1.resultType = lambda *a: None



class C(tp.Generic[T]):
    def f1(self) -> gf1.resultType(T, bool):
        pass

    def f2(self) -> gf1.resultType(tp.List[T], bool):
        pass


if not tp.TYPE_CHECKING:
    def reveal_type(x):
        pass


# outputs: builtins.str
reveal_type(gf1(1, True))
# wanted: builtins.str
reveal_type(C[int]().f1())

# outputs: builtins.dict[builtins.int*, builtins.int*]
reveal_type(gf1([1], True))
# wanted: builtins.dict[builtins.int*, builtins.int*]
reveal_type(C[int]().f2())
