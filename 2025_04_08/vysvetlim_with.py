#pip install mysql-connector-python
from mysql.connector import connect

pripojeni = connect(host="localhost", user='root', password='YourNewPassword')
pripojeni.close()
print(pripojeni.user)
# Context Manager
with connect(host="localhost", user='root', password='YourNewPassword') as pripojeni:
    print(pripojeni.user)

print("Jsem jinde")