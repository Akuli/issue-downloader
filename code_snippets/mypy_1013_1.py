def f(a: A) -> None:
    a.f(x=1)  # Failure if a is an instance of B

f(B())
