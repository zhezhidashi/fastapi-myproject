# 专门用来处理用户相关的路由
from fastapi import APIRouter, Depends, HTTPException
from core.dependencies import verify_token, get_db
from mysql.connector import cursor
from models import tables, models
from utils import operation, security
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/login",
    tags=["login"],
)


# 用户登录
@router.post("/", response_model=models.Token)
async def login_for_access_token(user : models.UserLogin, db: Session = Depends(get_db)):
    result = security.authenticate_user(db, user.username, user.passwd)
    if not result:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = security.create_access_token(data={"sub": result.username})
    return {"access_token": access_token}