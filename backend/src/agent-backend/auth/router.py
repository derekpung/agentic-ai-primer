from fastapi import APIRouter, Request, Response, Depends
from fastapi.responses import RedirectResponse
from auth.oauth import oauth
from auth.jwt import create_jwt
from auth.config import auth_config
from auth.deps import get_current_user
import os

router = APIRouter()


@router.get("/me")
def me(request: Request, user=Depends(get_current_user)):
    return {"user": user}


@router.get("/login")
async def login(request: Request):
    redirect_uri = auth_config.KEYCLOAK_CALLBACK_URL
    return await oauth.keycloak.authorize_redirect(request, redirect_uri)


@router.get("/callback")
async def callback(request: Request):
    REDIRECT_URL = os.getenv("REDIRECT_URL", "")

    token = await oauth.keycloak.authorize_access_token(request)
    userinfo = token.get("userinfo") or {}
    app_jwt = create_jwt(userinfo)

    resp = RedirectResponse(url=f"{REDIRECT_URL}")
    resp.set_cookie(
        key="app_token",
        value=app_jwt,
        httponly=True,
        secure=False,  # set True in production
        samesite="lax",
        max_age=auth_config.APP_JWT_EXPIRE_MIN * 60,
        path="/",
    )
    return resp


@router.post("/logout")
def logout():
    resp = Response(status_code=204)
    resp.delete_cookie("app_token", path="/")
    return resp
