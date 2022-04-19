from functools import singledispatch
import typing as tp

@singledispatch
def f(x: tp.Any) -> None: pass

@f.register
def _f_list(x: list[int]) -> None: pass

if __name__ == '__main__':
    f([1, 2, 3])
