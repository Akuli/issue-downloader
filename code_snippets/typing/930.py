y: str
assert is_list_of_str(x)
assert len(x) > 0
y = x[0]

y: str
assert_is_nonempty_list_of_str(x)  # note, this encodes another runtime check, the len check
y = x[0]

def assert_is_nonempty_list_of_str(x) -> AssertingTypeGuard[list[str]]:
    if not isinstance(x, list):
        raise ExpectedListError(x)
    if not x:
        raise EmptyContainerError(x)
    if not all(isinstance(y, str) for y in x):
        raise ContainedInvalidTypeError(x, str)
    return x
