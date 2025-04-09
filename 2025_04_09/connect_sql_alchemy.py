from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/')

Base = declarative_base()
Session = sessionmaker(bind=db)

session = Session()
#test connection with SELECT 1
result = session.execute(text("SELECT 1"))
for row in result:
    print(row[0])
