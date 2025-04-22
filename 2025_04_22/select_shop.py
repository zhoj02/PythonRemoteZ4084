from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from shop_definition import CiselnikZbozi
db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/sql_orm')

#insert mock data
sessionmaker = sessionmaker(bind=db)
session = sessionmaker()
# Select
result = session.query(CiselnikZbozi).all()
for row in result:
    print(row.id, row.nazev_zbozi, row.carovy_kod)