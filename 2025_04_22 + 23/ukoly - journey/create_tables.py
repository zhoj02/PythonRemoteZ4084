from sqlalchemy import create_engine
from definition import base
db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/sql_orm')


base.metadata.create_all(db)