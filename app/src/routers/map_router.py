from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder

from src.schemas.user_schemas import UserOut
from src.schemas.map_schemas import *
from src.services.map_service import *
from src.services.auth_utils import get_current_user
from requests import post
import json

map_router = APIRouter(
    tags=['Map'],
    prefix='/map'
)

@map_router.get('/location')
async def route_get_all_locations():
    all_location = await get_all_locations()
    return all_location


@map_router.get('/location/{location_id}', response_model=GetLocation)
async def route_get_location_by_id(location_id: int):
    location = await get_location_by_id(location_id)
    return location


@map_router.post('/location')
async def route_create_location_list(location_list: list[NewLocation]):
    await create_location_list(location_list)


@map_router.post('/category')
async def route_create_category_list(category_list: list[NewCategory]):
    await create_category_list(category_list)


@map_router.post('/location/{location_id}')
async def route_visit_location(location_id: int, current_user: UserOut = Depends(get_current_user)):
    await visit_location(current_user.id, location_id)
