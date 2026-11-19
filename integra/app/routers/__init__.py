# app/routers/__init__.py
from fastapi import APIRouter

from app.routers.mov_routers.py import router as mov_router

router = APIRouter
router.include_router(mov_router)