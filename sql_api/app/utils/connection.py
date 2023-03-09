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
def conn():
    db = connect(
        host = db_host,
        user = db_user,
        password = db_password,
        database = db_name
    )

    if db:
        print("Loading to connect ...")
        print("Conneting to database ....\n")
    return db

conn()