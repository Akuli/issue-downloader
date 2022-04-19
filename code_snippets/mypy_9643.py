import io

class MyStringIO(io.StringIO):
    def readline(self, size=None) -> str:
        return super().readline(size)
