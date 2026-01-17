from authlib.integrations.starlette_client import OAuth
from auth.config import auth_config

oauth = OAuth()

oauth.register(
    name="keycloak",
    client_id=auth_config.KEYCLOAK_CLIENT_ID,
    client_secret=auth_config.KEYCLOAK_CLIENT_SECRET,
    server_metadata_url=f"{auth_config.KEYCLOAK_BASE}/realms/{auth_config.KEYCLOAK_REALM}/.well-known/openid-configuration",
    client_kwargs={"scope": "openid profile email"},
)
