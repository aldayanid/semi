import sys


def select_file(selected_num) -> str:

    while True:
        if selected_num == 1:
            current_file = open("station_1.txt", "w", encoding='utf-8')
            return current_file
        elif selected_num == 2:
            current_file = open("station_2.txt", "w", encoding='utf-8')
            return current_file
        elif selected_num == 3:
            current_file = open("station_3.txt", "w", encoding='utf-8')
            return current_file
        else:
            print("Error! Please use only one of these numbers: 1, 2, 3")
            continue #return to the beginning og the loop, again?????


def read_from_file():
    pass


def check_connection():
    pass


def send_to_server():
    pass


def main():
    selected_num = int(input("Please select the station number,\njust input the number of station:\n 1, 2 or 3:\n"))
    selected_file = select_file(selected_num)
    print(selected_file)
    read_from_file()
    check_connection()
    send_to_server()


if __name__ == '__main__':
    main()
