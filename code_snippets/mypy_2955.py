import signal
import sys
signal.signal(signal.SIGTERM, lambda signum, stack: sys.exit(1))
