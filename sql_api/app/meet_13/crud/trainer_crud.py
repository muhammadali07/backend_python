from datetime import datetime
from config import engine
from sqlalchemy.orm import sessionmaker
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

        