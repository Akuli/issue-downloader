import inspect
import mymod

inspect.signature(mymod.MyClass.method1)
# or
help(mymod.MyClass)
# correctly prints (a,b,c)

class Myclass:
  @classmethod
  def __init__(cls, *args, **kwargs) -> None: ...
  def method1(self, *args, **kwargs) -> Any: ...
