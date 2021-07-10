# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями —запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

import sys
import pickle


def line_count(file):
    count = 0
    for _ in file:
        count += 1
    file.seek(0)
    return count


def user_hobby_dict(count_1, count_2):
    if count_1 == count_2:
        new_dict = dict(zip(USER, HOBBY))
    elif count_1 > count_2:
        for i in range(count_1 - count_2):
            HOBBY.append(['None'])
        new_dict = dict(zip(USER, HOBBY))
    else:
        sys.exit(1)
    return new_dict


with open('users.csv', 'r', encoding='utf-8') as f:
    with open('hobby.csv', 'r', encoding='utf-8') as f2:
        with open('user_hobby.csv', 'w', encoding='utf-8') as f3:
            count_user = line_count(f)
            count_hobby = line_count(f2)
            USER = map(str, (line.rstrip('\n').replace(',', ' ') for line in f))
            HOBBY = [line.rstrip('\n').split(',') for line in f2]
            user_hobby = user_hobby_dict(count_1=count_user, count_2=count_hobby)
            for key, val in user_hobby.items():
                f3.write(f'{key} : {val} \n')

with open('write_with_pickle.csv', 'wb') as f4:
    pickle.dump(user_hobby, f4)

