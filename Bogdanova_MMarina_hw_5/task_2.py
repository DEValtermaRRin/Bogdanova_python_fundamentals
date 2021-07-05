# Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

n = int(input('По какое число вывести нечётные числа?  '))

odd_num = (num for num in range(1, n + 1) if num % 2)
odd_num_2 = (num for num in range(1, n + 1, 2))

print(*odd_num)
print(*odd_num_2)
