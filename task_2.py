"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
hour = s / 3600
min = (s - hour * 3600) / 60
sec = s - hour * 3600 - min * 60
"""
time_in_seconds = int(input('Пожалуйста введите время в секундах: '))
hours = time_in_seconds // 3600
minutes = (time_in_seconds - hours * 3600) // 60
seconds = time_in_seconds - hours * 3600 - minutes * 60

if __name__ == "__main__":
    print("Ваше время: %d:%d:%d" % (hours, minutes, seconds))