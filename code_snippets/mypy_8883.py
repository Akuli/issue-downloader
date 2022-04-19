class _AuthParamsPassword(TypedDict):
    grant_type: Literal["password"]
    email: str
    password: str
class _AuthParamsRefresh(TypedDict):
    grant_type: Literal["refresh_token"]
    refresh_token: str
AuthParams = Union[_AuthParamsPassword, _AuthParamsRefresh]

class _TokenParamsPassword(TypedDict):
    grant_type: Literal["password"]
    client_id: str
    client_secret: str
    email: str
    password: str
class _TokenParamsRefresh(TypedDict):
    grant_type: Literal["refresh_token"]
    client_id: str
    client_secret: str
    refresh_token: str
TokenParams = Union[_TokenParamsPassword, _TokenParamsRefresh]
