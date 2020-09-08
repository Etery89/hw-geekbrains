"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


def get_result(num_list):
    """
    возвращает генератор списка,
    в котором содержатся те значения исходного списка,
    что больше предыдущих
    :param num_list:
    :return: генератор списка
    """
    for num in range(1, len(num_list)):
        if num_list[num] > num_list[num - 1]:
            yield num_list[num]


if __name__ == "__main__":
    test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    print(test_list)
    result = [test_list[num] for num in range(1, len(test_list)) if test_list[num] > test_list[num - 1]]
    print(result)
    gen_result = get_result(test_list)
    print(list(gen_result))


