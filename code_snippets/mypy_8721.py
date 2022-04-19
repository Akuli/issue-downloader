last = None
reveal_type(last)  # Revealed type is 'None'

for val in range(10):
    reveal_type(last)  # Revealed type is 'None'

    if last is not None and last < 2:
        print("apparently unreachable")
        reveal_type(last)  # no output

    reveal_type(last)  # Revealed type is 'None'
    last = val
    reveal_type(last)  # Revealed type is 'builtins.int*'
