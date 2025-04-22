from sqlalchemy import Column, Integer, String, ForeignKey


class CiselnikZbozi:
    # Primary Key
    id = Column(Integer, primary_key=True)
    nazev_zbozi = Column(String)
    carovy_kod = Column(Integer)


class Zasoby:
    id = Column(Integer, primary_key=True)
    #Foreign Key
    cislo_zbozi = Column(Integer, ForeignKey('CiselnikZbozi.id'))
    pocet = 10


class Prodeje:
    id = 1
    cislo_zbozi = CiziKlic(CiselnikZbozi(id))
    cas_prodeje = "14:30 2025-04-21"
    pocet = 2
