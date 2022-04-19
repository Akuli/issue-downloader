import mmap
WriteableBuffer = mmap.mmap
ReadableBuffer = bytes | WriteableBuffer
