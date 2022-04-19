@contextmanager
def disable_errors(self) -> None:
    self.disable_count += 1
    yield
    self.disable_count -= 1
