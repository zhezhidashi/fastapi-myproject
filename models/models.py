from typing import List, Optional

from pydantic import BaseModel

# 用户相关
class UserBase(BaseModel):
    username: str

# 创建用户
class UserCreate(UserBase):
    passwd: str

# 登录用户
class UserLogin(UserBase):
    passwd: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

# Token相关
class Token(BaseModel):
    access_token: str
