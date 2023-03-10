from sqlalchemy.orm import sessionmaker

from models import Base
from config import connection_core
from crud import trainer_crud

def create_basemodel():
    Base.metadata.create_all(connection_core())
    Session = sessionmaker(connection_core())
    session = Session()
    return session

while(True):
    print("=== Belajar SQL Alchemy CRUD ===")
    print("Creating table from Base...")
    create_basemodel()
    menu = input("pilih yang mana \n 1. Create Data \n 2. Get Data List From Keyword \n 3. Update Data \n 4. Delete Data \n Jawaban :  ")

    if int(menu) == 1:
        # result = core_crud.create_data()
        result = trainer_crud.create_data(
            {
                "trainer_nama" : "Muh Ali Bakhtiar",
                "trainer_kelas" : "Back End Python",
                "trainer_tahun_masuk": "2023",
                "trainer_ket" : "Memenuhi project EOS BMS",
                "trainer_gelar": "Sarjana Komputer",
                "trainer_alumni_univ": "Universitas Muhammadiyah Sidoarjo",
                "trainer_konsentrasi" : "Software Engineering",
                "trainer_tahun_lulus" : "2019"
            }
        )
        print(result)
    elif int(menu) == 2:
        result = trainer_crud.search('Ali')
        print(result)
    # elif int(menu) == 3:
    #     result = core_crud.update_data()
    #     print(result)
    # elif int(menu) == 4:
    #     result = core_crud.delete_data()
    #     print(result)
    # elif int(menu) == 0:
    #     create_basemodel()
    else:
        if int(menu) > 4:
            break

