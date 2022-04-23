class A:
    a = 1

class B(A):
    a = ''  # Show that 'a' was defined in 'A' (in addition to the current message)

class C(A): pass

c = C()
c.a = ''   # Again, maybe show that 'a' was defined in 'A'

class A:
    a = 1

    def f(self) -> None:
        self.a = ''   # The current message is probably just fine, as the context is clear
