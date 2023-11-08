from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    login: str
    password: str


class UserOut(BaseModel):
    id: str
    login: str
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(UserCreate):
    pass


# TODO maybe move to another file
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
