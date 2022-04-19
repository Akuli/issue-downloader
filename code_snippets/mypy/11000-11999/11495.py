from dataclasses import dataclass

@dataclass(unsafe_hash=False, eq=True, frozen=False)
class SecondCase2:
    x: int
    __hash__: None  # E: Incompatible types in assignment (expression has type "None", base class "object" defined the type as "Callable[[object], int]")
print(SecondCase2(1).__hash__)  # N: Revealed type is "None" \
                                                      # E: Missing positional argument "__hash__" in call to "SecondCase2"
