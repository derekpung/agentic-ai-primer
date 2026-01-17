import datetime
import jwt
from auth.config import auth_config


def create_jwt(payload: dict) -> str:
    payload.update(
        {
            "iss": auth_config.APP_JWT_ISSUER,
            "aud": auth_config.APP_JWT_AUDIENCE,
            "exp": datetime.datetime.now(datetime.timezone.utc)
            + datetime.timedelta(minutes=auth_config.APP_JWT_EXPIRE_MIN),
        }
    )
    return jwt.encode(payload, auth_config.APP_JWT_SECRET, algorithm="HS256")


def verify_jwt(token: str) -> dict:
    return jwt.decode(
        token,
        auth_config.APP_JWT_SECRET,
        algorithms=["HS256"],
        audience=auth_config.APP_JWT_AUDIENCE,
        issuer=auth_config.APP_JWT_ISSUER,
    )
