noop_ctxmgr = contextmanager(lambda: (yield))

@contextmanager
def noop_ctxmgr():
    yield

