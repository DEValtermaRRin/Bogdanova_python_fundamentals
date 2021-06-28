# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(eng_num, num_dict):
    if eng_num.istitle():
        eng_num = eng_num.lower()
        return (num_dict[eng_num]).title() if eng_num in num_dict else None
    else:
        return num_dict[eng_num] if eng_num in num_dict else None


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

num = input('Введите числительное от 0 до 10 на английском языке:  ')
print(f'{num} (eng.)  -  {num_translate_adv(num, numbers_translation)} (рус.)')
