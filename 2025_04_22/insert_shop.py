from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from shop_definition import CiselnikZbozi
db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/sql_orm')

#insert mock data
sessionmaker = sessionmaker(bind=db)
session = sessionmaker()
# Create mock data
session.add(CiselnikZbozi(id=1, nazev_zbozi="Test Product", carovy_kod=1234567890123))





