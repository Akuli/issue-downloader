from dataclasses import dataclass

dataclass_alias = dataclass
dataclass_alias2 = dataclass(order=False)

def dataclass_wrapper(cls):
	return dataclass(cls)

@dataclass
class A: arg1: int

@dataclass_alias
class B: arg1: int

@dataclass_alias2
class C: arg1: int

@dataclass_wrapper
class D: arg1: int

a = A(arg1=1)
b = B(arg1=1)
c = C(arg1=1)
d = D(arg1=1)
