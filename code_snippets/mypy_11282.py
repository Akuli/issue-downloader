def divide(a: int, b: int) -> int | NoReturn[ZeroDivisionError]:
    return a // b


def main():
    res = divide(5, 4)
    total = 5 + res  # mypy will complain here because NoReturn type can't be using with integer
    print(total)

def build_error(error_type: str) -> UnauthorizedApiError | NotFoundApiError | NoReturn[RuntimeError, NotFound]: ...

def handler():
    try:
        result = f()  # some function with Union[str, NoResult] return type
        ...  # in all lines in the try block Mypy could safely assume that result will be str
    except Exception as exc:
        ...  # here I'm not sure, but at least we could assume the type of exc variable? In case we've got a few other functions that could raise an exception in a try block, this could be a union of all NoResults in try block for which this exception is an ancestor.

def get_index(l: list, i: int) -> Any | NoResult:  # this kind of NoResult means that we don't know the actual error, shortcut for NoResult[Exception]
    # with type: unwrap instruction Mypy will not complain about this line
    return l[i]  # type: unwrap

