django.db.models.fields.CharField[Union[builtins.str, builtins.int, django.db.models.expressions.Combinable], builtins.str]

def make_queryset_repr_return_only_one_type():
    from mypy.types import TypeStrVisitor

    old_visit_instance = TypeStrVisitor.visit_instance

    def patched_visit_instance(self, t: Instance) -> str:
        if t.type.has_base(helpers.QUERYSET_CLASS_FULLNAME):
            return old_visit_instance(self, helpers.reparametrize_instance(t, [t.args[0]]))
        else:
            return old_visit_instance(self, t)

    TypeStrVisitor.visit_instance = patched_visit_instance

