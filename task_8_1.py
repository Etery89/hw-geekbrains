"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    """
    Класс Дата, принимает строковый параметр date_str в виде "day-month-year"
    метод get_int_data - метод класса, применим лишь к классу Date и не применим к объектам,
    принимает строку такого же вида, что и конструктор, и возвращает кортеж из трёх чисел типа int - (day, months, year)
    метод validation_date - статический метод класса, проверяет корректность введённых данных так, чтобы значения
    дня и месяца не выходили за действительные пределы, а год соответствовал текущему.
    """
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def get_int_data(cls, date_str):
        list_str_date = date_str.split("-")
        new_list_date = []
        for str_ in list_str_date:
            if not str_.isdigit:
                raise Exception("В строке с датой должны быть только цифры, разделённые '-'")
            if str_[0] == "0":
                new_list_date.append(int(str_[1:]))
            else:
                new_list_date.append(int(str_))
        return new_list_date[0], new_list_date[1], new_list_date[2]

    @staticmethod
    def validation_date(day, month, year):
        list_num_from_day = [elem for elem in range(31)]
        list_num_from_month = [elem for elem in range(12)]
        if not day in list_num_from_day:
            raise Exception("День задан некорректным числом")
        if not month in list_num_from_month:
            raise Exception("Месяц задан некорректным числом")
        if not year == 2020:
            raise Exception("Введён год, не соответствующий текущему")
        print("Все данные введены корректно")



day1, month1, year1 = Date.get_int_data("20-09-2020")
print(day1)
print(month1)
print(year1)
Date.validation_date(day1, month1, year1)


