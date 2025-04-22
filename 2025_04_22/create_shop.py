from sqlalchemy import Column

class CiselnikZbozi:
    # Primary Key
    id = Column(Integer, primary_key=True)
    nazev_zbozi = "Ranné brambory"
    carovy_kod = 987548


class Zasoby:
    id = 1
    #Foreign Key
    cislo_zbozi = CiziKlic(CiselnikZbozi(id))
    pocet = 10


class Prodeje:
    id = 1
    cislo_zbozi = CiziKlic(CiselnikZbozi(id))
    cas_prodeje = "14:30 2025-04-21"
    pocet = 2
