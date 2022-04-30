from pathlib import Path
import subprocess
import time

# no type error
code_1 = '''
from typing import Any
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
'''

# incorrect return type
code_2 = '''
from typing import Any
def fib(n: int) -> str:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
'''

# changed return type to Any, should not error
code_3 = '''
from typing import Any
def fib(n: int) -> Any:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
'''

# this should be the dmypy path in the current virtual env
dmypy_path = '/home/jiayi/Projects/SPOT/.venv/bin/dmypy'

check_dir = Path("temp/type_check")
check_dir.mkdir(exist_ok=True, parents=True)
with open(check_dir / "code.py", "w") as f:
    f.write(code_1)
subprocess.run(['python', dmypy_path, 'restart', '--', '--follow-imports=skip'],cwd=check_dir)

print('---checking code_1---')
subprocess.run(['python', dmypy_path, 'check', '.'],cwd=check_dir)

with open(check_dir / "code.py", "w") as f:
    f.write(code_2)
print('---checking code_2---')
subprocess.run(['python', dmypy_path, 'recheck', "--update", "code.py"],cwd=check_dir)

with open(check_dir / "code.py", "w") as f:
    f.write(code_3)
print('---checking code_3---')
subprocess.run(['python', dmypy_path, 'recheck', "--update", "code.py"],cwd=check_dir)
print("test finished.")

print('---wait and check code_3 again---')
time.sleep(1.0)  # will not work if waiting time is shorter
with open(check_dir / "code.py", "w") as f:  # need this rewriting
    f.write(code_3)
subprocess.run(['python', dmypy_path, 'recheck', "--update", "code.py"],cwd=check_dir)
print("test finished.")
