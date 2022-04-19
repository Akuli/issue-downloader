import jwt

def generate_auth() -> str:
    return jwt.encode({}, "secret_string", algorithm="HS384")
