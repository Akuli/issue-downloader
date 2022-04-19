# flags: --always-false=IS_WINDOWS
if IS_WINDOWS:
    import win_specific_import

def some_fun_broken() -> int:
    if not IS_WINDOWS:
        return 1 # checked
    # The rest of this function is analyzed even though we returned above. 

    # Blows up since `win_specific_import` isn't defined
    return win_specific_import.something()

def some_fun_fixed() -> int:
    if not IS_WINDOWS:
        return 1  # checked
    else:
        # Not analyzed because this is in the `else` part of the `if` statement
        return win_specific_import.something()  # Works
