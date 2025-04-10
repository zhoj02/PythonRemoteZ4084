from sqlalchemy import create_engine, text, String, Integer, Date, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open("heslo.txt", "r") as file:
    password = file.read()

# connection string
db = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/online_movie_rating')

Base = declarative_base()
Session = sessionmaker(bind=db)

session = Session()


class Actor(Base):
    __tablename__ = "actor"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    birth_date = Column(Date)


Base.metadata.create_all(db)
