# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, \
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    __income_director = {'wage': 150000, 'bonus': 50000}
    __income_manager = {'wage': 100000, 'bonus': 30000}
    __income_freelancer = {'wage': 10000, 'bonus': 25000}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def position_salary(self):
        if self.position == 'director':
            _salary = sum(self.__income_director.values())
        elif self.position == 'manager':
            _salary = sum(self.__income_manager.values())
        else:
            _salary = sum(self.__income_freelancer.values())
        return _salary


class Position(Worker):

    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        print(full_name)

    def get_total_income(self):
        salary = self.position_salary()
        print(salary)


worker1 = Position('Ivan', 'Petrov', 'freelancer')
worker1.get_full_name()
worker1.get_total_income()
manager_1 = Position('Petr', 'Ivanov', 'manager')
manager_1.get_full_name()
manager_1.get_total_income()
director = Position('Sergey', 'Sergeev', 'director')
director.get_full_name()
director.get_total_income()