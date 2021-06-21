# 3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
# задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.

root = 'процент'
end_1 = 'а'
end_2 = 'ов'
numbers_for_1 = [2, 3, 4]
numbers_for_2 = [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

num = int(input('Введите число от 0 до 20:  '))
if num == 1:
    print(f'{num} {root}')
elif num in numbers_for_1:
    print(f'{num} {root}{end_1}')
elif num in numbers_for_2:
    print(f'{num} {root}{end_2}')
else:
    print('Вы ввели некорректное число')

# для проверки

for num in range(0, 22):
    if num == 1:
        print(f'{num} {root}')
    elif num in numbers_for_1:
        print(f'{num} {root}{end_1}')
    elif num in numbers_for_2:
        print(f'{num} {root}{end_2}')
    else:
        print('Вы ввели некорректное число')