import mock
import typing


class Foo:
    def bar(self, a: int) -> str:
        return str(a)


# I want to pass a spec'd mock here (mock.create_autospec(spec=Foo)).
def test_something(foo: Foo):
    # I'd like to find a way for this to be accepted by mypy.
    # error: "Callable[[int], str]" has no attribute "return_value"
    foo.bar.return_value = "42"


# This can be resolved arduously by writing a custom protocol for each mock.
class BarMockProtocol(typing.Protocol):
    return_value: str

    def __call__(self, a: int) -> str:
        pass

    # def assert_called():
    #     ...
    # And so on...


class FooMockProtocol(typing.Protocol):
    bar: BarMockProtocol


def test_something_else(foo: FooMockProtocol):
    # Error as expected.
    # error: Incompatible types in assignment (expression has type "int", variable has type "str")
    foo.bar.return_value = 42

    # No error as expected.
    foo.bar.return_value = "42"


# This is what I'd suggest
def test_something_else_yet(foo: mock.Mock[Foo]):
    # Error
    foo.bar.return_value = 42
    # No error
    foo.bar.return_value = "42"


# Usage sample
foo_mock = mock.create_autospec(spec=Foo)
test_something_else_yet(foo_mock)
