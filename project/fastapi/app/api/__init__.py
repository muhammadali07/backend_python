from fastapi import APIRouter

from .account_user import *
from .upload_data import *

api_router = APIRouter()

# user
api_router.include_router(account_user.root, prefix='/account_user', tags=['Account User'])
# upload data
api_router.include_router(upload_data.root, prefix='/upload-file', tags=['Upload File'])

