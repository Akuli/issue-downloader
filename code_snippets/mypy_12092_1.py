def matches_a(s: str) -> bool:
    return s.strip() == "a"

def return_a(strings: list[str]) -> Optional[str]:
    # Argument 1 to "filter" has incompatible type "Callable[[str], Any]"; expected "Callable[[Optional[str]], Any]"
    return next(filter(matches_a, strings), None)
