def func(f: float):
    if not isinstance(f, float):
        print("hi")  # no 'unreachable code' error
        reveal_type(f)  # int | complex
