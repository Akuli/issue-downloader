from . import bar

class Foo:
    def bar(arg: bar.Spam):
        pass

class Spam:
    pass

from . import bar

def bar(arg: bar.Spam):
    pass

