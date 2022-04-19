from typing import Iterable, TYPE_CHECKING, TypeVar

_TC = TypeVar('_TC', int, float, complex)


def f1(arg: Iterable[complex]) -> complex:
    if TYPE_CHECKING:

        reveal_type(f2(arg))                # Revealed type is 'builtins.complex' Ok.
        reveal_type(1/f2(arg))              # Revealed type is 'builtins.complex' Ok.
        reveal_type(1*f2(arg))              # Revealed type is 'builtins.complex' Ok.

        reveal_type(sum(arg))               # Revealed type is 'builtins.complex*' <- What does mean '*' at the end?

        reveal_type(1/sum(arg))             # Revealed type is 'builtins.float' ???
                                            # Argument 1 to "sum" has incompatible type "Iterable[complex]"; expected "Iterable[int]" ???

        reveal_type(1*sum(arg))             # Revealed type is 'builtins.int' ???
                                            # Argument 1 to "sum" has incompatible type "Iterable[complex]"; expected "Iterable[int]" ???

        reveal_type(1.0/sum(arg))           # Revealed type is 'builtins.float' ???
                                            # Argument 1 to "sum" has incompatible type "Iterable[complex]"; expected "Iterable[float]" ???

        reveal_type(1.0*sum(arg))           # Revealed type is 'builtins.float' ???
                                            # Argument 1 to "sum" has incompatible type "Iterable[complex]"; expected "Iterable[float]" ???

        reveal_type(1/sum(arg, start=complex(0.0)))  # Revealed type is 'builtins.float' ???
                                            # Argument 1 to "sum" has incompatible type "Iterable[complex]"; expected "Iterable[int]" ???

        reveal_type(complex(1)/sum(arg))    # Revealed type is 'builtins.complex' <- workaround
        reveal_type(1/complex(sum(arg)))    # Revealed type is 'builtins.complex' <- workaround

    return 1/sum(arg)                       # error: Argument 1 to "sum" has incompatible type "Iterable[complex]"; expected "Iterable[int]"


def f2(arg: Iterable[_TC]) -> _TC:
    return 1/next(iter(arg))


if __name__ == '__main__':

    a = [1.0, 2.0+3.0j]
    print(f1(a))
