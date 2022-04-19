from typing import List

class SampleClass:
    an_attribute: int

foo: List[SampleClass] = []

bar = map(lambda an_instance: an_instance.an_attribute, foo)
