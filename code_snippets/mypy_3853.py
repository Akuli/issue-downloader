from multipledispatch import dispatch

@dispatch(int)
def foo(x: int) -> None:
    print('int')

@dispatch(str)
def foo(x: str) -> None:
    print('str')

foo(1)  # Prints 'int'.
foo('a')  # Prints 'str'.
