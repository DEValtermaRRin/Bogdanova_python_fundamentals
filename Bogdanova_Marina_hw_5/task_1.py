# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

def gen_odd_num(n):
    for num in range(1, n + 1):
        if num % 2:
            yield num


user_num = int(input('По какое число вывести нечётные числа?  '))
odd_num = gen_odd_num(user_num)
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
