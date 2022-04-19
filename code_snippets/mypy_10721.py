class Cmd:
    prompt = '> '
    ...

class MyCmd(cmd.Cmd):
    @property
    def prompt(self):
        if self.some_condition():
            return '$ '
        else:
            return '> '

    @prompt.setter
    def prompt(self, value: str) -> None:
        raise NotImplementedError
    ...
