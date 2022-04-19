import os
import typing as t
T = t.TypeVar('T')
R = t.TypeVar('R')

class flatmap(t.Generic[T, R]):

  def __init__(self, func: t.Callable[[T], R]) -> None:
    self.func = func

  def __ror__(self, value: t.Optional[T]) -> t.Optional[R]:
    if value is not None:
      return self.func(value)
    return None

# error: Cannot infer type argument 1 of "flatmap"
# error: "object" has no attribute "upper"
print(os.getenv('VARNAME') | flatmap(lambda m: m.upper()))
print(os.getenv('VARNAME') | flatmap(str.upper))  # ok

# 1)
os.getenv('VARNAME') | flatmap(lambda m: m.upper())

# 2)
flatmap(os.getenv('VARNAME'), lambda m: m.upper())

# 1)
email = maybe_get_user() | flatmap(lambda user: user.email) | flatmap(sanitize_email_address)

# 2)
email = flatmap(flatmap(maybe_get_user(), lambda user: user.email), sanitize_email_address)

# 3)
user = maybe_get_user()
email = sanitize_email_address(user.email) if user and user.email else None

