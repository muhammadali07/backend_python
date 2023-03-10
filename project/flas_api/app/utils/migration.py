from sqlalchemy.orm import sessionmaker

from models import Base
from .connection import engine

def migrate_basemodel():
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    return session