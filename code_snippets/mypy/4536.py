from typing_extensions import Protocol

class Jumps(Protocol):
    def jump(self) -> int:
        pass

class Jumper1:
    @classmethod
    def jump(cls) -> int:
        print("class jumping")
        return 1

class Jumper2:
    def jump(self) -> int:
        print("instance jumping")
        return 2

def do_jump(j: Jumps):
    print(j.jump())

do_jump(Jumper1)
do_jump(Jumper2())
