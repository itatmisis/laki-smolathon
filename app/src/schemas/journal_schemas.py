from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class NoteOut(BaseModel):
    id: int
    id_user: int
    id_location: int
    text: str | None
    photo: str | None

    class Config:
        orm_mode = True

class NoteUpdate(BaseModel):
    text: str
    photo: str

