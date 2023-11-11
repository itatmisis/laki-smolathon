from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    login: str
    password: str
    first_name: str
    last_name: str


class UserUpdate(BaseModel):
    login: str | None = None
    password: str | None = None
    first_name: str | None = None
    last_name: str | None = None


class UserOut(BaseModel):
    id: str
    login: str
    first_name: str
    last_name: str
    created_at: datetime

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
