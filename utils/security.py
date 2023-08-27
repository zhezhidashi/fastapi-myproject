from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from passlib.context import CryptContext
from models import tables
from datetime import datetime, timedelta


# openssl rand -hex 32
SECRET_KEY = "fe10f78d5adf6bae931daab736dcb61ca8887b2fed42d6df5b7b03557e3d591c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 验证密码
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 由明文密码生成密文密码
def get_password_hash(password):
    return pwd_context.hash(password)

# 验证用户
def authenticate_user(db, username: str, password: str):
    user = db.query(tables.User).filter(tables.User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_passwd):
        return False
    return user

# 生成token
def create_access_token(data: dict, expires_delta: int = ACCESS_TOKEN_EXPIRE_DAYS):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
