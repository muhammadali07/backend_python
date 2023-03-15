from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

MYSQL_USERNAME="bootcamp_user"
MYSQL_PASSWORD="bootcamp_password"
MYSQL_HOST="localhost"
MYSQL_PORT=3306
MYSQL_DB="bootcamp_isi_development"



SQLALCHEMY_DATABASE_URL = f"mysql+aiomysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

metadata = MetaData()
Base = declarative_base(metadata=metadata)


# Buat session factory
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# db async session
async def get_async_session():
    db = async_session()
    try:
        yield db
    finally:
        await db.close() # type: ignore


# async def create_mysql_pool():
#     pool = await aiomysql.create_pool(
#         host='localhost',
#         port=3306,
#         user='bootcamp_user',
#         password='bootcamp_password',
#         db='bootcamp_isi_development',
#         autocommit=True
#     )
#     # Base.metadata.drop_all(engine)
#     # Base.metadata.create_all(engine)
#     print("Migration Base Model Success ...")
#     return pool


