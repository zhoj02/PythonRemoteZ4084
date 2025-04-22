from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


class CiselnikZbozi:
    # Primary Key
    id = Column(Integer, primary_key=True)
    nazev_zbozi = Column(String)
    carovy_kod = Column(Integer)


class Zasoby:
    id = Column(Integer, primary_key=True)
    #Foreign Key
    cislo_zbozi = Column(Integer, ForeignKey('CiselnikZbozi.id'))
    pocet = Column(Integer)


class Prodeje:
    id = Column(Integer, primary_key=True)
    cislo_zbozi = Column(Integer, ForeignKey('CiselnikZbozi.id'))
    cas_prodeje = Column(DateTime)
    pocet = Column(Integer)
