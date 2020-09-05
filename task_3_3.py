"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(*args):
    numbers = []
    for num in range(len(args)):
        numbers.append(args[num])
    max_1 = max(numbers)
    numbers.remove(max_1)
    max_2 = max(numbers)
    return max_1 + max_2


if __name__ == "__main__":
    print(my_func(3, 5, 1))
    print(my_func(8, 7, 5, 4, 2))
    print(my_func(9, 16, 46, 82, 7, 5, 3, 4))
