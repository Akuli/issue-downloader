import typing as t
T = t.TypeVar('T')
V = t.TypeVar('V')
def test(key: T, value: V):
  values: t.Dict[T, V] = {}
  print(values.pop(key, None))  # ok
  values.pop(key, value)        # ok
  values.pop(key, None)         # error: Argument 2 to "pop" of "MutableMapping" has incompatible type "None"; expected "V"
  values.pop(key, 42)           # error: Argument 2 to "pop" of "MutableMapping" has incompatible type "int"; expected "V"

class MutableMapping(Mapping[_KT, _VT], Generic[_KT, _VT]):
    # ....
    @overload
    def pop(self, key: _KT, default: Union[_VT, _T] = ...) -> Union[_VT, _T]: ...

