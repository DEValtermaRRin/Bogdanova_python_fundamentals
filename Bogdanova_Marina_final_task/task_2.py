# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class NumDivision:

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'{self.a}'

    def __truediv__(self, other):
        try:
            return NumDivision(self.a / other.a)
        except ZeroDivisionError:
            print('Деление на 0 недопустимо')


a = NumDivision(5)
b = NumDivision(10)
c = NumDivision(0)

print(a/b)
print(a/c)



