@runtime_checkable
class Adapter(Protocol):
    interrupt: bool

    def __init__(self, device: Device) -> None:
        ...

    async def run_forever(self) -> None:
        ...

class ComposedAdapter:
    _interpreter: Interpreter
    _server: Server
    interrupt: bool = False

    def __init__(self, device: Device) -> None:
        assert isinstance(self._interpreter, Interpreter)
        assert isinstance(self._server, Server)
        self._device = device

    async def run_forever(self) -> None:
        async for interrupt in self._server.run_forever(
            lambda message: self._interpreter.handle(self, message) # Error raised here
        ):
            self.interrupt |= interrupt

