class A:
    @classmethod
    def hi(cls):
        pass

    bye = classmethod(hi.__func__)
