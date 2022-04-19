Foo = TypedDict('Foo', {
    'bar': int,
})
foo = Foo({'bar': 42})
