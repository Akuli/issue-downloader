if random() > 0.5:
    import mod1
else:
    import mod2 as mod1

try:
    import fastmath
except ImportError:
    import math as fastmath
