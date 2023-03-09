import colorama
from dotenv import dotenv_values
from mysql.connector import connect
from progresbar import progress_bar


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


def migration_data():
    try:
        print("Importing data from .sql file\n")
        fdb = 'database/bootcamp_isi_development.sql'
        data = open(fdb)
        query_data = data.read()
        data = []
        data.append(query_data)
        
        # koneksi
        cur_db = db.cursor()
        cur_db.execute(query_data)
        cur_db.close()
        db.close()
        progress_bar(0, len(data))
        print("Migration data success\n")
    except Exception as e:
        print(f"Migration data Failed !!! : {e}")

if db:
    print("Loading to connect ...")
    print("Conneting to database ....\n")
    migration_data()