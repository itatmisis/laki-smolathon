from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder

from src.schemas.user_schemas import *
from src.services.user_service import *
from src.services.auth_utils import get_current_user
from requests import post
import json

auth_router = APIRouter(
    tags=['auth']
)


@auth_router.post('/registration', response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def route_registration(user_reg: UserCreate):
    new_user = await registration_user(user_reg.login, user_reg.password, user_reg.first_name, user_reg.last_name)
    return new_user


@auth_router.post('/login', response_model=Token)
async def route_login(login_form: OAuth2PasswordRequestForm = Depends()):
    user_data = await login_user(login_form.username, login_form.password)
    return user_data
