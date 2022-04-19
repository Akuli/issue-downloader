class A(object):
    @staticmethod
    def open():
        return 123
    @staticmethod
    def proccess():
        return 456

    switch = {
        1: open.__func__,
        2: proccess.__func__,   
    }
