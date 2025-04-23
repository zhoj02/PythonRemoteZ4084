from sqlalchemy import create_engine

from shop_definition import Base
db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/sql_orm')

Base.metadata.create_all(db)