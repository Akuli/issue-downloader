a: str = "foo"
print(a)  # value needs to be used before redefinition
a: int  # but it is really still str
if a > 1:
    ...
