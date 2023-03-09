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


def start_game():
    print("Welcome to the Tamagochi game with pytho crud")
    print("=== Login Game ===")
    username = input("Username : ")
    password = input("Password : ")
    if username not in (None, []) and password not in (None, []):
        logic_login = login(username, password)

def login(username, password):
    query = f'''
        select username, password from users where username = '{0}'
    '''.format(username)
    data = []
    return data
