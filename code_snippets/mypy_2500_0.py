class A:
    a = 1

class B(A):
    a = ''  # Show that 'a' was defined in 'A' (in addition to the current message)

class C(A): pass

c = C()
c.a = ''   # Again, maybe show that 'a' was defined in 'A'
