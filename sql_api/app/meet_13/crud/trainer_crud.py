from datetime import datetime
from config import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from sqlalchemy import and_, or_, delete, desc, asc
from models import TrainerModels, TrainerDetailsModels
from utils import ResponseOutCustom

Session = sessionmaker(engine)
session = Session()

def create_data(data):
    new_data = TrainerModels(
        trainer_nama=data['trainer_nama'],
        trainer_kelas=data['trainer_kelas'],
        trainer_tahun_masuk=data['trainer_tahun_masuk'],
        trainer_ket=data['trainer_ket'],
        create_date = datetime.now()
    )
    try:
        session.add(new_data)
        session.commit()
        session.close()
        return ResponseOutCustom(message_id="00", status="Success", data=[data])
    except Exception as e:
        return ResponseOutCustom(message_id="03", status=f'{str(e)}', data=[])
    

def create_trainer_detail(data):
    new_data = TrainerDetailsModels(
        trainer_nama_lengkap=['trainer_nama'],
        trainer_gelar=['trainer_gelar'],
        trainer_alumni_univ=['trainer_alumni_univ'],
        trainer_konsentrasi=['trainer_konsentrasi'],
        trainer_tahun_lulus=['trainer_tahun_lulus'],
        create_date = datetime.now()
    )
    try:
        session.add(new_data)
        session.commit()
        session.close()
        return ResponseOutCustom(message_id="00", status="Success", data=[data])
    except Exception as e:
        return ResponseOutCustom(message_id="03", status=f'{e}', data=[])

def search(keyword:str):
    try:
        tb_trainer = TrainerModels

        terms = []

        if keyword not in (None, ''):
            terms.append(and_(
                or_(
                    tb_trainer.trainer_nama.ilike(f"%{keyword}%"),
                    tb_trainer.trainer_kelas.ilike(f"%{keyword}%"),
                    tb_trainer.trainer_ket.ilike(f"%{keyword}%")
                )
            )
        )
        query_stmt = (
            select(tb_trainer).filter(*(terms)).order_by(asc(tb_trainer.create_date))
        )
        proxy_rows = session.execute(query_stmt)
        result = proxy_rows.all()
        data = []
        for i in result:
            dt = {
                "trainer_nama":i[0]
            }
            data.append(dt)
        session.close()
        return ResponseOutCustom(message_id="00", status="Success", data=[data])
    except Exception as e:
        return ResponseOutCustom(message_id="03", status=f'{e}', data=[])

        