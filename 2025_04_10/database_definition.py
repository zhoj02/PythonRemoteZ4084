from sqlalchemy import String, Integer, Date, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Actor(Base):
    __tablename__ = "actor"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    birth_date = Column(Date)
