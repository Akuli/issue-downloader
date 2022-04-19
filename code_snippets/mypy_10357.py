import http.server
import threading
from typing import Optional, Type


class ThreadedHttpServer:
    def __init__(
        self,
        host: str,
        port: int,
        custom_server: Type["CustomServer"],
        custom_attribute: str,
    ) -> None:
        self.host = host
        self.port = port
        self.custom_server = custom_server
        self.custom_server.CUSTOM_ATTRIBUTE = custom_attribute

        self.httpd = http.server.HTTPServer((self.host, self.port), self.custom_server)
        self.t = threading.Thread(target=self.httpd.serve_forever)

    def start(self) -> "ThreadedHttpServer":
        self.t.start()

        return self

    def shutdown(self) -> None:

        self.httpd.shutdown()
        self.t.join()


class CustomServer(http.server.BaseHTTPRequestHandler):
    CUSTOM_ATTRIBUTE = Optional[str]

    def do_POST(self) -> None:
        pass
