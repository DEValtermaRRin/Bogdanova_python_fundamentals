# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    title = 'рисунка'

    def __init__(self):
        self.draw()

    def draw(self):
        print('Запуск отрисовки', end=' ')


class Pen(Stationery):

    def draw(self):
        print(f'ручкой - делаем основные штрихи {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'карандашом - делаем набросок {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'маркером - обводим контуры {self.title}')

a = Stationery()
drawing_pen = Pen()
a.draw()
drawing_pencil = Pencil()
a.draw()
drawing_handle = Handle()

