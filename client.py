import sys


def select_file(selected_num: int) -> str:

    while True:
        if selected_num == 1:
            # current_file = open("station_1.txt", "w", encoding='utf-8')
            current_file = str("station_1.txt")
            return current_file
        elif selected_num == 2:
            current_file = str("station_2.txt")
            return current_file
        elif selected_num == 3:
            current_file = str("station_3.txt")
            return current_file
        else:
            print("Error! Please use only one of these numbers: 1, 2, 3")
            continue #return to the beginning og the loop, again????? Continue doesn't work


def check_connection() -> bool:
    return True


def read_from_file(file_name: str) -> str:
    line = ""
    with open(file_name, 'r', encoding='UTF-8') as file:
        while line in file.readline().rstrip():
            print(line)


def send_to_server(data_from_file: str, connection: bool) -> bool:
    print("Everything is OK")


def main():
    selected_num = int(input("Please select the station number,\njust input the number of station:\n 1, 2 or 3:\n"))
    selected_file = select_file(selected_num)
    print(selected_file)
    data_from_file = read_from_file(selected_file)
    print(data_from_file)
    check_connection()
    send_to_server(data_from_file, connection=True)


if __name__ == '__main__':
    main()
