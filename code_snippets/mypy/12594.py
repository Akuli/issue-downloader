class A:
    def hello(self, a: str, b: str):
        pass

    world = hello

class B(A):
    # Also tried without ":A" on the self argument
    def world(self: A, a: str, b: str):
        # Do something slightly different when child-class is the instance
        pass

