def add_non_ext_class_attr(builder: IRBuilder,
                           non_ext: NonExtClassInfo,
                           lvalue: NameExpr,
                           stmt: AssignmentStmt,
                           cdef: ClassDef,
                           attr_to_cache: List[Tuple[Lvalue, RType]]) -> None:
    """Add a class attribute to __annotations__ of a non-extension class.

    If the attribute is initialized with a value, also add it to __dict__.
    """
    # We populate __annotations__ because dataclasses uses it to determine
    # which attributes to compute on.
    # TODO: Maybe generate more precise types for annotations
    key = builder.load_str(lvalue.name)
    typ = builder.add(LoadAddress(type_object_op.type, type_object_op.src, stmt.line))
    builder.call_c(dict_set_item_op, [non_ext.anns, key, typ], stmt.line)
