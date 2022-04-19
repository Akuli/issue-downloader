@puremixin
class MyMixin:
    def do_stuff(self) -> int:
        self.one_thing()  # ok, even though not defined in this class
        return self.second_thing(1)  # also ok

class Thing(Implementation[MyMixin]):
    def one_thing(self) -> None: pass  # ok
    def second_thing(self, x: int) -> str:    # error: return type not compatible with do_stuff
        return 'x'
