from sqlalchemy.orm import sessionmaker

from datetime import datetime
from config import engine
from models import sa
from utils import ResponseOutCustom
# import model
from models import students

Session = sessionmaker(bind=engine)
session = Session() 

def create_data():
    data = students.insert().values(nama = 'indra', id_kelas = 2, tahun_masuk=2023, jenis_kelas = "Devops", create_date=datetime.now())
    # conn = engine.connect()
    session.execute(data)
    session.commit()
    return ResponseOutCustom(message_id="00",status="data berhasil di tambahkan", data=[])

def get_list_student():
    query_stmt = sa.select(students).where(students.c.nama=='indra')
    # conn = engine.connect()
    result = session.execute(query_stmt).all()
    data = []

    for i in result:
        dt = {
            "id_siswa": i[0],
            "nama": i[1],
            "id_kelas": i[2],
            "tahun_masuk": i[3],
            "jenis_kelas": i[4],
            "update_date": i[5],
            "create_date": i[6],
        }
        data.append(dt)
    status = "Berhasil" if result not in (None, '', [], ()) else "Data tidak ditemukan"
    return ResponseOutCustom(message_id="00",status=status, data=data if len(data)>0 else [])

def update_data():
    data = students.update().where(students.c.nama=='indra').values(id_kelas=9)
    # conn = engine.connect()
    session.execute(data)
    session.commit()
    return ResponseOutCustom(message_id="00",status="Data berhasil di ubah", data=[])

def delete_data():
    data = students.delete().where(students.c.nama == 'indra')
    # conn = engine.connect()
    session.execute(data)
    session.commit()
    return ResponseOutCustom(message_id="00",status="Data berhasil di hapus", data=[])


