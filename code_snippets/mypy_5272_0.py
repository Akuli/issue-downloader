from pynamodb.attributes import MapAttribute, NumberAttribute
from pynamodb.models import Model

class MyMapAttribute(MapAttribute):
   foo = NumberAttribute()
   bar = NumberAttribute()

class MyModel(Model):
   my_map = MyMapAttribute()
