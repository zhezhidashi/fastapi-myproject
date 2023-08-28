from fastapi import Header, HTTPException, Depends
from core.database import SessionLocal, engine
from jose import JWTError, jwt
from utils.security import SECRET_KEY, ALGORITHM

async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_token(token: str):
    credentials_exception = HTTPException(
        status_code=400, detail="Could not validate credentials"
    )
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise credentials_exception
    return True

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()