from contextlib import ExitStack

def context_manager_with_return_bug() -> int:
    with ExitStack() as stack:
        return 5
