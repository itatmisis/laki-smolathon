from fastapi import HTTPException, status
import requests

import src.database.user_db as db
import src.services.auth_utils as auth
from src.database.models.models import Users
from src.database.db import async_session

async def registration_user(login: str, password: str, first_name: str, last_name: str):
    new_user = await auth.reg_user(login, password, first_name, last_name)
    return new_user


async def login_user(login, password):
    user = await auth.auth_user(login, password)
    access_token = await auth.create_access_token({'user_id': user.id})

    user_data = {
        'access_token': access_token,
        'token_type': 'bearer'
    }

    return user_data


async def update_user(user_id: int, login: str = None, password: str = None, first_name: str = None, last_name: str = None):
    async with async_session() as session:
        await db.update_user(session, user_id, login, password, first_name, last_name)



