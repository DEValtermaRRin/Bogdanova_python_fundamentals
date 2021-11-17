# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from abc import ABC, abstractmethod
import random
import string


class Warehouse:
    """ склад """

    def __init__(self):
        self.dict = {}
        self.dict_of_equipment = {}

    def goods_acceptance(self, equipment):
        self.dict.setdefault(equipment.equip_name(), []).append(f'{equipment.brand} - {equipment.model}')

    def invent_equipment(self, equipment, inv_number):
        self.dict_of_equipment.setdefault(f'{equipment.brand} - {equipment.model}', ''.join(inv_number))

    def distribution(self, equipment):
        if self.dict[equipment.equipment_name]:
            self.dict.setdefault(equipment.equipment_name).pop(0)
        if self.dict_of_equipment[f'{equipment.brand} - {equipment.model}']:
            self.dict_of_equipment.pop(f'{equipment.brand} - {equipment.model}')

    def count_equipment(self):
        count = 0
        for _ in self.dict_of_equipment.values():
            count += 1
        return count

    @staticmethod
    def making_inventory_number():
        random_symbols = string.digits + string.ascii_letters
        inv_number = ''.join(random.sample(random_symbols, 10))
        return inv_number


class OfficeEquipment(ABC):
    """ оргтехника """

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        self.equipment_name = self.__class__.__name__

    def equip_name(self):
        return f'{self.equipment_name}'

    def __add__(self, other):
        return OfficeEquipment(self.price + other.price)

    def __radd__(self, other):
        if not isinstance(other, OfficeEquipment):
            return self
        return self.__add__()

    @abstractmethod
    def action(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, brand, price, model):
        super(Printer, self).__init__(brand, price)
        self.model = model

    def action(self):
        print('Выводит на печать')


class Scanner(OfficeEquipment):
    def __init__(self, brand, price, model):
        super().__init__(brand, price)
        self.model = model

    def action(self):
        print('Сканирует')


class Xerox(OfficeEquipment):
    def __init__(self, brand, price, model):
        super().__init__(brand, price)
        self.model = model

    def action(self):
        print('Создает ксерокопии')


# создаем объект склада:
store = Warehouse()
# создаем объекты оргтехники:
printer_1 = Printer('HP', 8000, 'Laser 107')
printer_2 = Printer('CANON', 11000, 'PIXMA G2411')
scanner_1 = Scanner('CANON', 9000, 'Canoscan LIDE400')
xerox_1 = Xerox('Xerox', 13000, 'B205VNI')

# добавляем объекты на склад:
store.goods_acceptance(printer_1)
store.goods_acceptance(scanner_1)
store.goods_acceptance(xerox_1)
store.goods_acceptance(printer_2)
print(store.dict)


# присваиваем каждому объекту инвентаризационный номер:
inv_number_printer_1 = store.making_inventory_number()
inv_number_printer_2 = store.making_inventory_number()
inv_number_scanner_1 = store.making_inventory_number()
inv_number_xerox_1 = store.making_inventory_number()

# создаем словарь с инвентаризационными номерами:
store.invent_equipment(printer_1, inv_number_printer_1)
store.invent_equipment(printer_2, inv_number_printer_2)
store.invent_equipment(scanner_1, inv_number_scanner_1)
store.invent_equipment(xerox_1, inv_number_xerox_1)
print(store.count_equipment())  # количество оргтехники на складе
print(store.dict_of_equipment)

# переносим принтер 1 в бухгалтерию
store.distribution(printer_1)
print(store.dict)
print(store.count_equipment())  # количество оргтехники на складе

# узнаем сколько всего было затрачено на закупку оргтехники
total_price = printer_1.price + printer_2.price + scanner_1.price + xerox_1.price
print(total_price)
