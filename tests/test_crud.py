from datetime import datetime

from app.sensors.crud.sensor import (
    create_sensor,
    get_sensors,
    retrive_average_value_from_equipment,
)
from app.sensors.models.sensor import Sensor


def test_create_sensor(test_db):
    sensor_data = {"equipmentId": "EQ123", "timestamp": datetime.now(), "value": 42.5}
    sensor = create_sensor(test_db, sensor_data)
    assert sensor.equipmentId == "EQ123"
    assert sensor.value == 42.5


def test_get_sensors(test_db):
    test_db.add(Sensor(equipmentId="EQ123", timestamp=datetime.now(), value=42.5))
    test_db.commit()

    sensors = get_sensors(test_db, skip=0, limit=10)
    assert len(sensors) > 0
    assert sensors[0].equipmentId == "EQ123"


def test_retrieve_average_value(test_db):
    test_db.add(Sensor(equipmentId="EQ123", timestamp=datetime.now(), value=40))
    test_db.add(Sensor(equipmentId="EQ123", timestamp=datetime.now(), value=60))
    test_db.commit()

    averages = retrive_average_value_from_equipment(test_db, days=7)
    assert len(averages) > 0
    assert averages[0].average_value == 50.0
