
T = TypeVar("T")

@singledispatch
def my_fun(
    val: T,
) -> List[T]:
    return list(val)

my_fun(5)
my_fun("Ĝis la revido!")
