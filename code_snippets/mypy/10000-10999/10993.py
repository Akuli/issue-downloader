f: int | str

if isinstance(f, int):
    # error: Unsupported operand types for + ("str" and "int")
    # even though there's no chance the value could be a string here since the lambda is immediately invoked
    (lambda: f+1)()

    # no error, even though the lambda could get called later when the type changes
    asdf = lambda: f + 1
