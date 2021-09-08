import json
import socket

BUFFER_SIZE = 1024
HOST = '127.0.0.1'
PORT = 8080
UTF8 = 'UTF-8'


def select_file(selected_num: int) -> str:

    try:
        if selected_num == 1:
            return str("station_1.txt")
        elif selected_num == 2:
            return str("station_2.txt")
        elif selected_num == 3:
            return str("station_3.txt")
    except NameError:
            print("Error! Please use only one of these numbers: 1, 2, 3")  ##  TODO How to get rid of the errors???


def read_from_file(file_name: str) -> str:
    with open(file_name, 'r', encoding=UTF8) as file:
        current_status = file.read().split("\n")
        json_current_status = json.dumps(current_status)
        return json_current_status


def send_to_server(data_from_file: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.send(data_from_file.encode(UTF8))
        status_bytes = sock.recv(BUFFER_SIZE)
        print("Received from the server:", status_bytes.decode(UTF8))


def main():
    selected_num = int(input("Please select the station number,\njust input the number of station:\n 1, 2 or 3:\n"))
    selected_file_name = select_file(selected_num)
    data_from_file = read_from_file(selected_file_name)
    print("Sending to the server:", data_from_file)
    send_to_server(data_from_file)


if __name__ == '__main__':
    main()
