from sqlmodel import Session, select

from app.sensors.models.sensor import Sensor
from app.sensors.schemas.sensor import SensorCreate


def create_sensor(db: Session, sensor_data: SensorCreate) -> Sensor:

    sensor = Sensor.model_validate(sensor_data)
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor


def get_sensors(db: Session, skip: int = 0, limit: int = 10) -> list[Sensor]:

    statement = select(Sensor).offset(skip).limit(limit)
    results = db.exec(statement)
    return results.all()


# todo: implement or remove this
def get_sensor_by_id(db: Session, equipment_id: str, timestamp: str) -> Sensor | None:

    statement = select(Sensor).where(
        Sensor.equipmentId == equipment_id, Sensor.timestamp == timestamp
    )
    result = db.exec(statement).first()
    return result
