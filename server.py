import sqlite3
from sqlite3 import Error, Connection
from typing import Optional
from datetime import datetime
import socket
import json

BUFFER_SIZE = 1024
HOST = '127.0.0.1'
PORT = 8080
UTF8 = 'UTF-8'
PATH_DB = "stations.db"

DB_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS stations (
    st_num INTEGER,
    time_st TIMESTAMP, 
    alarm_1 INTEGER,
    alarm_2 INTEGER    
    );"""

DB_INSERT_ROW = """
    INSERT INTO stations VALUES
    (?, ?, ?, ?
    );"""


def insert_to_db(station_status: tuple, db_connection: Optional[Connection]) -> str:
    curs = db_connection.cursor()

    timestamp = datetime.now()
    time_st = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    st_num, alarm_1, alarm_2 = station_status
    station_status = curs.execute(DB_INSERT_ROW, (st_num, time_st, alarm_1, alarm_2))
    db_connection.commit()
    return station_status


def read_from_db(db_connection: Optional[Connection]) -> str:
    curs = db_connection.execute("SELECT * FROM stations")
    last_row_from_db = curs.fetchone()
    last_row_str = " ".join(map(str, last_row_from_db))
    return  last_row_str


def convert_from_raw(bytes_array: bytes) -> tuple:
    received_array = bytes_array.decode(UTF8)
    json_current_status = json.loads(received_array)
    return json_current_status


def create_db_connection(path_db: str) -> Optional[Connection]:
    db_connection = None
    try:
        db_connection = sqlite3.connect(path_db)
        db_connection.execute(DB_CREATE_TABLE)
        print("Connection to SQLite DB successful")
    except Error as err:
        print("The error", err, "occurred")
    return db_connection


def handle_request(sock: socket.socket, db_connection: Connection) -> None:
    station_status_raw = sock.recv(BUFFER_SIZE)
    station_status = convert_from_raw(station_status_raw)
    insert_to_db(station_status, db_connection)
    station_status_str = read_from_db(db_connection)
    print("Feedback: ", station_status_str)
    sock.send(station_status_str.encode(UTF8))


def main():
    db_connection = create_db_connection(PATH_DB)
    with socket.create_server((HOST, PORT)) as server:
        while True:
            sock, addr = server.accept()
            print("Client address:", addr)
            handle_request(sock, db_connection)


if __name__ == '__main__':
    main()
