class Foo:
    print(__doc__)
    print(__name__)
    print(__qualname__)  # error: Name '__qualname__' is not defined
    print(__module__)  # error: Name '__module__' is not defined
