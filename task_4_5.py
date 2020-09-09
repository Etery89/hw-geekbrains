"""
5. Реализовать формирование списка, используя функцию range()
и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().

"""
from functools import reduce


def my_func(elem, prev_elem):
    return elem * prev_elem


if __name__ == "__main__":
    test_list = [elem for elem in range(100, 1001) if elem % 2 == 0]
    print(reduce(my_func, test_list))
