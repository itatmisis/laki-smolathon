from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NoteOut(BaseModel):
    id: int
    id_user: int
    id_location: int
    text: str | None
    photo: str | None
    marked_at: datetime

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.timestamp(),
        }

class NoteUpdate(BaseModel):
    text: str | None
    photo: str | None
