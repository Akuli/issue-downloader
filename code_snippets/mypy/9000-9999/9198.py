class ClassA:
    def attribute(self):
        return None


class ClassB:
    attribute = None

    @classmethod
    def create(cls):
        assert not issubclass(cls, ClassA)

ClassB.create()
