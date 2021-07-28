# 2.	Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, params):
        self.param = params

    @abstractmethod
    def count(self):
        pass


class Coat(Clothes):

    def __init__(self, params):
        super().__init__(params)
        self.size = self.param

    @property
    def count(self):
        amount = self.size / 6.5 + 0.5
        return amount


class Suit(Clothes):

    def __init__(self, params):
        super().__init__(params)
        self.height = self.param
        self.amount = None

    @property
    def count(self):
        self.amount = self.height * 2 + 0.3
        return self.amount

    def __str__(self):
        return


new_coat = Coat(48)
print(f'Для создания товара необходимо {new_coat.count:.02f} м. ткани')
new_suit = Suit(170)
print(f'Для создания товара необходимо {new_suit.count:.02f} м. ткани')
