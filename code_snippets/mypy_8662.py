TerminateHandlerContextType = TypedDict( "TerminateHandlerContextType",{...},)
CrashHandlerContextType = TypedDict( "CrashHandlerContextType", {... },)
QuitHandlerContextType = TypedDict("QuitHandlerContextType", {...})

TerminateHandlerType = Callable[[TerminateHandlerContextType], None]
QuitHandlerType = Callable[[QuitHandlerContextType], None]
CrashHandlerType = Callable[[CrashHandlerContextType], None]

