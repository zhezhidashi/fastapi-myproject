from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 与mysql连接
# 格式为 'mysql+pymysql://账号名:密码@ip:port/数据库名'
SQLALCHEMY_DATABASE_URI:str = 'mysql+pymysql://root:zzh12345@localhost:3306/myproject'

# 生成一个SQLAlchemy引擎
engine = create_engine(SQLALCHEMY_DATABASE_URI,pool_pre_ping=True)
# 生成sessionlocal类，这个类的每一个实例都是一个数据库的会话
# 注意命名为SessionLocal，与sqlalchemy的session分隔开
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
session = SessionLocal()

Base = declarative_base()