funclist = [lambda x: print(1)]
funclist += [lambda k: print(2)]  # incompatible signature, but type not widened and no error
reveal_type(funclist)  # builtins.list[def (x: Any)]
funclist[1](x=4)  # this will error at runtime because of a typing mistake
