from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), unique=True, index=True)
    hashed_passwd = Column(String(256))

    
