import json
from datetime import datetime
from flask import jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from sqlalchemy import and_, or_, delete, desc, asc
from models import TrainerModels, TrainerDetailsModels

from utils import engine, as_dict, ResponseOutCustom


Session = sessionmaker(engine)
session = Session()

def create_data(data):
    _val = validation_data_trainer(data['trainer_nama'])
    new_data = TrainerModels(
        trainer_nama=data['trainer_nama'],
        trainer_kelas=data['trainer_kelas'],
        trainer_tahun_masuk=data['trainer_tahun_masuk'],
        trainer_ket=data['trainer_ket'],
        create_date = datetime.now()
    )
    try:
        if _val == True:
            return ResponseOutCustom(message="02", status=f"Data dengan {data['trainer_nama']} sudah tersedia", data=[])
        else:
            session.add(new_data)
        session.commit()
        session.refresh(new_data)
        session.close()
        return ResponseOutCustom(message="00", status="Berhasil", data=data)
    except Exception as e:
        return "Error"
    

# def create_trainer_detail(data):
#     new_data = TrainerDetailsModels(
#         trainer_nama_lengkap=data['trainer_nama_lengkap'],
#         trainer_gelar=data['trainer_gelar'],
#         trainer_alumni_univ=data['trainer_alumni_univ'],
#         trainer_konsentrasi=data['trainer_konsentrasi'],
#         trainer_tahun_lulus=data['trainer_tahun_lulus'],
#         create_date = datetime.now()
#     )
#     try:
#         session.add(new_data)
#         session.commit()
#         session.close()
#         return ResponseOutCustom(message_id="00", status="Success", data=data)
#     except Exception as e:
#         return ResponseOutCustom(message_id="03", status=f'{e}', data=[])

def get_list_data(keyword, limit, page):
    try:
        tbtrainer = TrainerModels
        offset = page * limit
        terms = []
        if keyword not in (None, ''):
            terms.append(and_(
                or_(
                    tbtrainer.trainer_nama.ilike(f"%{keyword}%"),
                    tbtrainer.trainer_kelas.ilike(f"%{keyword}%"),
                    tbtrainer.trainer_ket.ilike(f"%{keyword}%")
                )
            )
        )
        if len(terms) > 0:
            query_stmt = (
                select(tbtrainer).filter(*(terms)).limit(limit).offset(offset).order_by(asc(tbtrainer.create_date))
            )
        else:
            query_stmt = (select(tbtrainer).limit(limit).offset(offset))
   
        proxy_rows = session.execute(query_stmt).scalars().all()
        data = as_dict(proxy_rows)
        if data not in (None, [], ''):
            return ResponseOutCustom(message="00", status="Success", data=data)
        else:
            return ResponseOutCustom(message="02", status="Data not found", data=data)
    except Exception as e:
        return ResponseOutCustom(message="03", status=f"{e}", data=[])

# def get_list_data():
#     try:
#         tb_trainer = TrainerModels
#         query_stmt = (
#             select(tb_trainer).order_by(asc(tb_trainer.create_date))
#         )
#         proxy_rows = session.execute(query_stmt)
#         result = proxy_rows.fetchall()
#         data = []
#         for i in result:
#             dt = {
#                 "trainer_nama":i[0]
#             }
#             data.append(dt)
#         session.close()
#         return ResponseOutCustom(message_id="00", status="Success", data=[data])
#     except Exception as e:
#         return ResponseOutCustom(message_id="03", status=f'{e}', data=[])

def validation_data_trainer(data):
    query_stmt = select(TrainerModels).where(TrainerModels.trainer_nama == str(data))
    proxy_row = session.execute(query_stmt).scalars().first()
    if proxy_row is None:
        return False
    else:
        data = as_dict(proxy_row)
        return True