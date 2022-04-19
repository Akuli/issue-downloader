import mmap
WriteableBuffer = mmap.mmap
ReadableBuffer = bytes | WriteableBuffer

import mmap
ReadableBuffer = bytes | mmap.mmap

from mmap import mmap
WriteableBuffer = mmap
ReadableBuffer = bytes | WriteableBuffer

