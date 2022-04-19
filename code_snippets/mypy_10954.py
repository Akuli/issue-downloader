# test_file.py
from collections import namedtuple

class Snapshot:
    def create_tuple_type(self, name: str):
        self.tuple_type = namedtuple(name, [])  # line 6

def create_tuple_type_1(name: str):
    x = namedtuple(name, [])                    # line 9

def create_tuple_type_2(name: str):
    return namedtuple(name, [])
