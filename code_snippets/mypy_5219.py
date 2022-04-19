class A: pass
class B(A): pass
class C(A): pass

x = [B(), C()]  # Inferrred type List[A], not List[Union[B, C]]
y: List[Union[B, C]]
y = [B(), C()]  # Now the type is List[Union[B, C]]
