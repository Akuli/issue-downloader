from typing import Sequence, Union, Tuple, List, Iterable, Collection, Optional, TypeVar, TypedDict


class _FieldOpts(TypedDict, total=True):
    fields: Sequence[Union[str, Sequence[str]]]


a: Sequence[Union[str, Sequence[str]]] = ("name",)
b: Tuple[Optional[str], _FieldOpts] = (None, {"fields": ("name",)})
c: Sequence[Tuple[Optional[str], _FieldOpts]] = [(None, {"fields": ("name",)})]
# E: Incompatible types in assignment (expression has type "Tuple[Tuple[None, Dict[str, Tuple[str]]]]", variable has type "Sequence[Tuple[Optional[str], _FieldOpts]]")
d: Sequence[Tuple[Optional[str], _FieldOpts]] = ((None, {"fields": ("name",)}),)
# E: Incompatible types in assignment (expression has type "Tuple[Tuple[Dict[str, Tuple[str]]]]", variable has type "Sequence[Tuple[_FieldOpts]]")
e: Sequence[Tuple[_FieldOpts]] = (({"fields": ("name",)},),)
f: Tuple[_FieldOpts] = ({"fields": ("name",)},)
g: List[Tuple[_FieldOpts]] = [({"fields": ("name",)},)]
h: Tuple[Tuple[_FieldOpts], ...] = (({"fields": ("name",)},),)
# E: Incompatible types in assignment (expression has type "Tuple[Tuple[Dict[str, Tuple[str]]]]", variable has type "Collection[Tuple[_FieldOpts]]")
i: Collection[Tuple[_FieldOpts]] = (({"fields": ("name",)},),)
# E: Incompatible types in assignment (expression has type "Tuple[Tuple[Dict[str, Tuple[str]]]]", variable has type "Iterable[Tuple[_FieldOpts]]")
j: Iterable[Tuple[_FieldOpts]] = (({"fields": ("name",)},),)
k: Iterable[Tuple[_FieldOpts]] = [({"fields": ("name",)},)]
# E: Incompatible types in assignment (expression has type "Tuple[Tuple[Dict[str, Tuple[str]]], Tuple[Dict[str, Tuple[str]]]]", variable has type "Iterable[Tuple[_FieldOpts]]")
m: Iterable[Tuple[_FieldOpts]] = (({"fields": ("name",)},), ({"fields": ("name",)},))

T = TypeVar("T")
ListOrTuple = Union[Tuple[T, ...], List[T]]
n: ListOrTuple[Tuple[_FieldOpts]] = (({"fields": ("name",)},),)
