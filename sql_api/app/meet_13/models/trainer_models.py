from sqlalchemy import Column, Integer, String, Text, BigInteger, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class TrainerModels(Base):
    __tablename__ = "trainer"
    id = Column(BigInteger, primary_key = True)
    trainer_nama = Column(String(200))
    trainer_kelas = Column(String(200))
    trainer_tahun_masuk = Column(Integer)
    trainer_ket = Column(Text)
    trainer = relationship("TrainerDetailsModels")
    create_date = Column(TIMESTAMP)
    
class TrainerDetailsModels(Base):
    __tablename__ = "trainer_detail"
    id = Column(BigInteger, primary_key = True)
    id_parents = Column(BigInteger,ForeignKey("trainer.id", ondelete="CASCADE"))
    trainer_nama_lengkap = Column(String(200))
    trainer_gelar = Column(String(200))
    trainer_alumni_univ = Column(String(200))
    trainer_konsentrasi = Column(String(200))
    trainer_tahun_lulus = Column(Integer)
    create_date = Column(TIMESTAMP)