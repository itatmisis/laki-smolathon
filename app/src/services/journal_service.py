from fastapi import HTTPException, status
import requests

from src.schemas.user_schemas import UserOut
from src.database.db import async_session
import src.database.journal_db as db
import src.services.auth_utils as auth
# from src.database.models.models import Users, Locations

async def get_all_note(id_user: int):
    note_list = []
    async with async_session() as session:
        note_list = await db.get_all_note(session, id_user)

    return note_list


async def get_note_by_location(location_id: int):
    note_list = []
    async with async_session() as session:
        note_list = await db.get_note_by_location(session, location_id)

    return note_list


async def get_note_by_id(note_id: int):
    note = None
    async with async_session() as session:
        note = await db.get_note_by_id(session, note_id)

    return note


async def update_note(note_id: int, text: str = None, photo: str = None):
    async with async_session() as session:
        await db.update_note(session, note_id, text, photo)
