# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class SomeDate:
    def __init__(self, dd, mm, yyyy):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

    @classmethod
    def take_num_from_date(cls, data):
        dd, mm, yyyy = map(int, data.split('-'))
        return cls(dd, mm, yyyy)

    @staticmethod
    def validator(data):
        dd, mm, yyyy = map(int, data.split('-'))
        if dd > 31 and mm > 12 and yyyy > 2100:
            raise ValueError('Введена некорректная дата')


date_1 = SomeDate.take_num_from_date('11-12-1989')
date_2 = SomeDate.validator('11-12-1989')
date_3 = SomeDate.take_num_from_date('32-13-3333')
date_4 = SomeDate.validator('32-13-3333')
