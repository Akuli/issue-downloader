O = TypeVar('O')

def decorator(method : Callable[[O, VarArg(), KwArg()], Any]) -> Callable[[VarArg(), O, KwArg()], Any]:
    def x(*args, **kwargs):
        return method(args[-1], *args[0:-1], **kwargs)
    return x
