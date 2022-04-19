def foo() -> None:
    global myglobal
    myglobal = 2  # error: Name 'myglobal' is not defined
