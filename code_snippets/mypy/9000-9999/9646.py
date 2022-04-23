FOO = "foo"

import constants

def bar():
    # type: () -> str
    print("{foo}".format(foo=constants.FOO))
    return "{constants.FOO}".format(constants=constants)
