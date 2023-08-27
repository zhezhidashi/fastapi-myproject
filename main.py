from fastapi import Depends, FastAPI

from routers import users, login
from core.database import Base, engine

# database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My Project",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="1.0.0",
)

# 导入路由
app.include_router(users.router)
app.include_router(login.router)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}
