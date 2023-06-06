from csv import reader, DictReader


def creating():
    file = 'phone.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия,Имя,Номер\n')


def record_info():
    info = get_info()
    writing_csv(info)


def writing_csv(info):
    file = 'phone.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]}\n')


def get_info():
    info = []
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    info.append(last_name)
    info.append(first_name)
    phone_number = ''
    flag = False
    while not flag:
        try:
            phone_number = input("Введите номер: ")
            if len(phone_number) != 11:
                print("В номере должно быть 11 цифр")
            else:
                phone_number = int(phone_number)
                flag = True

        except:
            print("В номере должны быть только цифры")
    info.append(phone_number)
    return info


def reading_csv(file):
    with open(file, encoding='utf-8') as data:
        res = list(DictReader(data))
    return res


def delete_info(file):
    with open(file, "r", encoding='utf-8') as data:
        num = data.read()
        num_line = num.split("\n")
        index = int(input("Введите номер записи (Начало с 0): ")) + 1
        num_line.pop(index)
    with open(file, "w", encoding='utf-8') as data:
        data.write("\n".join(num_line))


def edit_info(file):
    with open(file, "r", encoding='utf-8') as data:
        num = data.read()
        index = int(input("Введите номер записи (Начало с 0): ")) + 1
        elements = num.split("\n")
        first = input("Введите фамилию: ")
        last = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        elements[index] = f'{first},{last},{phone}'
        print(index)
    with open(file, "w", encoding='utf-8') as f:
            f.write("\n".join(elements))
