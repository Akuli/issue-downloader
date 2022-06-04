class TestDict(TypedDict):
    a: int


def myfunc(test: dict):
    print(test)


myfunc(TestDict(a=2))
