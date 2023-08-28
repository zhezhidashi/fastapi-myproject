# 专门用来处理用户相关的路由
from fastapi import APIRouter, Depends, HTTPException
from core.dependencies import verify_token, get_db
from mysql.connector import cursor
from models import tables, models
from utils import operation, security
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(verify_token)],
)

# 得到所有用户
@router.get("/get-users", response_model=List[models.User])
async def read_users(db: Session = Depends(get_db)):
    users = operation.get_users(db)
    return users

# 添加一个用户
@router.post("/add-user", response_model=models.User)
async def add_users(user: models.UserCreate, db: Session = Depends(get_db)):
    if(operation.check_user_exist(db, user.username)):
        raise HTTPException(status_code=400, detail="username " + user.username + " already exists"
    )
    return operation.create_users(db, user)

# 删除一个用户
@router.post("/delete-user", response_model=models.User)
async def delete_users(user: models.UserDelete, db: Session = Depends(get_db)):
    if(not operation.check_user_exist(db, user.username)):
        raise HTTPException(status_code=400, detail="username " + user.username + " not exists"
    )
    return operation.delete_users(db, user)