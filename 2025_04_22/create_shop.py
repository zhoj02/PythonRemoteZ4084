from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CiselnikZbozi(Base):
    # Primary Key
    id = Column(Integer, primary_key=True)
    nazev_zbozi = Column(String)
    carovy_kod = Column(Integer)


class Zasoby(Base):
    id = Column(Integer, primary_key=True)
    #Foreign Key
    cislo_zbozi = Column(Integer, ForeignKey('CiselnikZbozi.id'))
    pocet = Column(Integer)


class Prodeje(Base):
    id = Column(Integer, primary_key=True)
    cislo_zbozi = Column(Integer, ForeignKey('CiselnikZbozi.id'))
    cas_prodeje = Column(DateTime)
    pocet = Column(Integer)
