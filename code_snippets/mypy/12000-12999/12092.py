def return_a(strings: list[str]) -> Optional[str]:
    # Item "None" of "Optional[str]" has no attribute "strip"
    return next(filter(lambda s: s.strip() == "a", strings), None)

def matches_a(s: str) -> bool:
    return s.strip() == "a"

def return_a(strings: list[str]) -> Optional[str]:
    # Argument 1 to "filter" has incompatible type "Callable[[str], Any]"; expected "Callable[[Optional[str]], Any]"
    return next(filter(matches_a, strings), None)

# return_a is inferred to return str | None
def return_a(strings: list[str]):
    # No error
    return next(filter(lambda s: s.strip() == "a", strings), None)
