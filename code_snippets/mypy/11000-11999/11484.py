from pydantic import BaseModel

BaseModelT = TypeVar('BaseModelT', bound=BaseModel)

class UserActions(Generic[BaseModelT]):
    async def create(
        self,
        data: 'UserCreateInput',
    ) -> BaseModelT:
        ...
    ...
