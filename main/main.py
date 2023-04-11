from get_data import get_last_operations
from get_data import load_data


def main():
    # Получаю список всех банковских операций
    file_data = load_data()

    # Получаю список 5 последних банковских операций
    last_operations = get_last_operations(file_data)

    # Делаю перебор экзмепляров
    for operation in last_operations:

    # Вывожу операции
        print(operation.print_operation())


    print(last_operations.__repr__())

if __name__ == "__main__":
    main()


