from sqlalchemy.orm import Session

from models import models, tables
from utils import security

# 获取所有用户
def get_users(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(tables.User).offset(skip).limit(limit).all()

# 创建用户
def create_users(db: Session, user: models.UserCreate):
    db_user = tables.User(
        username=user.username, 
        hashed_passwd=security.get_password_hash(user.passwd)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 创建用户时验证用户名是否存在
def check_user_exist(db, username: str):
    user = db.query(tables.User).filter(tables.User.username == username).first()
    if user:
        return True
    return False
