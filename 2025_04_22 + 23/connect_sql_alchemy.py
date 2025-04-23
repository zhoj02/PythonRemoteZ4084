from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


# connection string
db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/')

Session = sessionmaker(bind=db)

session = Session()

result = session.execute(text("SELECT 1"))
for row in result:
    print(row[0])
