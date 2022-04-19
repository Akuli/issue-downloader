import ctypes

Quaternion = ctypes.c_int * 4
Pair = Quaternion * 2

quat = Quaternion(1, 2, 3, 4)
p = Pair((1, 2, 3, 4), (2, 3, 4, 5))
