_TypeT = TypeVar("_TypeT", bound=type)
_Reduce = Union[Tuple[Callable[..., _TypeT], Tuple[Any, ...]], Tuple[Callable[..., _TypeT], Tuple[Any, ...], Optional[Any]]]

# ...

dispatch_table: dict[type, Callable[[type], str | _Reduce[type]]]  # undocumented

import copyreg
import pickle


class Foo:
    __slots__ = ("contained_dict",)

    def __init__(self, argv_tuples):
        self.contained_dict = dict(argv_tuples)

    def __repr__(self):
        return f"Foo({repr(list(self.items()))})"

    def items(self):
        return self.contained_dict.items()


class MyPickler(pickle.Pickler):
    dispatch_table = copyreg.dispatch_table.copy()
    dispatch_table[Foo] = lambda myval: (Foo, (tuple(myval.items()),))


if __name__ == "__main__":
    a = Foo([("a", "b"), ("c", "d")])
    b = pickle.loads(pickle.dumps(a))
    print(repr(a))
    print(repr(b))
