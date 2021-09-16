import sqlite3
from sqlite3 import Error, Connection

DB_SELECT_REQUEST = """
    SELECT * FROM stations
    ORDER BY time_st
    DESC LIMIT 1"""

db_connection = None
try:
    db_connection = sqlite3.connect("stations.db")
    db_connection.execute("""
    CREATE TABLE IF NOT EXISTS stations (
    st_num INTEGER,
    time_st TIMESTAMP, 
    alarm_1 INTEGER,
    alarm_2 INTEGER    
    );""")
    print("Connection to SQLite DB successful")
except Error as err:
    print("The error", err, "occurred")

curs = db_connection.execute(DB_SELECT_REQUEST)
last_row_from_db = curs.fetchone()

print("The last row is: ", last_row_from_db)
last_row_str = " ".join(map(str, last_row_from_db))
print("In string: ", last_row_str)