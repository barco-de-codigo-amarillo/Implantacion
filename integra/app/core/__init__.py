from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
from app.core.config import DEBUG

Base = declarative_base()

app = FastAPI(title="API Integración", debug=DEBUG)

from app.routers.mov_routers import router as mov_router

app.include_router(mov_router)