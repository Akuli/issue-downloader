from mypy_extensions import TypedDict

Details = TypedDict('Details', {'first_name': str, 'last_name': str})
DetailsSubset = TypedDict('DetailsSubset', {'first_name': str, 'last_name': str}, total=False)
defaults = {'first_name': 'John', 'last_name': 'Luther'}  # type: Details


def generate(data: DetailsSubset) -> Details:
    return {**defaults, **data}
