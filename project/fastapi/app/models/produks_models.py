from sqlalchemy import (Column,Integer, BigInteger, 
                        String, Text, TIMESTAMP
                        )
from service import Base


class ProduksModels(Base):
    __tablename__ = "produk"
    id_produk = Column(BigInteger, primary_key = True)
    product_name = Column(String(200))
    category = Column(String(200))
    sub_category = Column(String(200))
    create_date = Column(TIMESTAMP)


class ProdukUsersModels(Base):
    __tablename__ = "produk_user"
    customer_id = Column(BigInteger, primary_key = True)
    city = Column(String(200))
    state = Column(String(200))
    postal = Column(Integer)
    create_date = Column(TIMESTAMP)