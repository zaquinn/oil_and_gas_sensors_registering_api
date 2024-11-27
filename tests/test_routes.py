from io import BytesIO

from fastapi import UploadFile
from fastapi.testclient import TestClient


def test_register_sensor(client: TestClient):
    payload = {
        "equipmentId": "EQ123",
        "timestamp": "2023-02-16T01:30:00.000-06:00",
        "value": 42.5,
    }
    response = client.post("/api/sensors/", json=payload)
    assert response.status_code == 200
    assert response.json()["equipmentId"] == "EQ123"


def test_register_sensors_from_csv(client: TestClient):
    csv_content = b"equipmentId,timestamp,value\nEQ123,2024-11-26T12:00:00,42.5"
    file = UploadFile(
        filename="test.csv",
        file=BytesIO(csv_content),
        headers={"content-type": "text/csv"},
    )
    response = client.post(
        "/api/sensors/from-csv",
        files={"file": (file.filename, file.file, file.content_type)},
    )
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["equipmentId"] == "EQ123"


def test_list_sensors(client: TestClient):
    response = client.get("/api/sensors/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_list_average(client: TestClient):
    response = client.get("/api/sensors/average?days=7")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
