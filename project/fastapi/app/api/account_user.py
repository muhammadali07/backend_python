from fastapi import APIRouter, Depends # type: ignore
from sqlalchemy.ext.asyncio import AsyncSession

# import get_async_session from migration
from service import get_async_session

# import schema /payload
from schema import AccountUser
# import crud
from crud import account_user_crud

root = APIRouter()

@root.post("/create_user", summary="Buat Akun Baru")
async def create_user(
    data: AccountUser,
    db_session: AsyncSession = Depends(get_async_session)
):
    out_response = account_user_crud.create_user(data=data, db_session=db_session)
    return out_response
