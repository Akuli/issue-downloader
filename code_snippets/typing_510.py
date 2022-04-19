def foo(xs: Iterable[Text]):
  return '|'.join(xs)

# list(Text) should return List[Char]
foo("abcd") # error
foo(list("abcd")) # correct, List[Char] is a special case of List[Text]

def bar(xs: Iterable[Char]):
  return '|'.join(xs)

bar("abcd") # correct, Text is a Iterable[Char]
bar(list("abcd")) # correct, List[Char] is a Iterable[Char]
bar(["ab", "cd"]) # error, List[Text] is not a Iterable[Char]

a: Char = 'a'

a[1] # error, Char cannot be indexed beyond index 0
a[0] # should be an error from type checking's PoV, Char should never be indexed
a[:] # should be an error from type checking's PoV, Char should never be copied as a slice

b: Text = 'b'
a + b # should be an error from type checking's PoV, Char and Text should be considered incompatible types
typing.cast(Text, a) + b # correct

c = a + a # correct, concatenate Char gets Text (but I'm not sure if this is reasonable though, what if we do (a + a) + a ?)
