from os import makedirs

makedirs('src/core')
makedirs('src/stuff')

open('src/__init__.py', 'w').write("""
# nothing here
""")

open('src/core/__init__.py', 'w').write("""
from .run import config
""")

open('src/core/run.py', 'w').write("""
from ..stuff import somefunction

config = None

somefunction()
""")

open('src/stuff/__init__.py', 'w').write("""
from .somemore import more
from .somefunction import somefunction
""")

open('src/stuff/somefunction.py', 'w').write("""
def somefunction():
    print("Hello, World!")
""")

open('src/stuff/somemore.py', 'w').write("""
def more():
    from ..core import config
""")
