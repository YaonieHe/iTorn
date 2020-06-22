import pymssql

SERVER = '222.160.142.50:8153'

SERVER_USERNAME = 'torn'
SERVER_PASSWORD = 'torn1'

DB_NAME = 'torncity'

conn = pymssql.connect(SERVER, SERVER_USERNAME, SERVER_PASSWORD, DB_NAME)

cursor = conn.cursor()

print(conn)

cursor.execute("use TornCity;")
cursor.execute("SELECT * from TornBingWaAllData")
row = cursor.fetchall()
print (row)
