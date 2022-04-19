def hook_func(ctx: AttributeContext) -> Type:
    ...

class MyPlugin(Plugin):
    def get_attribute_hook(self, fullname: str) -> ...:
        return hook_func
