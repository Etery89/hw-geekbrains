"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
    warehouse = {}

    def __init__(self, name, num):
        self.name = name
        self.num = num

    def get_warehouse(self):
        self.warehouse[self.name] = self.num


class OfficeEquipment:
    def __init__(self, name):
        self.name = name


class Printer(OfficeEquipment):
    color = False
    cartridge_included = False

    def __init__(self, name, amount_of_paper, cartridge_included, color):
        super().__init__(name)
        self.amount_of_paper = amount_of_paper
        self.cartridge_included = cartridge_included
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed


class Copier(OfficeEquipment):
    def __init__(self, name, type_print, copy_permission):
        super().__init__(name)
        self.type_print = type_print
        self.copy_permission = copy_permission
