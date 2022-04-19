from mypy_extensions import TypedDict

keys = {'name': str, 'age': int, 'address': str}
Details = TypedDict('Details', keys)
DetailsSubset = TypedDict('DetailsSubset', keys, total=False)
