import inspect
import mymod

inspect.signature(mymod.MyClass.method1)
# or
help(mymod.MyClass)
# correctly prints (a,b,c)
