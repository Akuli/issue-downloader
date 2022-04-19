if condition:
  s = get_str()
else:
  s = get_optional_str()

if condition:
  s: Optional[str] = get_str()
else:
  s = get_optional_str()

s: Optional[str]
if condition:
  s = get_str()
else:
  s = get_optional_str()

if condition:
   model = get_foo_model()  # FooModel
else:
   model = get_bar_model()  # BarModel
# model is Model

