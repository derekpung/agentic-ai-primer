from pydantic import BaseModel


class UserInfo(BaseModel):
    sub: str
    email: str | None = None
    name: str | None = None


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
