from datetime import datetime, timedelta
from io import BytesIO

import pandas as pd
from fastapi import HTTPException, UploadFile
from sqlmodel import Session, func, select

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


async def create_sensors_from_csv(db: Session, file: UploadFile) -> list[Sensor]:
    if file.content_type != "text/csv":
        raise HTTPException(
            status_code=400, detail="Invalid file type. Please upload a CSV file."
        )
    content = await file.read()
    df = pd.read_csv(BytesIO(content))
    sensors = []
    for _, row in df.iterrows():
        sensor_data = row.to_dict()
        print(sensor_data)
        sensor = Sensor.model_validate(sensor_data)
        db.add(sensor)
        sensors.append(sensor)

    db.commit()
    for sensor in sensors:
        db.refresh(sensor)

    return sensors


def retrive_average_value_from_equipment(db: Session, days: int) -> list[Sensor]:
    now = datetime.now()
    past_days = now - timedelta(days=days)

    statement = (
        select(
            Sensor.equipmentId,
            func.round(func.avg(Sensor.value), 2).label("average_value"),
        )
        .where(Sensor.timestamp >= past_days)
        .group_by(Sensor.equipmentId)
    )

    results = db.exec(statement)

    return results.all()
