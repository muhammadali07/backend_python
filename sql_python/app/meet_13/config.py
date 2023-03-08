import sqlalchemy as sa
from sqlalchemy import create_engine

MYSQL_USERNAME="bootcamp_user"
MYSQL_PASSWORD="bootcamp_password"
MYSQL_HOST="localhost"
MYSQL_PORT=3306
MYSQL_DB="bootcamp_isi_development"

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

def connection():
    SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )

    return engine