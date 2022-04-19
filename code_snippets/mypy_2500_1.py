class A:
    a = 1

    def f(self) -> None:
        self.a = ''   # The current message is probably just fine, as the context is clear
