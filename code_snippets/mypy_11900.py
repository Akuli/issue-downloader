def foo() -> None:
    user = None

    while True:
        if user is None:
            user = 123
        else:
            print(1 + "lol")

foo()
