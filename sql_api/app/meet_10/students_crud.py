from dotenv import dotenv_values
from mysql.connector import connect

params = {
    "db": dotenv_values(".env")
}

db_user = params["db"]["MYSQL_USERNAME"]
db_password = params["db"]["MYSQL_PASSWORD"]
db_host = params["db"]["MYSQL_HOST"]
db_port = params["db"]["MYSQL_PORT"]
db_name = params['db']['MYSQL_DB']

# membuat objek koneksi database
db = connect(
    host = db_host,
    user = db_user,
    password = db_password,
    database = db_name
)

if db:
    print("Loading to connect ...")
    print("Conneting to database ....\n")


# membuat database
def create_database():
    try:
        # membuat object cursor
        cursor_db = db.cursor()

        # perintah eksekusi dari cursor
        cursor_db.execute("CREATE DATABASE IF NOT EXISTS bootcamp_isi_development")

        # menutup objek cursor
        cursor_db.close()

        # memutus koneksi database
        db.close()
        print("Database berhasil dibuat...")
        return True
    except Exception as e:
        print(f"Database Gagal dibuat: {e}")


def create_table():
    try:
        cursor_db = db.cursor()
        query_stmt = '''
            CREATE Table students(
            id_siswa int primary key auto_increment,
            nama VARCHAR(50) not null,
            id_kelas int not null,
            tahun_masuk VARCHAR(50) not null,
            jenis_kelas VARCHAR(100) not null,
            update_date timestamp,
            create_date timestamp
        )
        '''
        cursor_db.execute(query_stmt)
        cursor_db.close()
        print("Table berhasil dibuat...")
        return True
    except Exception as e:
        print(f"Tabel Gagal dibuat: {e}")    

def insert_data():
    try:
        cursor_db = db.cursor()
        query_stmt = '''
            INSERT INTO students (nama, id_kelas, tahun_masuk, jenis_kelas, create_date)
            VALUES
                ('anwar', 1, 2023, 'backend', NOW()),
                ('dwija', 1, 2023, 'backend', NOW()),
                ('rida', 1, 2023, 'backend', NOW()),
                ('kinanti', 1, 2023, 'backend', NOW()),
                ('touya', 2, 2023,  'flutter', NOW()),
                ('kanami', 2, 2023, 'flutter', NOW()),
                ('tsubasa', 3, 2023, 'laravel', NOW())
                '''
        cursor_db.execute(query_stmt)
        db.commit()
        cursor_db.close()
        print("inset data berhasil dibuat...")
        return True
    except Exception as e:
        print(f"insert data gagal dibuat: {e}") 

def insert_with_loop():
    try:
        data = [
            ('anwar', 1, 2023, 'backend'),
            ('dwija', 1, 2023, 'backend'),
            ('rida', 1, 2023, 'backend'),
            ('kinanti', 1, 2023, 'backend'),
            ('touya', 2, 2023,  'flutter'),
            ('kanami', 2, 2023, 'flutter'),
            ('tsubasa', 3, 2023, 'laravel')
        ]
        cursor_db = db.cursor()
        query_stmt = '''
            INSERT INTO students (nama, id_kelas, tahun_masuk, jenis_kelas, create_date) VALUES (%s,%s,%s,%s,NOW())
        '''
        for i in data:
            cursor_db.execute(query_stmt,i)

        db.commit()
        cursor_db.close()
        print("inset data dengan perulangan berhasil dibuat...")
        return True
    except Exception as e:
        print(f"insert data dengan perulangan gagal dibuat: {e}") 
    finally:
        db.close()

def update_data(nama, kolom, nilai):
    try:
        query_stmt = f'''
            update students
            SET
                {kolom} = {nilai}
            WHERE
                nama = "{nama}"
        '''
        cursor_db = db.cursor()
        cursor_db.execute(query_stmt)
        db.commit()
        cursor_db.close()
        db.close()
        print("Update data berhasil")
    except Exception as e:
        print(f"Updata data gagal : {e}")

def delete_data(nama):
    try:
        query_stmt = f'''
            delete from students where nama = "{nama}"
        '''
        cursor_db = db.cursor()
        cursor_db.execute(query_stmt)
        db.commit()
        cursor_db.close()
        db.close()
        print("Hapus data berhasil")
    except Exception as e:
        print(f"Hapus data gagal : {e}")

def list_data():
    try:
        query_stmt = f'''
            SELECT * from students s order by s.create_date DESC limit 10
        '''
        cursor_db = db.cursor()
        cursor_db.execute(query_stmt)
        result = cursor_db.fetchall()
        cursor_db.close()
        db.close()

        for student in result:
            print(student)
        print("Get data berhasil")
    except Exception as e:
        print(f"Get data gagal : {e}")

def list_data_many():
    try:
        query_stmt = f'''
            SELECT * from students s order by s.create_date DESC limit 10
        '''
        cursor_db = db.cursor()
        cursor_db.execute(query_stmt)
        result = cursor_db.fetchmany()
        cursor_db.close()
        db.close()

        for student in result:
            print(student)
        print("Get data berhasil")
    except Exception as e:
        print(f"Get data gagal : {e}")


def search_list(keyword):
    try:
        query_stmt = f'''
            SELECT * from students s where = "{keyword}" order by s.create_date DESC limit 10
        '''
        cursor_db = db.cursor()
        cursor_db.execute(query_stmt)
        result = cursor_db.fetchone()
        cursor_db.close()
        db.close()

        print(result)
        print("Get data berhasil")
    except Exception as e:
        print(f"Get data gagal : {e}")


_create_table = create_table()
if _create_table == True:
    # insert_data()
    # insert_with_loop()
    list_data()