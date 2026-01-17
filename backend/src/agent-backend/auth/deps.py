import jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from auth.config import auth_config

bearer = HTTPBearer(auto_error=False)


def get_current_user(
    creds: HTTPAuthorizationCredentials = Depends(bearer),
    cookie_token: str | None = None,
):
    token = None
    if creds and creds.scheme.lower() == "bearer":
        token = creds.credentials
    elif cookie_token:
        token = cookie_token

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token"
        )

    try:
        payload = jwt.decode(
            token,
            auth_config.APP_JWT_SECRET,
            algorithms=["HS256"],
            audience=auth_config.APP_JWT_AUDIENCE,
            issuer=auth_config.APP_JWT_ISSUER,
        )
        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
