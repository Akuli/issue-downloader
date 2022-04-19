vals = [1, 2, 3]
operation(vals)
print(vals)  # What is vals here?

def operation(vals: Sequence[int]) -> None:
    assert isinstance(vals, list)
    vals += [3, 4, 5]

