import os.path
import socket
import re
from datetime import datetime
import sqlite3
from sqlite3 import Connection
from typing import Optional

BUFFER_SIZE = 1024
HOST = '127.0.0.1'
PORT = 8888
UTF8 = 'UTF-8'
PATH_DB = "stations.db"

DB_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS stations (
    id INT AUTOINCREMENT PRIMARY KEY,
    time TIMESTAMP,
    num INT,
    flag_1 INT,
    flag_2 INT    
);
"""


def insert_to_db(station_status: str, db_connection: Optional[Connection]) -> str:
    conn = sqlite3.connect(PATH_DB)
    curs = conn.db_connection()

    timestamp = datetime.now()
    time_st = timestamp.strftime('%Y-%m-%d %H:%M:%S')

    pattern = re.compile(r";|, ")
    st_num, st_num, flag_1, flag_2 = pattern.split(station_status)

    result = curs.execute("""INSERT INTO stations (time, st_num, flag_1, flag_2)
                            VALUES (?, ?, ?, ?)""",
                          (time_st, st_num, flag_1, flag_2)
                          )
    db_connection.commit()
    return result


def convert_from_raw(bytes_array: bytes) -> str:
    decoded_array = str(bytes_array.decode(UTF8))
    print(decoded_array)
    return decoded_array

def create_db_connection(PATH_DB: str) -> Optional[Connection]:
    if os.path.exists(PATH_DB):
        print("Stations database file does exist")
        db_connection = sqlite3.connect(PATH_DB)
        print("Connection to SQLite DB is successful")
        handle_request(db_connection)
        return db_connection
    else:
        print("DB doesn't exist, but we gonna fix it")
        db_connection = sqlite3.connect(PATH_DB)
        curs = db_connection.cursor()
        curs.execute(DB_CREATE_TABLE)
        db_connection.commit()
        return db_connection


def handle_request(sock: socket.socket, db_connection: Connection) -> None:
    station_status_raw = sock.recv(BUFFER_SIZE)
    station_status = convert_from_raw(station_status_raw)
    status = insert_to_db(station_status, db_connection)
    sock.send(status.encode(UTF8))


def main():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind((HOST, PORT))
            db_connection = create_db_connection(PATH_DB)
            handle_request(sock, db_connection)


if __name__ == '__main__':
    main()
