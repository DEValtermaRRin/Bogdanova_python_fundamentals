# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?

def thesaurus(*names):
    rez = {}
    for name in names:
        first_letter = name[0].title()
        rez[first_letter] = rez.setdefault(first_letter, []) + [name.title()]
    return rez


def sort_dict_keys(sm_dict):
    value_list = [] + [*sm_dict.values()]
    keys_lst = list(sm_dict.keys())
    keys_lst.sort()
    value_list.sort()
    rez = dict(zip(keys_lst, value_list))
    return rez


names_dict = thesaurus('Ярослав', 'Алиса', 'Марина', 'Мария', 'Иван', 'Игорь', 'Яна', 'Даниил', 'Антон', 'Николай',
                       'Дарья', 'Михаил', 'Ангелина')

print(names_dict)
print(sort_dict_keys(names_dict))
