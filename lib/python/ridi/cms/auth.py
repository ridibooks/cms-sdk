from ridi.cms.cf_jwt_validator import CFJwtValidator
from ridi.cms.config import Config
from ridi.cms.cms_client import AdminAuth
from ridi.cms.thrift.Errors.ttypes import *

COOKIE_CMS_TOKEN = 'CF_Authorization'

def introspectJwt(token: str, config: Config) -> dict:
    if not token:
        raise NoTokenException()

    jwt = CFJwtValidator()
    key = jwt.getPublicKey(config.AUTH_URL)
    payload = jwt.decode(token, key, config.CF_AUDIENCE_TAG)
    if not payload:
        raise UnauthorizedException()

    return payload

def authenticate(token: str, config: Config) -> str:
    payload = introspectJwt(token, config)
    id = payload['email'].split('@')[0]
    return id

def authorizeByTag(admin_auth: AdminAuth, tags: list) -> bool:
    return admin_auth.authorizeByTag('', tags)
