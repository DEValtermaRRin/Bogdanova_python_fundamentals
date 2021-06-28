# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Например:
# >>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": "Петр Алексеев"
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Сможете ли вы вернуть отсортированный по ключам словарь?

def thesaurus(*args):
    new_dict = {}
    names_dict = {}
    for name in args:
        idx = name.find(' ')
        first_letter_surname = name[idx+1].title()
        names_dict[first_letter_surname] = names_dict.setdefault(first_letter_surname, []) + [name.title()]
    for key, val in names_dict.items():
        new_dict[key] = thesaurus_adv(val)
    return new_dict


def thesaurus_adv(lists):
    mini_dict = {}
    for name in lists:
        first_letter_name = name[0]
        mini_dict[first_letter_name] = mini_dict.setdefault(first_letter_name, []) + [name.title()]
    return mini_dict


print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
