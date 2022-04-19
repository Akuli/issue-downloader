import unittest

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.foo = 42  # "Type[Tests]" has no attribute "foo"

    def test_foo(self) -> None:
        print(self.foo)  # "Tests" has no attribute "foo"
