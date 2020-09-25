"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
хранилище = {принтеры: [], сканеры: [], ксероксы: []}
"""


class Warehouse:
    warehouse = {
        'printers': [],
        'scanners': [],
        'copiers': []
    }
    records_of_equipment = {
        1: {'printers': [], 'scanners': [], 'copiers': []},
        2: {'printers': [], 'scanners': [], 'copiers': []},
        3: {'printers': [], 'scanners': [], 'copiers': []}
    }

    def receiving_equipment(self, name_equip, cls_equip, num):
        self.warehouse[name_equip].append({cls_equip.name: [cls_equip, num]})

    def transfer_to_a_division(self, num_division, type_equip, cls_equip, num):
        self.records_of_equipment[num_division][type_equip].append([cls_equip, num])
        equip_in_wh = self.warehouse[type_equip]
        for equip in equip_in_wh:
            if cls_equip.name == list(equip.keys())[0]:
                num_equip_in_wh = equip[cls_equip.name][1]
                equip[cls_equip.name][1] = num_equip_in_wh - num


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


scanner_1 = Scanner("HP", 200)
warehouse_1 = Warehouse()
# print(scanner_1.name)
warehouse_1.receiving_equipment("scanners", scanner_1, 10)
# print(warehouse_1.warehouse)
printer_1 = Printer("Xerox", 400, True, False)
warehouse_1.receiving_equipment("printers", printer_1, 5)
# print(warehouse_1.warehouse)
warehouse_1.transfer_to_a_division(2, "scanners", scanner_1, 6)
print(warehouse_1.warehouse)
print(warehouse_1.records_of_equipment)

