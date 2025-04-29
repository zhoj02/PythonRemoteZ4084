from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


# connection string
db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/banka')

Session = sessionmaker(bind=db)

session = Session()


class Ucet:
    pass

class Client:
    pass

try:
    session.add(
        Client(id=5, ...)
    )
    session.add(
        Ucet(id=1, nazev="Ucet 1", zbyva=1000, zablokovany=False, typ="Běžný", datum_vytvoreni="Ahoj", id_klienta=1)
    )
    session.commit()
except Exception as e:
    session.rollback()
    print("Chyba při vkládání dat:", e)
