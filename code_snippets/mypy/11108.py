class Spam(TypedDict):
    one: str

x = Spam(one='one')
Spam(**x)
