from sqlalchemy.orm import sessionmaker

from models import Base
from config import connection_core
from crud import trainer_crud

def create_basemodel():
    Base.metadata.create_all(connection_core())
    Session = sessionmaker(connection_core())
    session = Session()
    return session

# while(True):
print("=== Belajar SQL Alchemy CRUD ===")
print("Creating table from Base...")
create_basemodel()
menu = input("pilih yang mana \n 1. Insert New Data \n 2. Insert Data Detail \n 3. Get Data from Keyword  \n 4. Get List \n Jawaban :  ")
if int(menu) == 1:
    result = trainer_crud.create_data(
        {
            "trainer_nama" : "Muh Ali Bakhtiar",
            "trainer_kelas" : "Back End Python",
            "trainer_tahun_masuk": "2023",
            "trainer_ket" : "Memenuhi project EOS BMS",
        }
    )
    print(result)
elif int(menu) == 2:
    result = trainer_crud.create_trainer_detail(
        {
            "trainer_nama_lengkap" : "Muh Ali Bakhtiar",
            "trainer_gelar": "Sarjana Komputer",
            "trainer_alumni_univ": "Universitas Muhammadiyah Sidoarjo",
            "trainer_konsentrasi" : "Software Engineering",
            "trainer_tahun_lulus" : "2019"
        }
    )
    print(result)
elif int(menu) == 3:
    result = trainer_crud.search('Ali')
    print(result)
elif int(menu) == 4:
    result = trainer_crud.get_list_data()
    print(result)
else:
    if int(menu) > 4:
        pass

