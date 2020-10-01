"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""

class ZeroException(Exception):
    def __init__(self, msg):
        self.message = msg


if __name__ == "__main__":
    divisible = 10
    divisor = 0
    try:
        if divisor == 0:
            raise ZeroException("Делить на ноль нельзя!")
        quotient = divisible / divisor
    except ZeroException as err:
        print(err)
