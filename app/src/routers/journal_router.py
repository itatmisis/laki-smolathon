from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder

from src.schemas.journal_schemas import *
from src.services.journal_service import *
from src.services.auth_utils import get_current_user
from requests import post
import json

journal_router = APIRouter(
    tags=['Journal'],
    prefix='/journal'
)


@journal_router.get('/note', response_model=list[NoteOut])
async def route_get_all_note(current_user: dict = Depends(get_current_user)):
    all_note = await get_all_note(current_user)
    return all_note


@journal_router.get('/note/{note_id}', response_model=NoteOut)
async def route_get_note_by_id(note_id: int, current_user: dict = Depends(get_current_user)):
    note = await get_note_by_id(note_id)
    return note


@journal_router.post('/note/{note_id}')
async def route_update_note(note_id: int, note_update: NoteUpdate, current_user: dict = Depends(get_current_user)):
    await update_note(note_id, note_update.text, note_update.photo)
