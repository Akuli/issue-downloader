class A:
    pass

class B:
    pass

class C:
    pass

class D:
    pass

@overload
def f(x: A) -> C:...

@overload
def f(x: B) -> D:...

def f(x: Union[A, B]) -> Union[C, D]:
    if isinstance(x, A):
        return C()
    else:
        return D()

@overload
def g(x: A, func: Callable[[C], bool]) -> None:...

@overload
def g(x: B, func: Callable[[D], bool]) -> None:...

def g(x: Union[A, B], func: Union[Callable[[C], bool], Callable[[D], bool]]) -> None:
    obj = f(x)
    func(obj) # error: Argument 1 has incompatible type "Union[C, D]"; expected "C"
