from fastapi import APIRouter, Depends # type: ignore
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

# import get_async_session from migration
from service import get_async_session, verify_token

# import schema /payload
from schema import AccountUser, AccountLogin
# import crud
from crud import account_user_crud

root = APIRouter()

@root.post('/upload-data', summary="Upload data")
async def upload_data():
    data = ''
    out_response = ''
    return out_response