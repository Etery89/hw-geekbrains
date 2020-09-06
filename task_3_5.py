"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу.
"""


def sum_string_nums(string_list):
    numbers = []
    for num in string_list:
        num = int(num)
        numbers.append(num)
    sum_numbers = sum(numbers)
    return sum_numbers


if __name__ == "__main__":
    count_sum = 0
    summa = 0
    while True:
        numbers_string = input("Пожалуйста введите числа через пробел (для выхода введите q): ").split()
        if numbers_string == ['q']:
            print("Выход из программы")
            break
        elif numbers_string[len(numbers_string) - 1] == "q":
            new_numbers_list = numbers_string[:(len(numbers_string) - 1)]
            sum_new_numbers_list = sum_string_nums(new_numbers_list)
            summa = summa + sum_new_numbers_list
            print(f"Сумма введённых чисел: {summa}", "Выход из программы", sep="\n")
            break
        else:
            if count_sum == 0:
                summa = sum_string_nums(numbers_string)
                print(f"Сумма введённых чисел: {summa}")
                count_sum += 1
            else:
                new_summa = sum_string_nums(numbers_string)
                summa += new_summa
                print(f"Сумма введённых чисел: {summa}")
