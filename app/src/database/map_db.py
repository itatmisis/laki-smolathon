from sqlalchemy import delete, func, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from .models.models import Users, Locations, Notes, Categories, Events
from src.schemas.map_schemas import NewLocation, NewCategory, NewEvent


async def get_all_locations(session: AsyncSession):
    locations_list = await session.execute(
        select(
            Locations
        )
    )
    locations_list = locations_list.scalars().all()
    return locations_list


async def get_location_by_id(session: AsyncSession, location_id: int):
    location = await session.execute(
        select(
            Locations
        ).where(
            Locations.id == location_id
        )
    )
    location = location.scalar_one_or_none()
    return location


async def create_location_list(session: AsyncSession, location_list: list[NewLocation]):
    for new_location in location_list:
        session.add(
            Locations(**new_location.dict())
        )

    await session.commit()


async def visit_location(session: AsyncSession, user_id: int, location_id: int):
    location = await get_location_by_id(session, location_id)
    if not location:
        raise HTTPException(
            detail=f'{location_id=} does not exist',
            status_code=status.HTTP_400_BAD_REQUEST
        )

    user = await session.execute(
        select(
            Users
        ).where(
            Users.id == user_id
        )
    )
    user = user.scalar_one_or_none()

    if not user:
        raise HTTPException(
            detail=f'{user_id=} does not exist',
            status_code=status.HTTP_400_BAD_REQUEST
        )

    note = Notes(
        id_user = user.id,
        id_location = location.id
    )

    session.add(note)
    await session.commit()


async def get_all_category(session: AsyncSession):
    category_list = await session.execute(
        select(
            Categories
        )
    )
    category_list = category_list.scalars().all()
    return category_list


async def create_category_list(session: AsyncSession, category_list: list[NewCategory]):
    for new_category in category_list:
        session.add(
            Categories(**new_category.dict())
        )

    await session.commit()


async def get_all_events(session: AsyncSession):
    events_list = await session.execute(
        select(
            Events
        )
    )
    events_list = events_list.scalars().all()
    return events_list


async def get_event_by_id(session: AsyncSession, event_id: int):
    event = await session.execute(
        select(
            Events
        ).where(
            Events.id == event_id
        )
    )
    event = event.scalar_one_or_none()
    return event


async def create_events_list(session: AsyncSession, event_list: list[NewEvent]):
    for new_event in event_list:
        session.add(
            Events(**new_event.dict())
        )

    await session.commit()
