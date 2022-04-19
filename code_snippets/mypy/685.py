S = TypeVar("S")
T = TypeVar("T")

class Pair(Generic[S, T],
    NamedTuple("Pair",[
        ('fst', S),
        ('second', T)])):
    def show(self):
        print(self.fst, self.second)

p = Pair("ab", 22)  # type: Pair[str, int]
