from fastapi import HTTPException, status
import requests

from src.database.db import async_session
import src.database.map_db as db
import src.database.journal_db as j_db
import src.services.auth_utils as auth
from src.schemas.map_schemas import NewLocation, NewCategory

# from src.database.models.models import Users, Locations


async def get_all_locations(user_id: int):
    all_location = []
    async with async_session() as session:
        location_list = await db.get_all_locations(session)
        note_list = await j_db.get_all_note(session, user_id)
        loc_id_set = [note.id_location for note in note_list]
        loc_id_set = set(loc_id_set)

        for location in location_list:
            sub_loc = location.__dict__
            sub_loc.pop('_sa_instance_state')
            sub_loc['has_visited'] = True if location.id in loc_id_set else False
            all_location.append(sub_loc)

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
