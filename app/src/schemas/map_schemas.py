from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NewLocation(BaseModel):
    id_category: int
    name: str
    description: str
    address: str
    coord_x: float
    coord_y: float


class GetLocation(NewLocation):
    id: int
    has_visited: bool

    class Config:
        orm_mode = True


class NewCategory(BaseModel):
    name: str


class NewEvent(BaseModel):
    id_category: int
    name: str
    description: str
    address: str
    coord_x: float
    coord_y: float
    event_date: str
    price: str
    link: str


class GetEvent(NewEvent):
    id: int

    class Config:
        orm_mode = True
