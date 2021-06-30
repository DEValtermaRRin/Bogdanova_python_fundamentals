# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.

def num_translate(eng_num, num_dict):
    return num_dict[eng_num] if eng_num in num_dict.keys() else None


numbers_translation = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

# print(num_translate('six', numbers_translation))

num = (input('Введите числительное от 0 до 10 на английском языке:  ')).lower()
print(f'{num} (eng.)  -  {num_translate(num, numbers_translation)} (рус.)')
