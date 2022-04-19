from xmlrpc.server import SimpleXMLRPCRequestHandler, SimpleXMLRPCServer


def forty_two() -> int:
    return 42


def echo_int(value: int) -> int:
    return value


class EchoInt(object):
    def __call__(self, value: int) -> int:
        return value


def main() -> None:
    xml_rpc_server = SimpleXMLRPCServer(
        ('0.0.0.0', 8080), requestHandler=SimpleXMLRPCRequestHandler, allow_none=True
    )
    xml_rpc_server.register_function(forty_two)
    xml_rpc_server.register_function(echo_int)
    xml_rpc_server.register_function(EchoInt)
