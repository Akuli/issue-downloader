# flags: --always-false=IS_WINDOWS

if IS_WINDOWS:
    import win_specific_import

def invalid_win_specific_function() -> bool:
    assert IS_WINDOWS
    return win_specific_import.some_func()  # This blows up

if IS_WINDOWS:
    def valid_win_specific_function() -> bool:
        return win_specific_import.some_func()
