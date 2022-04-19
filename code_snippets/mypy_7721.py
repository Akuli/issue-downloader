# example.py
def f1(*args):
    pass


def f2(*args):
    return f1(*args)  # this is the problem statement

# example.py
def f1(*args) -> None:
    pass


def f2(*args):
    return f1(*args)

