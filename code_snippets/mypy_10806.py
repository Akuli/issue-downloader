a: object = None

def foo() -> None:
    global a
    a = None
    bar()
    if a:
        print("hi")

def bar() -> None:
    global a
    a = 1
