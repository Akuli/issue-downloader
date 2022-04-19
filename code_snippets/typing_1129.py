class TypingFeatures:
  PARAMSPEC_SUPPORTED = ...
  VARIADIC_SUPPORTED = ...
  LITERAL_STRING_SUPPORTED = ...

if TypingFeatures.PARAMSPEC_SUPPORTED:
  def contextmanager(func: Callable[_P, Iterator[_T]]) -> Callable[_P, ContextManager[_T]]: ...
else:
  def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., ContextManager[_T]]: ...

alias1 = int | str

alias1 = Union[int, str]

if TypingFeatures.UNION_OPERATOR:
  alias1 = int | str
else:
  alias1 = Union[int, str]
