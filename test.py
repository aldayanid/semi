import sqlite3
from sqlite3 import Error, Connection

conn = sqlite3.connect('stations.db')
cursor = conn.execute("SELECT * FROM stations")
result = cursor.fetchone()
print("Operation done successfully", result)

conn.close()
