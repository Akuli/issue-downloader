def hook_func(ctx: AttributeContext) -> Type:
    ...

class MyPlugin(Plugin):
    def get_attribute_hook(self, fullname: str) -> ...:
        return hook_func

def hook_gen(name: str):
    def hook_func(ctx: AttributeContext) -> Type:
        ...
    return hook_func

class MyPlugin(Plugin):
    def get_attribute_hook(self, fullname: str) -> ...:
        return hook_gen(fullname)

