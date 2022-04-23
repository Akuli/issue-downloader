from pynamodb.attributes import MapAttribute, NumberAttribute
from pynamodb.models import Model

class MyMapAttribute(MapAttribute):
   foo = NumberAttribute()
   bar = NumberAttribute()

class MyModel(Model):
   my_map = MyMapAttribute()

class MapAttribute(...):
    @overload
    def __get__(self: _MT, instance: Model, owner: Any) -> Tagged[_MT, "instance"]: ...
    @overload
    def __get__(self: _MT, instance: Type[Model], owner: Any) -> Tagged[_MT, "class"]: ...

class NumberAttribute(...):
    @overload
    def __get__(self, instance: Model, owner: Any) -> float: ...
    @overload
    def __get__(self, instance: Type[Model], owner: Any) -> NumberAttribute: ...
    @overload
    def __get__(self, instance: Tagged[MapAttribute, "instance"], owner: Any) -> float: ...
    @overload
    def __get__(self, instance: Tagged[MapAttribute, "class"], owner: Any) -> float: ...
