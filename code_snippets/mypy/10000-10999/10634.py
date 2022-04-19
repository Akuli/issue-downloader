foo = None

def bar() -> str:
    global foo
    if foo is not None:
        print("Hello")
    else:
        foo = "bar"
        return "lol"
