from fastapi import APIRouter

from app.sensors.crud.sensor import create_sensor, get_sensors
from app.sensors.db.session import SessionDep
from app.sensors.schemas.sensor import Sensor, SensorCreate

router = APIRouter(
    prefix="/sensors",
    tags=["sensors"],
    responses={404: {"message": "not found"}},
)


@router.post("/", response_model=Sensor)
def register_sensor(sensor: SensorCreate, db: SessionDep):
    return create_sensor(db, sensor)


@router.get("/", response_model=list[Sensor])
def list_sensors(db: SessionDep, skip: int = 0, limit: int = 10):
    return get_sensors(db, skip=skip, limit=limit)
