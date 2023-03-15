from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

# import service
from service import ResponseOutCustom

from schema import AccountUser

# import models
from models import AccountUserModels


async def create_user(data: AccountUser, db_session:AsyncSession):
    async with db_session as session:
        try:
            tbUser = AccountUserModels
            new_data = tbUser(
                username = data.username,
                email=data.email,
                password=data.password,
                role=data.role,
                divisi=data.divisi,
                create_date=datetime.now()
            )
            session.add(new_data) # type: ignore
            await session.commit()
            # out_resp = await ResponseOutCustom(message="00", status="Create Account Success", data= new_data)
            return "berhasil"
        except Exception as e:
            # out_resp = await ResponseOutCustom(message="03",status=f"{e}", data=[])
            return 'haha'