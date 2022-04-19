def func1(f: float):
    reveal_type(f)  # float | int | complex

def func2(b: bytes):
    reveal_type(b)  # bytes | bytearray | memoryview

def func3(u: unicode):  # python 2 moment
    reveal_type(u)  # unicode | str

def func(f: float):
    f.is_integer()  # error: int has no member "is_integer"

def func(f: float):
    if not isinstance(f, float):
        print("hi")  # no 'unreachable code' error
        reveal_type(f)  # int | complex
