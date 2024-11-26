from fastapi import APIRouter

from app.sensors.api.routes import router as sensors_router

api_router = APIRouter()
api_router.include_router(sensors_router)
