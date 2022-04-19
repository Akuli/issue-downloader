class TestExternal(unittest.TestCase):
    # TODO: Get this to work on Windows.
    # (Or don't. It is probably not a good use of time.)
    @unittest.skipIf(sys.platform.startswith("win"), "rt tests don't work on windows")
    def test_c_unit_test(self) -> None:
        """Run C unit tests in a subprocess."""
        # Build Google Test, the C++ framework we use for testing C code.
        # The source code for Google Test is copied to this repository.
        cppflags: List[str] = []
        env = os.environ.copy()
        if sys.platform == 'darwin':
            cppflags += ['-mmacosx-version-min=10.10', '-stdlib=libc++']    # passing cppflags parameter
        env['CPPFLAGS'] = ' '.join(cppflags)
