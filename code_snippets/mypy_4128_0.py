from mypy_extensions import TypedDict

Details = TypedDict('Details', {'name': str, 'age': int, 'address': str})
DetailsSubset = TypedDict('DetailsSubset', {'name': str, 'age': int, 'address': str}, total=False)
