from sqlalchemy import (Column,Integer, BigInteger, 
                        String, Text, TIMESTAMP
                        )
from service import Base


class AccountUserModels(Base):
    __tablename__ = "account_user"
    id = Column(BigInteger, primary_key = True)
    username = Column(String(200))
    email = Column(String(200))
    password = Column(Text)
    role = Column(String(50))
    divisi = Column(String(300))
    create_date = Column(TIMESTAMP)