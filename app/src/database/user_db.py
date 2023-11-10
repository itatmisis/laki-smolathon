from sqlalchemy import delete, func, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from .db import async_session
from .models.models import Users


async def reg_user(login: str, password: str, first_name: str, last_name: str) -> int | None:
    session: AsyncSession
    async with async_session() as session:
        check = await session.execute(
            select(
                Users.login
            ).where(
                Users.login == login
            )
        )
        check = check.scalar_one_or_none()
        if check is not None:
            raise HTTPException(
                detail='login already exist',
                status_code=status.HTTP_400_BAD_REQUEST
            )

        new_user = Users(
            login=login,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        session.add(new_user)
        await session.commit()

        return new_user


async def get_user_by_id(id_user: int):
    session: AsyncSession
    async with async_session() as session:
        user = await session.execute(
            select(
                Users
            ).where(
                Users.id == int(id_user)
            )
        )
        user = user.scalar_one_or_none()
        return user


async def get_user_by_login(login: str):
    session: AsyncSession
    async with async_session() as session:
        user = await session.execute(
            select(
                Users
            ).where(
                Users.login == login
            )
        )
        user = user.scalar_one_or_none()
        return user


async def update_user(session: AsyncSession, user_id: int, login: str = None, password: str = None, first_name: str = None, last_name: str = None):
    user = await session.execute(
        select(
            Users
        ).where(
            Users.id == user_id
        )
    )
    user = user.scalar_one_or_none()

    if login:
        user.login = login

    if password:
        user.password = password

    if first_name:
        user.first_name = first_name

    if last_name:
        user.last_name = last_name

    await session.commit()
