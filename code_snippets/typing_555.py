from datetime import datetime
from mypy_extensions import TypedDict
from somewhere import AliasWithMetadata

# define metadata type
Options = TypedDict('Options', {'min': int, 'max': int})
# define type alias with allowed metadata
MinMaxInt = AliasWithMetadata(int, Options)

# define age arg as type int with metadata attached
def get_rough_birth_year(age: MinMaxInt(min=0, max=120)):
    return datetime.today().year - age

# call function with int without mypy complaining
get_rough_birth_year(105)
