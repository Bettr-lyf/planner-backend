from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(input: str) -> str:
    return pwd_context.hash(input)

def verify_password(input: str, hash: str) -> bool:
    return pwd_context.verify(input, hash)

def generate_token(payload: dict):
    to_encode = payload.copy()
    to_encode['exp'] = datetime.now(timezone.utc) + timedelta(minutes=60 * 6)
    return jwt.encode(to_encode, 'secret', algorithm='HS256')
    