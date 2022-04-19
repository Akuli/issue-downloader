def divide(a: int, b: int) -> int | NoReturn[ZeroDivisionError]:
    return a // b


def main():
    res = divide(5, 4)
    total = 5 + res  # mypy will complain here because NoReturn type can't be using with integer
    print(total)
