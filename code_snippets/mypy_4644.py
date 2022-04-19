class A(object):
    __metaclass__ = ABCMeta

    @property
    def prop(self):
        # type: () -> int
        return 1

class B(A):
    @A.prop.setter
    def prop(self, val):
        # type: (int) -> None
        pass
