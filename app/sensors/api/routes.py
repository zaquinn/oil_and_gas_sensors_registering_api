from fastapi import APIRouter, UploadFile

from app.sensors.crud.sensor import (
    create_sensor,
    create_sensors_from_csv,
    get_sensors,
    retrive_average_value_from_equipment,
)
from app.sensors.db.session import SessionDep
from app.sensors.schemas.sensor import Sensor, SensorAverageValue, SensorCreate

router = APIRouter(
    prefix="/sensors",
    tags=["sensors"],
    responses={404: {"message": "not found"}},
)


@router.post("/", response_model=Sensor)
def register_sensor(sensor: SensorCreate, db: SessionDep):
    return create_sensor(db, sensor)


@router.post("/from-csv", response_model=list[Sensor])
async def register_sensors_from_csv(db: SessionDep, file: UploadFile):
    return await create_sensors_from_csv(db, file)


@router.get("/", response_model=list[Sensor])
def list_sensors(db: SessionDep, skip: int = 0, limit: int = 10):
    return get_sensors(db, skip=skip, limit=limit)


@router.get("/average", response_model=list[SensorAverageValue])
def list_sensors(db: SessionDep, days: int):
    return retrive_average_value_from_equipment(db, days)
