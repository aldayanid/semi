import sqlite3
from sqlite3 import Error, Connection
from typing import Optional
import socket


BUFFER_SIZE = 1024
HOST = '127.0.0.1'
PORT = 8080
UTF8 = 'UTF-8'
PATH_DB = "stations.db"

DB_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS stations (
    time TIMESTAMP
    st_num INT,
    flag_1 INT,
    flag_2 INT    
);
"""

DB_INSERT_ROW = """
    INSERT INTO stations VALUES
    (?, ?, ?, ?);
    """

def insert_to_db(station_status: str, db_connection: Optional[Connection]) -> str:
# check if database exists, if not create it
    with sqlite3.connect(PATH_DB) as conn:
        conn.execute(DB_CREATE_TABLE)
    cursor = db_connection.cursor()
    result = cursor.execute(DB_INSERT_ROW)
    db_connection.commit()
    return result


def convert_from_raw(bytes_array: bytes) -> str:
    return str(bytes_array.decode(UTF8))


def create_connection(path_db: str) -> Optional[Connection]:
    db_connection = None
    try:
        db_connection = sqlite3.connect(path_db)
        print("Connection to SQLite DB successful")
    except Error as err:
        print("The error", err, "occurred")
    return db_connection


def handle_request(sock: socket.socket, db_connection: Connection) -> None:
    # station_status_raw = sock.recv(BUFFER_SIZE)
    # station_status = convert_from_raw(station_status_raw)
    # status = insert_to_db(station_status, db_connection)
    # sock.send(status.encode(UTF8))
    print(sock, db_connection)


def main():
    db_connection = create_connection(PATH_DB)
    with socket.create_server((HOST, PORT)) as server:
        while True:
            sock, addr = server.accept()
            print("Client address:", addr)
            handle_request(sock, db_connection)


if __name__ == '__main__':
    main()
