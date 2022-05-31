@dataclass
class MyModel:
   id: uuid
   name: str
   hostname: str
   memory_size: int

# bad names
Magic = SubsetTypedDict(MyModel, exclude=["id"], total=False)

def wait_for_update(model_or_id: Model|uuid, **kw: Magic) -> Model:
   ...
