from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder

from src.schemas.user_schemas import *
from src.services.user_service import *
from src.services.auth_utils import get_current_user
from requests import post
import json

user_router = APIRouter(
    tags=['User'],
    prefix='/user'
)


@user_router.get('/me', response_model=UserOut)
async def route_get_user(current_user: UserOut = Depends(get_current_user)):
    return current_user


@user_router.post('/me')
async def route_update_user(user_update: UserUpdate, current_user: UserOut = Depends(get_current_user)):
    await update_user(current_user.id, user_update.login, user_update.password, user_update.first_name, user_update.last_name)
