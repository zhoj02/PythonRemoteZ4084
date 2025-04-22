from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# connection string
db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/')

