import socket
import sys

print(sys.platform)
s = socket.socket(socket.AF_NETLINK, socket.SOCK_RAW, socket.NETLINK_ROUTE)
print(s)

