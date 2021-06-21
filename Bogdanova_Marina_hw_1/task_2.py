# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
# будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# Внимание: новый список не создавать!!!

def digit_sum(arg):
    dig_sum = 0
    while arg != 0:
        dig_sum += arg % 10
        arg //= 10
    return dig_sum

#  Альбина, я пробовала решить без функции около 4-х часов(( никак мне без нее не обойтись(


number_sum = 0
number_sum_plus_17 = 0
odd_cube_lst = [number ** 3 for number in range(0, 1000) if number % 2 != 0]

for num in odd_cube_lst:
    if digit_sum(num) % 7 == 0:
        number_sum += num

for num in odd_cube_lst:
    num += 17
    if digit_sum(num) % 7 == 0:
        number_sum_plus_17 += num


print(odd_cube_lst)
print(number_sum)
print(number_sum_plus_17)
