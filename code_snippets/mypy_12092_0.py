def return_a(strings: list[str]) -> Optional[str]:
    # Item "None" of "Optional[str]" has no attribute "strip"
    return next(filter(lambda s: s.strip() == "a", strings), None)
