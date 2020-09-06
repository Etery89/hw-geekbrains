"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def get_quotient_two_num(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if num2 != 0:
        return num1 / num2
    else:
        return "На 0 делить нельзя!"


if __name__ == "__main__":
    user_num1, user_num2 = input("Пожалуйста введите два числа для того,чтобы узнать их частное: ").split()
    print(get_quotient_two_num(user_num1, user_num2))
