# this works and does not throw an error
class A:

    def __or__(self, v: int) -> A:...

    def __ior__(self, v: int) -> None: ...

    reveal_type(__or__)  # note: Revealed type is "def (_error.A, builtins.int) -> _error.A"
    reveal_type(__ior__)  # note: Revealed type is "def (_error.A, builtins.int)"


# this errors
class B:

    def _no(self, v: int) -> B: ...

    __or__ = _no

    def __ior__(self, v: int) -> None: ...  # error: Signatures of "__ior__" and "__or__" are incompatible

    reveal_type(__or__)  # note: Revealed type is "def (self: _error.B, v: builtins.int) -> _error.B"
    reveal_type(__ior__)  # note: Revealed type is "def (_error.B, builtins.int)"

