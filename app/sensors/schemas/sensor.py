from datetime import datetime
from decimal import Decimal
from typing import ClassVar

from pydantic import ConfigDict
from sqlmodel import Field, SQLModel


class SensorBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    equipmentId: str
    timestamp: datetime
    value: Decimal = Field(decimal_places=2)


class SensorCreate(SensorBase):
    pass


class SensorAverageValue(SQLModel):
    equipmentId: str
    average_value: Decimal = Field(decimal_places=2)


class Sensor(SensorBase):
    Config: ClassVar[ConfigDict] = ConfigDict(from_attributes=True)
