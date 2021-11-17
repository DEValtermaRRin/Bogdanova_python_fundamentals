# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, *args):
        self.num = complex(*args)

    def __str__(self):
        return f'{self.num}'

    def __add__(self, other):
        return ComplexNumber(self.num + other.num)

    def __mul__(self, other):
        return ComplexNumber(self.num * other.num)


a = ComplexNumber(3, 6)
b = ComplexNumber(2, 3)

print(a)
print(b)

print(a + b)
print(a * b)
