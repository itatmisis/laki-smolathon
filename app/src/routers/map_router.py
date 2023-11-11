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


@map_router.get('/location/event', response_model=list[GetEvent])
async def route_get_all_events(current_user: UserOut = Depends(get_current_user)):
    all_events = await get_all_events()
    return all_events


@map_router.get('/location/event/{event_id}', response_model=GetEvent)
async def route_get_event_by_id(event_id: int, current_user: UserOut = Depends(get_current_user)):
    event = await get_event_by_id(event_id)
    return event


@map_router.post('/location/event')
async def route_create_events_list(event_list: list[NewEvent], current_user: UserOut = Depends(get_current_user)):
    await create_events_list(event_list)


@map_router.get('/location', response_model=list[GetLocation])
async def route_get_all_locations(current_user: UserOut = Depends(get_current_user)):
    all_location = await get_all_locations(current_user.id)
    return all_location


@map_router.get('/location/{location_id}', response_model=GetLocation)
async def route_get_location_by_id(location_id: int, current_user: UserOut = Depends(get_current_user)):
    location = await get_location_by_id(current_user.id, location_id)
    return location


@map_router.post('/location')
async def route_create_location_list(location_list: list[NewLocation]):
    await create_location_list(location_list)


@map_router.post('/location/{location_id}')
async def route_visit_location(location_id: int, current_user: UserOut = Depends(get_current_user)):
    await visit_location(current_user.id, location_id)


@map_router.get('/category')
async def route_get_all_category():
    all_category = await get_all_category()
    return all_category


@map_router.post('/category')
async def route_create_category_list(category_list: list[NewCategory]):
    await create_category_list(category_list)
