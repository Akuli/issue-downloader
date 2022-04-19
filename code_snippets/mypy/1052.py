class A:
    def __setattr__(self, x, y):
        raise RuntimeError
