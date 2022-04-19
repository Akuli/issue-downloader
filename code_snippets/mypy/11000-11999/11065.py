from multipledispatch import dispatch


@dispatch(list, str)
def concatenate(a: list, b: str):
    a.append(b)
    return a


@dispatch(str, str)
def concatenate(a: str, b: str):
    return a + b


@dispatch(str, int)
def concatenate(a: str, b: int):
    return a + str(b)


@dispatch(int, str)
def concatenate(a: int, b: str):
    return str(a) + b


print(concatenate(["a", "b"], "c"))
# ['a', 'b', 'c']
print(concatenate("Hello", "World"))
# HelloWorld
print(concatenate("a", 1))
# a1
print(concatenate(2, "b"))
# 2b
