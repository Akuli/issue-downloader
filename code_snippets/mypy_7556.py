Base = some.custom_class('Base', ...)

class Model(Base):
    ...

class Model(some.custom_class('Base', ...)):  # the hook is not called here
    ...

