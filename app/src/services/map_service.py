from fastapi import HTTPException, status
import requests

from src.database.db import async_session
import src.database.map_db as db
import src.services.auth_utils as auth
from src.schemas.map_schemas import NewLocation, NewCategory

# from src.database.models.models import Users, Locations


async def get_all_locations():
    all_location = []
    async with async_session() as session:
        all_location = await db.get_all_locations(session)
    return all_location


async def get_location_by_id(location_id: int):
    location = None
    async with async_session() as session:
        location = await db.get_location_by_id(session, location_id)
    return location


async def create_location_list(location_list: list[NewLocation]):
    async with async_session() as session:
        await db.create_location_list(session, location_list)


async def visit_location(user_id: int, location_id: int):
    async with async_session() as session:
        await db.visit_location(session, user_id, location_id)


async def get_all_category():
    all_category = []
    async with async_session() as session:
        all_category = await db.get_all_category(session)
    return all_category


async def create_category_list(category_list: list[NewCategory]):
    async with async_session() as session:
        await db.create_category_list(session, category_list)
