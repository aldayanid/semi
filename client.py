import socket
from subprocess import Popen


BUFFER_SIZE = 1024
HOST = '127.0.0.1'
PORT = 8888
UTF8 = 'UTF-8'


def select_file(selected_num: int) -> str:

    while 1:
        if selected_num == 1:
            return str("station_1.txt")
        elif selected_num == 2:
            return str("station_2.txt")
        elif selected_num == 3:
            return str("station_3.txt")
        else:
            print("Error! Please use only one of these numbers: 1, 2, 3")
            break
# How to get rid of the errors???


def read_from_file(file_name: str) -> list:
    with open(file_name, 'r', encoding=UTF8) as file:
        return file.read().split("\n")


def send_to_server(data_from_file: str) -> bool:
    #Popen("python server.py")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, PORT))
        sock.send(data_from_file.encode(UTF8))
        status = sock.recv(BUFFER_SIZE)
        print(status, "has been received")


def main():
    selected_num = int(input("Please select the station number,\njust input the number of station:\n 1, 2 or 3:\n"))
    selected_file_name = select_file(selected_num)
    data_from_file = str(read_from_file(selected_file_name))
    print(data_from_file)
    send_to_server(data_from_file)


if __name__ == '__main__':
    main()
