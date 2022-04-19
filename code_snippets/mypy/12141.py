import os

for component in os.uname():
    print(component.encode())
