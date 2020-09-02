"""
6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

products = []
count = 1

num_products = int(input("Пожалуйста введите общее число видов товаров: "))

for num in range(num_products):
    name_of_product = input("Пожалуйста введите название товара: ")
    price = int(input("Пожалуйста введите цену товара: "))
    quantity = int(input("Введите количество единиц товара: "))
    unit_of_measurement = input("В каких единицах измеряется товар: ")
    structure_product = dict(
        наименование=name_of_product,
        цена=price,
        количество=quantity,
        единицы=unit_of_measurement
        )
    info_one_product = (count, structure_product)
    products.append(info_one_product)
    count += 1

print(f"Сформированная таблица товаров: {products}")

name_list = []
price_list = []
quantity_list = []
unit_list = []

analytics = {}

for num in range(len(products)):
    name_list.append(products[num][1][list(products[0][1].keys())[0]])
    price_list.append(products[num][1][list(products[0][1].keys())[1]])
    quantity_list.append(products[num][1][list(products[0][1].keys())[2]])
    unit_list.append(products[num][1][list(products[0][1].keys())[3]])

analytics[list(products[0][1].keys())[0]] = name_list
analytics[list(products[0][1].keys())[1]] = price_list
analytics[list(products[0][1].keys())[2]] = quantity_list
analytics[list(products[0][1].keys())[3]] = list(set(unit_list))


print(f"Статистика по таблице товаров: {analytics}")
