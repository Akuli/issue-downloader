from unittest.mock import MagicMock


class Foo:
    def bar(self) -> None:
        pass


foo = Foo()
foo.bar = MagicMock()
foo.bar()
foo.bar.assert_called()
