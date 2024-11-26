from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import api_router
from app.sensors.db.session import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(title="Oil and Gas Sensor API", lifespan=lifespan)

app.include_router(api_router, prefix="/api")
