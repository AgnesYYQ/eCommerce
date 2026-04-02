import os
import jwt
import requests
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

COGNITO_REGION = os.getenv("COGNITO_REGION", "us-east-1")
COGNITO_USERPOOL_ID = os.getenv("COGNITO_USERPOOL_ID", "us-east-1_XXXXXX")
COGNITO_APP_CLIENT_ID = os.getenv("COGNITO_APP_CLIENT_ID", "clientid")
JWKS_URL = f"https://cognito-idp.{COGNITO_REGION}.amazonaws.com/{COGNITO_USERPOOL_ID}/.well-known/jwks.json"

bearer_scheme = HTTPBearer()

_jwks = None
def get_jwks():
    global _jwks
    if not _jwks:
        _jwks = requests.get(JWKS_URL).json()
    return _jwks

def verify_jwt(token: str):
    jwks = get_jwks()
    headers = jwt.get_unverified_header(token)
    key = next((k for k in jwks["keys"] if k["kid"] == headers["kid"]), None)
    if not key:
        raise HTTPException(status_code=401, detail="Invalid JWT")
    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
    try:
        payload = jwt.decode(token, public_key, algorithms=[headers["alg"]], audience=COGNITO_APP_CLIENT_ID)
        return payload
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid JWT")

def cognito_auth(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    return verify_jwt(credentials.credentials)
