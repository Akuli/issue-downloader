# test.py
from typing import NamedTuple

ExampleClass = NamedTuple('ExampleClass', test_id=str, timestamp=str)

ExampleClass = NamedTuple('ExampleClass', [(test_id, str), (timestamp, str)])

