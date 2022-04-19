class Parent:
    # No error if there's no type hint in the constructor (type unimportant)
    def __init__(self, args: int):
        # The next line succeeds if it's a tuple, but fails on list.
        self.var_a = []
        # The type of this variable doesn't seem to matter at all, but it needs
        # to exist and be trying to set a property.
        self.var_b = None

    # This needs to be a property, but the getter doesn't affect anything.
    var_b = property(fset=lambda self, value: None)


class Child(Parent):
    @property  # Error reported on this line.
    def var_a(self):
        return self._var_a

    @var_a.setter
    def var_a(self, value):
        self._var_a = []
