from fastapi import APIRouter

from .account_user import *

api_router = APIRouter()

# user
api_router.include_router(account_user.root, prefix='/account_user', tags=['Account User'])


