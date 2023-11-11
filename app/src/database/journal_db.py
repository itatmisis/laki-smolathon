import base64
from datetime import datetime 

from sqlalchemy import delete, func, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from .models.models import Notes
from src.schemas.user_schemas import UserOut


async def get_all_note(session: AsyncSession, current_user: UserOut) -> list | None:
    note_list = await session.execute(
        select(
            Notes
        ).where(
            Notes.id_user == current_user.id
        )
    )
    note_list = note_list.scalars().all()
    return note_list


async def get_note_by_location(session: AsyncSession, id_location: int):
    note_list = await session.execute(
        select(
            Notes
        ).where(
            Notes.id_location == id_location
        )
    )
    note_list = note_list.scalars().all()
    return note_list


async def get_note_by_id(session: AsyncSession, note_id: int):
    note = await session.execute(
        select(
            Notes
        ).where(
            Notes.id == note_id
        )
    )
    note = note.scalar_one_or_none()
    return note


async def update_note(session: AsyncSession, note_id: int, text: str = None, photo: str = None):
    note = await session.execute(
        select(
            Notes
        ).where(
            Notes.id == note_id
        )
    )
    note = note.scalar_one_or_none()

    if not note:
        raise HTTPException(
            detail=f'{note_id=} does not exist',
            status_code=status.HTTP_400_BAD_REQUEST
        )

    if text:
        note.text_reaction = text

    if photo:
        photo_as_byte = str.encode(photo)
        photo_recovered = base64.b64decode(photo_as_byte)
        try:
            file_name = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
            with open(f'./static/{file_name}.png', 'wb+') as f:
                f.write(photo_recovered)
        except Exception as e:
            print(e)
            raise HTTPException(
                detail=f'photo data is incorrect',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        photo_path = f'img/{file_name}.png'
        note.photo = photo_path

    await session.commit()
