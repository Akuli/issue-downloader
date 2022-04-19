# simple function which the author doesn't realize can consume a single string
# count_starts_lowercase("some string") should fail
def count_starts_lowercase(x: Sequence[str]) -> int:
    return len([c for c in x if c[0] in string.ascii_lowercase])

# function with overloaded definitions based on str/Sequence[str]
# the following definition should work
@typing.overload
def poly_getlen(value: str) -> int: ...
@typing.overload
def poly_getlen(value: Sequence[str]) -> List[int]: ...
def poly_getlen(value: Union[str, Sequence[str]]) -> Union[int, List[int]]:
    if isinstance(value, str):
        return len(value)
    return [len(x) for x in value]

# a sequence of unions containing str should be carefully considered
# ideally `count_terminal_digit_is_0("00011101")` would fail
# if this adds too much complexity, it can be allowed
def count_terminal_digit_is_0(x: Sequence[Union[str, int]]) -> int:
    terminal_digits = [(n % 10 if isinstance(n, int) else n[-1]) for n in x]
    return len([d for d in terminal_digits if d in (0, "0")])
