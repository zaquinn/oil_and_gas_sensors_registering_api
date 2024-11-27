from typing import Annotated

import pytest
from fastapi import Depends
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from app.main import app
from app.sensors.db.session import get_session


@pytest.fixture(name="test_db")
def test_db_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture
def client(test_db):
    def get_test_db_override():
        return test_db

    app.dependency_overrides[get_session] = get_test_db_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
