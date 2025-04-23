# 5 zbozi do ciselniku
# kazde to zbozi dat na sklad - Zasoby

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from shop_definition import CiselnikZbozi

db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/sql_orm')
Session = sessionmaker(bind=db)
session = Session()

session.add_all(
    [
        CiselnikZbozi(id=3, nazev_zbozi="Banany ruzove", carovy_kod=19582),
        CiselnikZbozi(id=4, nazev_zbozi="Maslo", carovy_kod=18975),
        CiselnikZbozi(id=5, nazev_zbozi="Redkvicky", carovy_kod=69750),
        CiselnikZbozi(id=6, nazev_zbozi="Testoviny", carovy_kod=47800),

    ]

)

session.commit()
