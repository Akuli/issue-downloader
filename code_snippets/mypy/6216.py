import sys

class A:
    def f(self) -> None:
        if sys.platform == 'xxx':
            import bad  # Error


def g() -> None:
    if sys.platform == 'xxx':
        import bad2  # No error
