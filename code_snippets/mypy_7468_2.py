isinstance(Left(1), Left)  # should typecheck, currently doesn't
isinstance(Left(1), Left[int])  # Parameterized generics cannot be ...
