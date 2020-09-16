"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    # title = "Stationery"
    # #
    def __init__(self):
        self.title = "Stationery"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки маркером")


if __name__ == "__main__":
    stationery = Stationery()
    pen = Pen()
    pencil = Pencil()
    handle = Handle()
    stationery.draw()
    pen.draw()
    pencil.draw()
    handle.draw()
    pen.title = "Ручка"
    print(stationery.title)
    print(pen.title)
