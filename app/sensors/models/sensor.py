from datetime import datetime
from decimal import Decimal

from sqlmodel import Field, SQLModel


class Sensor(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    equipmentId: str
    timestamp: datetime
    value: Decimal = Field(decimal_places=2)
