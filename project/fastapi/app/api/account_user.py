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

@root.post("/create_user", summary="Create New Account")
async def create_user(
    data: AccountUser,
    db_session: AsyncSession = Depends(get_async_session)
):
    out_response = await account_user_crud.create_user(data=data, db_session=db_session)
    return out_response

@root.post("/login", summary="Login Apps")
async def login(
    data: AccountLogin,
    db_session: AsyncSession = Depends(get_async_session)
):
    out_response = await account_user_crud.login(data=data, db_session=db_session)
    return out_response

@root.get("/get-list-user", 
          summary="List Account User",
          )
async def get_list_user(
    keyword: str = "",
    limit: int = 10,
    page: int = 0,
    db_session: AsyncSession = Depends(get_async_session),
    user_info: dict = Depends(verify_token)
):
    # print(user_info)
    out_response = await account_user_crud.get_list_user(
        keyword=keyword,
        limit=limit,
        page=page,
        db_session=db_session)
    return out_response


@root.get("/get-user-by-id", 
          summary="Get User By ID",
          )
async def get_user_by_id(
    id: str = '',
    db_session: AsyncSession = Depends(get_async_session),
    # user_info: dict = Depends(verify_token)
):
    # print(user_info)
    out_response = await account_user_crud.get_user_by_id(id, db_session)
    return out_response



