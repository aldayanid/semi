import sqlite3
from sqlite3 import Error, Connection
from typing import Optional

PATH_DB = "laptops.db"


def create_connection(path_to_db: str) -> Optional[Connection]:
    connection = None
    try:
        connection = sqlite3.connect(path_to_db)
        print("Connection to SQLite DB successful")
    except Error as e:
        print("The error", e, "occurred")

    return connection


def exec_request(request_number: int, connection: Optional[Connection]) -> str:
    cursor = connection.cursor()

    if request_number == 1:
        query_result = ""
        result = cursor.execute("SELECT * FROM laptops;")
        for record in result:
            query_result += str(record) + "\n"
        return query_result
    elif request_number == 2:
        result = cursor.execute("SELECT * FROM laptops;")
        return result
    else:
        return "Quit"


def main():
    connection = create_connection(PATH_DB)
    print("Please choose one option:\n1. Show all products\n2. Insert a new laptop\n3. Exit\n")
    request_number = int(input("Your choose: "))
    result = exec_request(request_number, connection)
    print(result)


if __name__ == '__main__':
    main()
