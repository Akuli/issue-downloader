import uuid
class Bar:
    uuid: uuid.UUID = uuid.uuid4()
reveal_type(Bar().uuid)
