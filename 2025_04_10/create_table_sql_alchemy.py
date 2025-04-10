from sqlalchemy import create_engine, text, String, Integer, Date, Column
from database_definition import Base
from sqlalchemy.orm import sessionmaker

with open("heslo.txt", "r") as file:
    password = file.read()

# connection string
db = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/online_movie_rating')

Session = sessionmaker(bind=db)

session = Session()


Base.metadata.create_all(db)
