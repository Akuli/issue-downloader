from typing import overload, Tuple

@overload
def foo(a: int, c: bool = True) -> int: ...

@overload
def foo(a: int, b: int, *args: int, c: bool = True) -> Tuple[int, ...]: ...

def foo(a, *args, c=True):
    if len(args) == 0:
        return a
    return (a,) + args


if __name__ == '__main__':
    print(foo(1))        # 1
    print(foo(1, 2, 3))  # (1, 2, 3)
