from mypy_extensions import TypedDict

Details = TypedDict('Details', {'name': str, 'age': int, 'address': str})
DetailsSubset = TypedDict('DetailsSubset', {'name': str, 'age': int, 'address': str}, total=False)

from mypy_extensions import TypedDict

keys = {'name': str, 'age': int, 'address': str}
Details = TypedDict('Details', keys)
DetailsSubset = TypedDict('DetailsSubset', keys, total=False)

