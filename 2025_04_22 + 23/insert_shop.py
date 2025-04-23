from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from shop_definition import CiselnikZbozi
db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/sql_orm')

#insert mock data
sessionmaker = sessionmaker(bind=db)
session = sessionmaker()
# Create mock data
session.add(CiselnikZbozi(id=2, nazev_zbozi="Test Product 2", carovy_kod=157578))
# Commit the transaction
session.commit()


# (id, nazev_zbozi, carovy_kod) values (1, 'Test Product', 1234567890123)





