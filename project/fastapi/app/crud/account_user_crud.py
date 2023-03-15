# from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, or_, and_, insert, join, outerjoin, delete, func, desc, asc
from sqlalchemy.future import select


from datetime import datetime, timedelta

# import service
from service import ResponseOutCustom, create_access_token

from schema import AccountUser

# import models
from models import AccountUserModels

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # waktu kedaluwarsa token


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
            out_resp =  ResponseOutCustom(message="00", status="Create Account Success", data= new_data)
            return out_resp
        except Exception as e:
            out_resp = ResponseOutCustom(message="03",status=f"{e}", data=[])
            return out_resp

async def login(data, db_session:AsyncSession):
    async with db_session as session:
        try:
            tbUser = AccountUserModels

            query_stmt = select(tbUser).filter(
                and_(
                    tbUser.email == data.email
                )
            )
            proxy_row = await session.execute(query_stmt)
            result = proxy_row.scalars().first()
            dt = {
                "username": result.username,
                "email": result.email,
                "divisi": result.divisi,
                "role": result.role
            }
            if result and result.password == data.password:
                _token = create_access_token(data=dt, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
                return ResponseOutCustom(message="00", status="Login Success", data= {"token_bearer": _token})
            else:
                return ResponseOutCustom(message="00", status="Login Failed", data= [])
        except Exception as e:
            out_resp = ResponseOutCustom(message="03",status=f"{e}", data=[])
            return out_resp

async def get_list_user(keyword:str, limit:int, page:int, db_session:AsyncSession):
    async with db_session as session:
        try:
            tbUser = AccountUserModels
            _limit = limit
            _page = page
            offset = _page * _limit
            terms = []
            if keyword not in (None, [], ''):
                terms.append(
                    or_(
                        tbUser.username.ilike(f"%{keyword}%"),
                        tbUser.divisi.ilike(f"%{keyword}%"),
                        tbUser.role.ilike(f"%{keyword}%")
                    )
                )
            
            if len(terms) > 0:
                query_stmt = select(tbUser).filter(*(terms)).limit(limit).offset(offset).order_by(desc(tbUser.create_date))
            else:    
                query_stmt = select(tbUser).limit(limit).offset(offset).order_by(desc(tbUser.create_date))
            proxy_row = await session.execute(query_stmt)
            result = proxy_row.scalars().all()
            status = "Success" if len(result) > 0 else "Data not found"
            out_resp =  ResponseOutCustom(message="00", status=status, data= result)
            return out_resp
        except Exception as e:
            out_resp = ResponseOutCustom(message="03",status=f"{e}", data=[])
            return out_resp