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

db = connect(
    host = db_host,
    user = db_user,
    password = db_password,
    database = db_name
)


if db:
    print("Database berhasil terkoneksi")

try:
    cursor_db = db.cursor()
    cursor_db.execute("CREATE DATABASE IF NOT EXISTS bootcamp_isi_development")

    query_stmt = '''CREATE Table students(

        id_siswa int primary key auto_increment,

        nama VARCHAR(50) not null,

        id_kelas int not null,

        tahun_masuk int not null
    )'''
    
    cursor_db.execute(query_stmt)
    cursor_db.close()
    db.close()
    print("tabel berhasil dibuat")
except Exception as e:
    print(f"Database gagal di buat {e}")