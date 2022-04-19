from mmap import mmap
WriteableBuffer = mmap
ReadableBuffer = bytes | WriteableBuffer
