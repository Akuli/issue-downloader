def fake_union(name: str, types: Tuple[Types, ...]) -> Union[Types]:
    ...

UserErrors = (A, B)

Response = fake_union(types=(User, *UserErrors), name="Response")

def union_hook(ctx: DynamicClassDefContext) -> None:
    types_expr = ctx.call.args[ctx.call.arg_names.index("types")]

    assert isinstance(types_expr, TupleExpr)

    for type_ in types_expr.items:
        if isinstance(type_, StarExpr):
            assert isinstance(type_.expr, NameExpr)
            name = type_.expr.name

            # how can I find the value of this expr?
            print(name)
