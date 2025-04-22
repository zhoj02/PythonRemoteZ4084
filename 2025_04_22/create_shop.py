class CiselnikZbozi:
    id = Primarni klic(1)
    nazev_zbozi = "Ranné brambory"
    carovy_kod = 987548


class Zasoby:
    id = 1
    #Foreign Keys
    cislo_zbozi = CiziKlic(CiselnikZbozi(id))
    pocet = 10


class Prodeje:
    id = 1
    cislo_zbozi = CiziKlic(CiselnikZbozi(id))
    cas_prodeje = "14:30 2025-04-21"
    pocet = 2
