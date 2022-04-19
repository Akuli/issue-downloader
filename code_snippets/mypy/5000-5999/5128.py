def foo() -> None:
    message = 'test'
    raise Exception(message) if message else Exception  # -> mypy error


def bar() -> None:
    raise Exception  # ok


def baz() -> None:
    message = 'test'
    raise Exception(message)  # ok


def qux() -> None:
    message = 'test'
    raise Exception if not message else Exception(message)  # -> mypy error


if __name__ == '__main__':
    foo()
