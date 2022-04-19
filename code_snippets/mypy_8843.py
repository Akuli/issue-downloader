from pynamodb.models import Model
from pynamodb.attributes import NumberAttribute

class MyModel(Model):
  my_number = NumberAttribute()
  my_optional_number = NumberAttribute(null=True)

reveal_type(MyModel().my_number)  # note: Revealed type is 'int'
reveal_type(MyModel().my_optional_number)  # note: Revealed type is 'Optional[int]'
