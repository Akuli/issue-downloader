import subprocess

class MyPopen(subprocess.Popen):

    def __init__(self) -> None:
        args = ['echo', 'test']
        super().__init__(
            args=args,
        )
