import sqlalchemy as sa 
from sqlalchemy import create_engine
from crud import create_data, get_list_student, update_data, delete_data

while(True):
    print("=== Belajar SQL Alchemy CRUD ===")
    menu = input("pilih yang mana \n 1. Create Data \n 2. Get Data List \n 3. Update Data \n 4. Delete Data \n Jawaban :  ")

    if int(menu) == 1:
        result = create_data()
        print(result)
    elif int(menu) == 2:
        result = get_list_student()
        print(result)
    elif int(menu) == 3:
        result = update_data()
        print(result)
    elif int(menu) == 4:
        result = delete_data()
        print(result)
    else:
        if int(menu) > 4:
            break

