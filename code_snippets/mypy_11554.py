import bar

class Foo:
    def __init__(self) -> None:
        self.view_selector = object()

from foo import Foo

class ServerView:
    def __init__(self) -> None:
        print(ChannelView().userlist)
        self.view_id = str(Foo().view_selector)

class ChannelView:
    def __init__(self) -> None:
        print(ServerView().view_id)
        self.userlist = object()

