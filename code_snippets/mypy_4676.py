_SysExcInfoType = Union[Tuple[type, BaseException, TracebackType],
                        Tuple[None, None, None]]
if sys.version_info >= (3, 5):
    _ExcInfoType = Union[None, bool, _SysExcInfoType, BaseException]
else:
    _ExcInfoType = Union[None, bool, _SysExcInfoType]

def log(self,
                lvl: int, msg: Text, *args: Any, exc_info: _ExcInfoType = ...,
                extra: Optional[Dict[str, Any]] = ..., **kwargs: Any) -> None: ...
