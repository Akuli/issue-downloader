a = foo(None)  # error: No overload variant of "foo" matches argument type "None"

reveal_type(a)  # note: Revealed type is "Any"
print(a)
bar(a)
a + "asdf"
