# return_a is inferred to return str | None
def return_a(strings: list[str]):
    # No error
    return next(filter(lambda s: s.strip() == "a", strings), None)
