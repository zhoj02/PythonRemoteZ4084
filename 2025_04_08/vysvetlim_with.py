#pip install mysql-connector-python
from mysql.connector import connect

pripojeni = connect(host="localhost", user='root', password='YourNewPassword')
print(pripojeni.user)
