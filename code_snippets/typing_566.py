from datetime import date
x: AnyOf[str, date] = ...
s: str = x  # ok
dt: date = x  # ok
i: int = x  # type error
u: Union[str, bytes] = x  # ok
x = u  # type error (although the type checker could do something smart here and infer that u can only be str here)
