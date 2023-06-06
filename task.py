from utils import *
from os.path import exists

def main():
    while True:
        path = 'phone.csv'
        print()
        print("ВЫБЕРИТЕ ДЕЙСТВИЕ:")
        print("read - Просмотреть записи")
        print("write - Добавить запись")
        print("delete - Удалить запись")
        print("change - Изменить запись")
        print("exit - Выйти")

        step = input("Введите ответ: ")
        print()
        if step == 'exit':
             break
        elif step == 'write':
            flag = exists(path)
            if not flag:
                creating()
                record_info()
            else:
                record_info()
        elif step == 'read':
            print(reading_csv(path))
        elif step == 'delete':
            delete_info(path)
        elif step == 'change':
            edit_info(path)
main()