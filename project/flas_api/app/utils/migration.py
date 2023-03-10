from sqlalchemy.orm import sessionmaker

from models import Base
from .connection import engine

def migrate_basemodel():
    # drop table
    Base.metadata.drop_all(engine)

    # create table
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    return session