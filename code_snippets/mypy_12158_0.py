from typing import final

@final
class A:
    b: int

if A():
    print("hi")  # no unreachable error

print(A() and "hi")
