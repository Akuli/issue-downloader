import attr

# example 1 (works with mypy)

@attr.s(auto_attribs=True, frozen=True)
class DirectlyDecorated:
    name: str


d = DirectlyDecorated('foo')  # no mypy error



# --- end example 1

# example 2 (does not work with mypy)

my_decorator = attr.s(auto_attribs=True, frozen=True)

@my_decorator
class IndirectlyDecorated:
    name: str


i = IndirectlyDecorated('bar')  # error: Too many arguments for "IndirectlyDecorated"

# --- end example 2


# example 3 (does not work with mypy)

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        newcls = super().__new__(cls, name, bases, dct)
        newcls = my_decorator(newcls)
        return newcls


class MetaDecorated(metaclass=MyMeta):
    name: str


m = MetaDecorated('baz')  # error: Too many arguments for "MetaDecorated"

# --- end example 3
